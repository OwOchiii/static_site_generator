import sys

from textnode import *
from copystatic import copy_files_recursive
import os
import shutil
import generate_page
from pathlib import Path
dir_path_static = "./static"
dir_path_public = "./docs"

def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath += "/"

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page.generate_pages_recursive("content", "./template.html", dir_path_public, basepath)
    Path(dir_path_public).mkdir(parents=True, exist_ok=True)
    (Path(dir_path_public) / ".nojekyll").write_text("")
    text_node = TextNode('Hello, World!', TextType.bold)
    print(text_node)

main()