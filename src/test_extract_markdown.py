import unittest
from extract_markdown import extract_markdown_image, extract_markdown_link, extract_title

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        matches = extract_markdown_image(text)
        self.assertEqual(
            matches,
            [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        )

    def test_extract_markdown_link(self):
        text = "This is text with a [link](https://www.google.com) and [another](https://boot.dev)"
        matches = extract_markdown_link(text)
        self.assertEqual(
            matches,
            [("link", "https://www.google.com"), ("another", "https://boot.dev")]
        )

    def test_extract_markdown_link_with_image(self):
        # Links should not accidentally extract images
        text = "This is text with a [link](https://www.google.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_link(text)
        self.assertEqual(
            matches,
            [("link", "https://www.google.com")]
        )

    def test_extract_title(self):
        markdown = "# Hello   \n\nSome body text"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_missing_h1(self):
        markdown = "## Not a title\n\nSome body text"
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
