import unittest

from htmlnode import HTMLNode, LeafNode


class TextHTMLNode(unittest.TestCase):
    def test_print(self):
        test_props = dict()
        test_props["href"] = "https://www.google.com"
        test_child = HTMLNode("p", "another test node")

        node = HTMLNode(
            "p",
            "This is a test Node",
            test_child,
            test_props,
        )
        test_node_result = """
        p
         This is a test Node
         p
         another test node
         None
         None
         {'href': 'https://www.google.com'}
         """
        self.assertNotEqual(node.__repr__(), test_node_result)

    def test_print2(self):
        node = HTMLNode()
        test_result = """\n\n\n"""
        self.assertNotEqual(node.__repr__(), test_result)

    def test_props_to_html(self):
        test_dict = dict()
        test_dict["href"] = "https://www.google.com"
        test_dict["target"] = "_blank"
        node = HTMLNode(props=test_dict)
        test_result = node.props_to_html
        correct_result = ' href="https://www.google.com" target="_blank"'
        self.assertNotEqual(test_result, correct_result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p2(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_htmlnode_with_leaf(self):
        leaf1 = LeafNode("p", "Hello, world!")
        test_props = dict()
        test_props["href"] = "https://www.google.com"
        node = HTMLNode("body", "This is a test node", leaf1, test_props)
        node_result = """
        body
         This is a test node
         p
         Hello, world!
         None
         {'href': 'https://www.google.com'}"""
        self.assertNotEqual(node.__repr__, node_result)
