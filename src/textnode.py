from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = None
    BOLD = 'b'
    ITALIC = 'i'
    CODE = 'code'
    LINK = 'a'
    IMAGE = 'img'

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url
    
    def to_htmlnode(self):
        prop = None
        if self.type == TextType.LINK:
            prop = {'href':self.url}
        elif self.type == TextType.IMAGE:
            return LeafNode(self.type.value,'',{'src':self.url,'alt':self.text})    
        return LeafNode(self.type.value,self.text,prop)

    def __eq__(self, other):
        if self.text == other.text and self.type == other.type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
    
