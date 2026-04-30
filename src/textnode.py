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

    def text_node_to_html_node(self):
        if self.text_type == TextType.text:
            return LeafNode(None, self.text)
        elif self.text_type == TextType.bold:
            return LeafNode("b", self.text)
        elif self.text_type == TextType.italic:
            return LeafNode("i", self.text)
        elif self.text_type == TextType.code_text:
            return LeafNode("code", self.text)
        elif self.text_type == TextType.link:
            if self.url is None:
                raise ValueError("URL is required for link text type")
            return LeafNode("a", self.text, {"href": self.url})
        elif self.text_type == TextType.image_link:
            if self.url is None:
                raise ValueError("URL is required for image link text type")
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
        else:
            raise ValueError("Invalid text type")

