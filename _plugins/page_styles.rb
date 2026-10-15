# Opted-in component CSS is global even when authored in a page/include. Place it
# after the shared stylesheets in <head>, preserving rule order and media attrs.
# This keeps Liquid-generated carousel/gallery CSS unchanged and valid HTML.
Jekyll::Hooks.register [:pages, :documents], :post_render do |document|
  next unless document.output_ext == '.html'
  html = document.output
  body_start = html.index(/<body\b[^>]*>/i)
  next unless body_start && html.match?(%r{</head>}i)

  styles = []
  # Ignore raw script/text content and HTML comments; only explicitly marked
  # component styles move. Future author examples and scripts remain untouched.
  tokens = %r{<!--.*?-->|<(script|textarea|iframe|template)\b[^>]*>.*?</\1\s*>|<style\b[^>]*>.*?</style\s*>}mi
  body = html[body_start..].gsub(tokens) do |token|
    if token.match?(/\A<style\b[^>]*\bdata-page-styles(?:[\s=>])/i)
      styles << token
      ''
    else
      token
    end
  end
  next if styles.empty?

  head = html[0...body_start].sub(%r{</head>}i) { "#{styles.join("\n")}\n</head>" }
  document.output = head + body
end
