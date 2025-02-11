import unittest

from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_block_to_blocktype(self):
        txt = "# This is a heading"
        txt1 = "### heading with 3"
        txt3 = "###### "
        self.assertEqual(block_to_blocktype(txt),BlockType.HEADING)
        self.assertEqual(block_to_blocktype(txt1),BlockType.HEADING)
        self.assertEqual(block_to_blocktype(txt3),BlockType.HEADING)
        ordered = "1. frgr\n2. gtg\n3. gtg"
        self.assertEqual(block_to_blocktype(ordered),BlockType.ORDERED_LIST)
        unordered = "* grgt\n* hhyh\n- gtgt\n* hyh"
        self.assertEqual(block_to_blocktype(unordered),BlockType.UNORDERED_LIST)
        cod = "```gtgt\ngtgt\ngt\n\n```"
        self.assertEqual(block_to_blocktype(cod),BlockType.CODE)
        quot = ">gtg\n>gtgt\n>gt\n>"
        self.assertEqual(block_to_blocktype(quot),BlockType.QUOTE)
        
        
