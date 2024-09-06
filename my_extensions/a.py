# my_extensions/code_block_extension.py
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import re


class CodeBlockExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(CodeBlockPattern(), "code_block", 175)


class CodeBlockPattern(InlineProcessor):
    def handleMatch(self, m, data):
        # 实现你的解析逻辑，例如提取 file:"dawd"
        code_block_content = m.group(0)
        # 解析逻辑，例如提取 file:"dawd" 信息
        # 返回处理后的内容
        return "", m.start(), m.end()


def makeExtension(**kwargs):
    return CodeBlockExtension(**kwargs)
