from enum import Enum

class TextType(Enum):
    NORMAL = 'normal text'
    BOLD = 'bold text'
    ITALIC = 'italic text'
    CODE = 'code text'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.type == other.type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
    
