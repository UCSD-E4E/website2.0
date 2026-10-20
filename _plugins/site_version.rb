# VERSION is shared by the rendered site, deployment stamp, and release workflow.
module Jekyll
  class SiteVersion < Generator
    safe true
    priority :highest

    def generate(site)
      version = File.read(site.in_source_dir("VERSION")).strip
      unless version.match?(/\A(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\z/)
        raise Errors::FatalException, "VERSION must contain a stable semantic version (MAJOR.MINOR.PATCH)"
      end
      site.config["website_version"] = version
    end
  end
end
