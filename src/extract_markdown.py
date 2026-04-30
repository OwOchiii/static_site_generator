import re

def extract_markdown_image(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return match

def extract_markdown_link(text):
    match = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return match