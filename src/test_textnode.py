import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('a text node', TextType.BOLD)
        node2 = TextNode('a text node', TextType.BOLD)
        self.assertEqual(node,node2)
    def test_not_eq_type(self):
        node = TextNode('text node', TextType.BOLD)
        node2 = TextNode('text node',TextType.ITALIC)
        self.assertNotEqual(node,node2)
    def test_not_eq_text(self):
        node3 = TextNode('text node 1', TextType.BOLD)
        node4 = TextNode('text node 2', TextType.BOLD)
        self.assertNotEqual(node3,node4)
    def test_not_eq_url(self):
        node5 = TextNode('text node', TextType.BOLD,'https://www.boot.dev')
        node6 = TextNode('text node', TextType.BOLD,'https://www.github.com')
        self.assertNotEqual(node5,node6)
    def test_not_eq_url2(self):
        node = TextNode('text node', TextType.BOLD)
        node2 = TextNode('text node', TextType.BOLD,'https://www.boot.dev')
        self.assertNotEqual(node,node2)    

if __name__ == "__main__":
    unittest.main()