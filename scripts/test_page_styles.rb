# Regression checks for preserving rendered content while relocating component CSS.
require 'jekyll'
require_relative '../_plugins/page_styles'
Document = Struct.new(:output, :output_ext)
def render(html, extension = '.html')
  document = Document.new(html, extension)
  Jekyll::Hooks.trigger(:pages, :post_render, document)
  document.output
end

a = '<style data-page-styles media="screen">.first { color: red }</style>'
b = '<style data-page-styles>.second { color: blue }</style>'
html = "<html><head><style>.base { color: black }</style></head><body><p>Before</p>#{a}<p>After</p>#{b}</body></html>"
output = render(html)
head, body = output.split('</head>', 2)
raise 'Component style order changed' unless head.index('.base') < head.index('.first') && head.index('.first') < head.index('.second')
raise 'Media attribute or body content changed' unless head.include?(a) && body.include?('<p>Before</p><p>After</p>')
raise 'Styles remain in body' if body.include?('<style')

script = '<script>const sample = "<style>.sample { color: red }</style>";</script>'
comment = '<!-- <style>.example { color: blue }</style> -->'
output = render("<html><head></head><body>#{script}#{comment}#{a}</body></html>")
raise 'Script or comment content was changed' unless output.include?(script) && output.include?(comment)

xml = '<root><style data-page-styles>example</style></root>'
raise 'Non-HTML output changed' unless render(xml, '.xml') == xml
puts '3 component-style regression checks passed.'
