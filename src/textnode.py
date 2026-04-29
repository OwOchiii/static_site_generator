from enum import Enum

class TextType(Enum):
    text = ''
    bold = '**'
    italic = '_'
    code_text = '`'
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