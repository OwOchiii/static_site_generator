import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code),
                TextNode(" word", TextType.text),
            ]
        )

    def test_split_nodes_delimiter_multiple(self):
        node = TextNode("This is text with a **bold** and *italic* word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bold", TextType.bold),
                TextNode(" and ", TextType.text),
                TextNode("italic", TextType.italic),
                TextNode(" word", TextType.text),
            ]
        )


if __name__ == "__main__":
    unittest.main()
