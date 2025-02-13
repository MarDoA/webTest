

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ''
        result = ''
        for k,v in self.props.items():
            result += f' {k}="{v}"'
        return result
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value:
            return True
        return False
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,props=props)  
    
    def to_html(self):
        if self.value is None:
            raise ValueError('leaf must have a value')
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("must have children")
        children_string = ''
        for ch in self.children:
            children_string += ch.to_html() 
        return f'<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>'
    
