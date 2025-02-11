import unittest

from helpers import *

class TestSplitInlineTextNode(unittest.TestCase):
    def test_mark_in_normal(self):
        enode = TextNode("*italic* text",TextType.NORMAL)
        elist = textnode_split_inline([enode],'*',TextType.ITALIC)
        self.assertEqual(str(elist),'[TextNode(italic, i, None), TextNode( text, None, None)]')
        txt = 'This is text with a **bolded phrase** in the middle'
        tnode = TextNode(txt,TextType.NORMAL)
        tlist = textnode_split_inline([tnode],'**',TextType.BOLD)
        self.assertEqual(str(tlist),'[TextNode(This is text with a , None, None), TextNode(bolded phrase, b, None), TextNode( in the middle, None, None)]')
    
    def test_normal_withoutmark(self):
        node = TextNode("normal",TextType.NORMAL)
        result = textnode_split_inline([node],'**',TextType.BOLD)
        self.assertEqual(result,[node])

    def test_mark_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.NORMAL)
        new_nodes = textnode_split_inline([node], "**", TextType.BOLD)
        anew_nodes = textnode_split_inline(new_nodes, "*", TextType.ITALIC)
        self.assertEqual(str(anew_nodes),'[TextNode(bold, b, None), TextNode( and , None, None), TextNode(italic, i, None)]')
    
    def test_multiple_bold(self):
        node = TextNode('normal **bold1** n2 ** bold2 with a space**',TextType.NORMAL)
        new_nodes = textnode_split_inline([node],'**',TextType.BOLD)
        self.assertEqual(str(new_nodes),'[TextNode(normal , None, None), TextNode(bold1, b, None), TextNode( n2 , None, None), TextNode( bold2 with a space, b, None)]')
        
    def tests_mark_bold_in_italic(self):
        pass

class TestExtractLinkAndImage(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_image(text),test)

    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_link(text),test)

class TestSplitImage(unittest.TestCase):
    def test_split_image(self):
        tnod = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.NORMAL)
        test = [TextNode("This is text with a link ",TextType.NORMAL), 
                TextNode("to boot dev", TextType.IMAGE, 'https://www.boot.dev'),
                TextNode(" and ", TextType.NORMAL),
                TextNode("to youtube", TextType.IMAGE,'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(split_imageOrlink_node([tnod],TextType.IMAGE),test)
    
    def test_split_link(self):
        tnod = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.NORMAL)
        test = [TextNode("This is text with a link ",TextType.NORMAL), 
                TextNode("to boot dev", TextType.LINK, 'https://www.boot.dev'),
                TextNode(" and ", TextType.NORMAL),
                TextNode("to youtube", TextType.LINK,'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(split_imageOrlink_node([tnod],TextType.LINK),test)
    
    def test_split_link_notimage(self):
        tnod = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.NORMAL)
        test = [TextNode("This is text with a link ",TextType.NORMAL), 
                TextNode("to boot dev", TextType.LINK, 'https://www.boot.dev'),
                TextNode(" and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL),]
        self.assertEqual(split_imageOrlink_node([tnod],TextType.LINK),test)

class TestTextToTextNode(unittest.TestCase):
    def test_text_multiple_types(self):
        txt = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = [TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),]
        self.assertEqual(text_to_textnode(txt),test)
    
class TestMarkDownToBlocks(unittest.TestCase):
    def test_txt_to_blocks(self):
        txt = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        correct = ["# This is a heading",
                   "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                   "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(markdown_to_blocks(txt),correct)
    
    def test_multiple_emptylines(self):
        txt = "\nblock1 line1\n\n\n\nblock2 line1\nline2\n\nblock3 line1\n\n\n\n\n\n\n\nblock4 line1\n"
        correct = ["block1 line1","block2 line1\nline2","block3 line1","block4 line1"]
        self.assertEqual(markdown_to_blocks(txt),correct)