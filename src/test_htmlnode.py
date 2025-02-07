import unittest

from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_probs(self):
        node = HTMLNode('','',None,{'href':'ds'})
        self.assertEqual(node.props_to_html(), ' href="ds"')
        node2 = HTMLNode('','',None,{'href':'ds','popo':'pepe'})
        self.assertEqual(node2.props_to_html(), ' href="ds" popo="pepe"')
    
    def test_values(self):
        node = HTMLNode('hi','greet',None,None)
        self.assertEqual(node.tag,'hi')
        self.assertEqual(node.value,'greet')
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,None)
    
    def test_repr(self):
        node = HTMLNode('div','page',None,{'pro':'p'})
        self.assertEqual(node.__repr__(),"HTMLNode(div, page, children: None, {'pro': 'p'})")

    def test_to_html(self):
        node = LeafNode('p','sup',{'hi':'g.co'})
        self.assertEqual(node.to_html(),'<p hi="g.co">sup</p>')
        node2 = LeafNode('p', 'sup')
        self.assertEqual(node2.to_html(),'<p>sup</p>')