import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.text)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("Different text", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.link, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.link, "https://www.example.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.link, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.link, "https://www.otherexample.com")
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", TextType.bold)
        self.assertEqual(str(node), "TextNode(This is a text node,TextType.bold,None)")

    def test_url(self):
        url_node = TextNode("This is a text node", TextType.link)
        self.assertEqual(str(url_node), "TextNode(This is a text node,TextType.link,None)")

    def test_text(self):
        node = TextNode("This is a text node", TextType.text)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()