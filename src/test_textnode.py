import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_textype(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("Hello world", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Hello world", TextType.LINK, "https://www.boot.dev/lessons")
        self.assertNotEqual(node, node2)

    def test_same_text_diff_url(self):
        node = TextNode("Same text node", TextType.CODE, "www.oneurl.com")
        node2 = TextNode("Same text node", TextType.CODE, "www.twourl.com")
        self.assertNotEqual(node, node2)

    def test_same_text_one_url_none(self):
        node = TextNode("Same text node", TextType.CODE, "www.url.com")
        node2 = TextNode("Same text node", TextType.CODE)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
