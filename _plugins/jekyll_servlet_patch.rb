# frozen_string_literal: true

# Monkey-patch for Jekyll 3.9.5 compatibility with Ruby 3.4
# Fixes: NoMethodError: undefined method 'key?' for nil
# in jekyll/commands/serve/servlet.rb:191 (conditionally_inject_charset)
#
# The issue is that @mime_types_charset (from server.config[:MimeTypesCharset])
# can be nil, causing a crash on every GET request.

require "jekyll/commands/serve/servlet"

module Jekyll
  module Commands
    class Serve
      class Servlet < WEBrick::HTTPServlet::FileHandler
        private

        def conditionally_inject_charset(res)
          return if @mime_types_charset.nil?

          typ = res.header["content-type"]
          return unless @mime_types_charset.key?(typ)
          return if %r!;\s*charset=!.match?(typ)

          res.header["content-type"] = "#{typ}; charset=#{@jekyll_opts["encoding"]}"
        end
      end
    end
  end
end
