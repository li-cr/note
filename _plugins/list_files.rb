# _plugins/list_files.rb

module Jekyll
    class ListFiles < Liquid::Tag
      def initialize(tag_name, text, tokens)
        super
        @text = text.strip
      end
  
      def render(context)
        site = context.registers[:site]
        files = site.static_files.map { |file| file.path }
        files.map { |file| "<a href='#{file}'>#{file}</a>" }.join("<br>")
      end
    end
  end
  
  Liquid::Template.register_tag('list_files', Jekyll::ListFiles)
  