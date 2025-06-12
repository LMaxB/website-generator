import unittest

from src.htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_none(self):
        html = HTMLNode()
        html2 = HTMLNode(None, None, None, None)
        self.assertEqual(html, html2)

    def test_diff_props(self):
        html = HTMLNode(tag="a", value="game link", children=[], props ={"href": "runescape.com"})
        html2 = HTMLNode(tag="a", value="game link", children=[], props ={"href": "ff14.com"})
        self.assertNotEqual(html, html2)

    def test_props_to_html_varied_types(self):
        node = HTMLNode(props={"a": None, "b": 123})
        result = node.props_to_html()
        self.assertIn('a="None"', result)
        self.assertIn('b="123"', result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
