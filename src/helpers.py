import re
from textnode import TextNode,TextType
from blocktype import *
from htmlnode import *

def extract_link(txt):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",txt)

def extract_image(txt):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",txt)

def textnode_split_inline(nodes,mark,type):
    new_nodes = []
    for node in nodes:
        lis = node.text.split(mark)
        if len(lis)%2 ==0:
            raise Exception("missing ending mark")
        for i in range(len(lis)):
            if lis[i] == '':continue
            if i%2:
                new_nodes.append(TextNode(lis[i],type))
            else:
                new_nodes.append(TextNode(lis[i],node.type))
    return new_nodes

def split_imageOrlink_node(nodes, type):
    n_nod = []
    mark = ''
    extract_func = extract_link
    if type == TextType.IMAGE:
        extract_func = extract_image
        mark = '!'
    for node in nodes:
        imgs = extract_func(node.text)
        if len(imgs) <=0:
            n_nod.append(node)
            continue
        line = node.text
        for im in imgs:
            lis = line.split(f'{mark}[{im[0]}]({im[1]})',1)
            if len(lis) != 2: raise Exception("invalid or image not closed")
            line = lis[1]
            if lis[0] != '':
                n_nod.append(TextNode(lis[0],node.type))
            n_nod.append(TextNode(im[0],type,im[1]))
        if line != '':
            n_nod.append(TextNode(line,node.type))
    return n_nod

def text_to_textnode(txt):
    begin = TextNode(txt, TextType.NORMAL)
    nafterb = textnode_split_inline([begin],"**",TextType.BOLD)
    nafteri = textnode_split_inline(nafterb,"*",TextType.ITALIC)
    nafterc = textnode_split_inline(nafteri,"`",TextType.CODE)
    nafterlink = split_imageOrlink_node(nafterc,TextType.LINK)
    nafterimg = split_imageOrlink_node(nafterlink,TextType.IMAGE)
    return nafterimg

def markdown_to_blocks(txt):
    lines = txt.split('\n')
    lines.append('')
    blocks = []
    block = ''
    for line in lines:
        if line == '':
            if block != '':
                blocks.append(block)
                block = ''
            continue
        if block != '':
            block += '\n'
        block += line
    return blocks

def txt_to_children(txt):
    nodes = text_to_textnode(txt)
    children = []
    for node in nodes:
        children.append(node.to_htmlnode())
    return children

def block_to_htmlnode(block,type):
    new_txt = block
    tag = type.value
    if type == BlockType.CODE:
        new_txt = block[3:-3].strip()
        inside = ParentNode('code',txt_to_children(new_txt))
        return ParentNode('pre',[inside])
    
    elif type == BlockType.HEADING:
        n = len(block)-len(block.lstrip('#'))
        tag = f'h{n}'
        new_txt = block[n+1:]

    elif type == BlockType.ORDERED_LIST or type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        list_items = []
        for line in lines:
            li_children = txt_to_children(line.split(" ",1)[1])
            list_items.append(ParentNode('li',li_children))
        return ParentNode(tag,list_items)

    elif type == BlockType.QUOTE:
        lines = block.split("\n")
        new_txt ="\n".join(list(map(lambda x: x[1:],lines))) 
    children = txt_to_children(new_txt)
    return ParentNode(tag,children)


def markdown_to_html(txt):
    blocks = markdown_to_blocks(txt)
    htmlnodes = []
    for block in blocks:
        btype = block_to_blocktype(block)
        htmlnodes.append(block_to_htmlnode(block, btype))
    return ParentNode('div', htmlnodes)
