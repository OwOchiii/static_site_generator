from textnode import *
from copystatic import copy_files_recursive
import os
import shutil
import generate_page
dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page.generate_pages_recursive("content", "./template.html", "./public")
    text_node = TextNode('Hello, World!', TextType.bold)
    print(text_node)

main()