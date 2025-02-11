from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'p'
    HEADING = 'h'
    CODE = 'pre'
    QUOTE = 'blockquote'
    UNORDERED_LIST = 'ul'
    ORDERED_LIST = 'ol'

def block_to_blocktype(block):
    if block[0:3] == block[-3:] == "```":
        return BlockType.CODE
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    lines = block.split('\n')
    quote = False
    for line in lines:
        if line[0] == '>':
            quote = True
            continue
        quote = False
        break
    if quote:
        return BlockType.QUOTE
    unordered = False
    for line in lines:
        if line.startswith(('* ','- ')):
            unordered = True
            continue
        unordered = False
        break
    if unordered:
        return BlockType.UNORDERED_LIST
    n = 1
    ordered = False
    for line in lines:
        if line.startswith(f"{n}. "):
            ordered = True
            n += 1
            continue
        ordered = False
        break
    if ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH





