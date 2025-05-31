import unittest

from src.htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
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