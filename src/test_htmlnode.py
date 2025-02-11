import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

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
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, 'sup')
        self.assertEqual(node.to_html(),'sup')

    def test_parentnode(self):
        node = ParentNode('p',[LeafNode('b','bold'),LeafNode(None,'normal')])
        self.assertEqual(node.to_html(),'<p><b>bold</b>normal</p>')
        node2 = ParentNode('s',[LeafNode('p','pol')],{'hi':'eng','yola':'span'})
        self.assertEqual(node2.to_html(),'<s hi="eng" yola="span"><p>pol</p></s>')
        pnode = ParentNode('bp',[node,node2])
        self.assertEqual(pnode.to_html(),'<bp><p><b>bold</b>normal</p><s hi="eng" yola="span"><p>pol</p></s></bp>')