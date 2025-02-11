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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        tnode = TextNode('txt node',TextType.NORMAL)
        html = tnode.to_htmlnode()
        self.assertEqual(html.tag,None)
        self.assertEqual(html.value,'txt node')
        self.assertEqual(html.props,None)
    def test_img(self):
        tnode = TextNode('alt txt',TextType.IMAGE,'rs.png')
        html = tnode.to_htmlnode()
        self.assertEqual(html.tag,'img')
        self.assertEqual(html.value,'')
        self.assertEqual(html.props,{'src':'rs.png','alt':'alt txt'})
    def test_bold(self):
        tnode = TextNode('bold',TextType.BOLD)
        html = tnode.to_htmlnode()
        self.assertEqual(html.tag,'b')
        self.assertEqual(html.value,'bold')
        self.assertEqual(html.props,None)
    

if __name__ == "__main__":
    unittest.main()
    