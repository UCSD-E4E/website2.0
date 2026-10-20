require 'jekyll'
require 'jekyll-resize'
require 'mini_magick'
require 'tmpdir'
require 'fileutils'

# Optional local fallback when only GraphicsMagick is installed. CI uses the
# normal ImageMagick backend used by the website.
MiniMagick.configure { |config| config.cli = :graphicsmagick } if ENV['IMAGE_TEST_GRAPHICSMAGICK'] == '1'

module ImageProcessingCount
  class << self
    attr_accessor :count
  end
  self.count = 0

  def _process_img(*args)
    ImageProcessingCount.count += 1
    super
  end
end
Jekyll::Resize.prepend(ImageProcessingCount)

class ImageCacheIntegrationTest
  def assert(condition, message)
    raise message unless condition
  end

  def assert_equal(expected, actual, message = 'unexpected image processing count')
    assert(expected == actual, "#{message}: expected #{expected.inspect}, got #{actual.inspect}")
  end

  def refute(condition, message)
    assert(!condition, message)
  end

  def test_only_missing_variants_are_processed_and_unused_images_are_not_published
    Dir.mktmpdir('e4e-image-build-') do |root|
      @root = root
      FileUtils.mkdir_p(File.join(root, 'assets'))
      image('red')
      assert_equal 1, build('8x8')
      assert_equal 0, build('8x8'), 'unchanged build should reuse its output'
      assert_equal 1, build('8x8', '4x4'), 'template-only change should add just one variant'
      assert_equal 0, build('8x8'), 'unused variants should be retained without reprocessing'
      assert_equal 1, Dir.glob(File.join(root, '_site/cache/resize/*')).size
      refute Dir.exist?(File.join(root, '_site/cache/resize_temp')), 'unused cache must stay unpublished'
      prepare # Simulate a build interrupted immediately after cache preparation.
      assert_equal 0, build('8x8', '4x4'), 'retained variant should survive an interrupted build'
      image('blue')
      assert_equal 1, build('8x8'), 'changed source image must be regenerated'
    end
  end

  def image(color)
    MiniMagick::Tool::Convert.new do |command|
      command.size '16x16'
      command << "xc:#{color}"
      command << File.join(@root, 'assets/image.png')
    end
  end

  def prepare
    script = File.expand_path('image-cache.cjs', __dir__)
    code = 'require(process.argv[1]).prepareImageCache(process.argv[2]).catch(e => { console.error(e); process.exit(1); })'
    assert system('node', '-e', code, script, @root), 'cache preparation failed'
  end

  def build(*sizes)
    File.write(File.join(@root, 'index.html'), "---\n---\n" + sizes.map { |size| "<img src=\"{{ '/assets/image.png' | resize: '#{size}' }}\">" }.join("\n"))
    prepare
    ImageProcessingCount.count = 0
    config = Jekyll.configuration('source' => @root, 'destination' => File.join(@root, '_site'),
                                  'baseurl' => '', 'exclude' => ['cache/resize_temp'], 'quiet' => true)
    Jekyll::Site.new(config).process
    html = File.read(File.join(@root, '_site/index.html'))
    html.scan(/src="([^"]+)"/).flatten.each do |url|
      assert File.file?(File.join(@root, '_site', url)), "missing generated image: #{url}"
    end
    ImageProcessingCount.count
  end
end

ImageCacheIntegrationTest.new.test_only_missing_variants_are_processed_and_unused_images_are_not_published
puts 'Image reuse, invalidation, interrupted-build recovery and publish exclusions passed.'
