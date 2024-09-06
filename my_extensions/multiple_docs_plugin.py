import os
import shutil
from mkdocs.plugins import BasePlugin


class MultipleDocsPlugin(BasePlugin):
    def on_pre_build(self, config):
        # 定义你想合并的目录列表
        extra_dirs = ["extra_docs1", "extra_docs2"]  # 将这些替换为你需要合并的目录路径

        # 遍历目录，将它们的内容复制到主 docs_dir
        for extra_dir in extra_dirs:
            for item in os.listdir(extra_dir):
                s = os.path.join(extra_dir, item)
                d = os.path.join(config["docs_dir"], item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)  # 合并文件夹
                else:
                    shutil.copy2(s, d)  # 合并单个文件
