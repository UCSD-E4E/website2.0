require "tmpdir"
require "fileutils"
require "jekyll"
require_relative "../_plugins/site_version"

# Render the real footer without rebuilding the image-heavy website. Verify that
# changing only VERSION updates the output and that invalid versions stop a build.
Dir.mktmpdir("website-version") do |root|
  source = File.join(root, "source")
  destination = File.join(root, "output")
  FileUtils.mkdir_p(File.join(source, "_includes"))
  FileUtils.cp(File.expand_path("../_includes/footer.html", __dir__), File.join(source, "_includes/footer.html"))
  File.write(File.join(source, "_includes/social.html"), "")
  File.write(File.join(source, "index.html"), "---\n---\n{% include footer.html %}\n")
  File.write(File.join(source, "CHANGELOG.md"), "Private release notes")

  config = Jekyll.configuration({
    "source" => source,
    "destination" => destination,
    "title" => "E4E",
    "url" => "https://e4e.ucsd.edu",
    "exclude" => YAML.safe_load(File.read(File.expand_path("../_config.yml", __dir__))).fetch("exclude"),
    "quiet" => true
  })

  [File.read(File.expand_path("../VERSION", __dir__)).strip, "2.3.0"].each do |version|
    File.write(File.join(source, "VERSION"), "#{version}\n")
    Jekyll::Site.new(config).process
    html = File.read(File.join(destination, "index.html"))
    raise "Footer did not render VERSION #{version}" unless html.include?("Website v#{version}</p>")
    raise "VERSION leaked into output" if File.exist?(File.join(destination, "VERSION"))
    raise "Changelog leaked into output" if File.exist?(File.join(destination, "CHANGELOG.md"))
  end

  File.write(File.join(source, "VERSION"), "02.2.1\n")
  begin
    Jekyll::Site.new(config).process
    raise "Invalid version was accepted"
  rescue Jekyll::Errors::FatalException => error
    raise unless error.message.include?("VERSION must contain")
  end
end

puts "Website version rendering, exclusions, and validation passed"
