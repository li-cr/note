from mkdocs.plugins import BasePlugin


class MyMkdocsPlugin(BasePlugin):
    def on_pag_content(self, content, page, config):
        return content
