import re

def extract_markdown_image(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return match

def extract_markdown_link(text):
    match = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return match

def extract_title(markdown):
    match = re.search(r"^# (.*)$", markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    raise Exception("No H1 header found")
