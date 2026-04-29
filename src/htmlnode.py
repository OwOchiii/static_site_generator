class HTMLNode:
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag #string
        self.value = value #string
        self.children = children #list of HTMLNode
        self.props = props #dict. example: {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self):
        return f'HTMLNode({self.tag},{self.value},{self.props_to_html()})'

