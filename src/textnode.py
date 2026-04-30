from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    text = ''
    bold = '**'
    italic = '_'
    code = '`'
    link = '[anchor text](url)'
    image_link = '[image link](url)'

class TextNode:
    def __init__(self, text='', text_type=TextType.text, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return False

    def __repr__(self):
        return f'TextNode({self.text},{self.text_type},{self.url})'

    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.text:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.bold:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.italic:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.code:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.link:
            if text_node.url is None:
                raise ValueError("URL is required for link text type")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == TextType.image_link:
            if text_node.url is None:
                raise ValueError("URL is required for image link text type")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        else:
            raise ValueError("Invalid text type")

