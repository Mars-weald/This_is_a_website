from enum import Enum
from inline import *
from textnode import text_node_to_html_node
from htmlnode import *

def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        clean = block.strip()
        result.append(clean)
    return result

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block[0:3] and block[len(block) - 3:len(block)] == "```":
        return BlockType.CODE
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("-"):
        for line in lines:
            if not line.startswith("-"):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1."):
        n = 1
        for line in lines:
            if not line.startswith(f"{n}. "):
                return BlockType.PARAGRAPH
            n += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    

def markdown_to_html_node(markdown):
    hey_kid = []
    markdown = markdown_to_blocks(markdown)
    for block in markdown:
        tipe = block_to_block_type(block)
        if tipe == BlockType.PARAGRAPH:
            texto = block.strip("\n")
            texto = " ".join(texto.splitlines())
            children = text_to_children(texto)
            hey_kid.append(ParentNode("p", children))
        elif tipe == BlockType.CODE:
            lines = block.split("\n")
            block = "\n".join(lines[1:-1]) +"\n"
            new_node = LeafNode("code", block)
            hey_kid.append(ParentNode("pre", [new_node], props=None))
        elif tipe == BlockType.QUOTE:
            clean = []
            lines = block.split("\n")
            for line in lines:
                line = line.lstrip("> ")
                clean.append(line)
            texto = "\n".join(clean)
            children = text_to_children(texto)
            hey_kid.append(ParentNode("blockquote", children))
        elif tipe == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            children = []
            for line in lines:
                line = line.lstrip("-")
                line = line.strip()
                kids = text_to_children(line)
                children.append(ParentNode("li", kids))
            hey_kid.append(ParentNode("ul", children))
        elif tipe == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            children = []
            for line in lines:
                line = line[3:]
                children.append(LeafNode("li", line))
            hey_kid.append(ParentNode("ol", children))
        elif tipe == BlockType.HEADING:
            tags = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "}
            for tag in tags:
                if block.startswith(tags[tag]):
                    texto = block.lstrip(tags[tag])
                    children = text_to_children(texto)
                    hey_kid.append(ParentNode(tag, children))

    return ParentNode("div", children=hey_kid)


def text_to_children(text):
    textnodes = list(text_to_textnodes(text))
    children = []
    for node in textnodes:
        kid = text_node_to_html_node(node)
        children.append(kid)
    return children