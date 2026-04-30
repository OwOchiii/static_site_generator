from src.text_to_textnode import split_nodes_image
from src.textnode import TextNode,TextType


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.text,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.text),
            TextNode("image", TextType.image_link, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text),
            TextNode(
                "second image", TextType.image_link, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )