from textnode import *
from helpers import *
from blocktype import *
from htmlnode import *
import os
import shutil

def main():
    publicPath = os.path.abspath("./public/")
    staticPath = os.path.abspath("./static/")
    copy_from_static(staticPath,publicPath)
    #shutil.rmtree(publicPath)
    templatePath = os.path.abspath("./template.html")
    markdownPath = os.path.abspath("./content/")
    destinationPath = os.path.abspath("./public/")
    generatePages_recur(markdownPath,templatePath,destinationPath)
    #generatePage(markdownPath,templatePath,destinationPath)



def copy_from_static(pfrom,pto):
    if os.path.exists(pto):
        shutil.rmtree(pto)
    shutil.copytree(pfrom,pto)

def generatePage(fro, temp, dst):
    print(f"Generating page from {fro} to {dst} using {temp}")
    mark_txt = ''
    template = ''
    with open(fro,'r') as file:
        mark_txt = file.read()
    with open(temp,'r') as file:
        template = file.read()
    html_string = markdown_to_html(mark_txt).to_html()
    title = extract_title(mark_txt)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",html_string)
    with open(dst+'/index.html', 'w') as file:
        file.write(template)

def generatePages_recur(contentPath, templatePath, dstPath):
    content = os.listdir(contentPath)
    for c in content:
        cpath = os.path.abspath(contentPath+'/'+c)
        if os.path.isfile(cpath):
            generatePage(cpath,templatePath,dstPath)
        else:
            path = os.path.join(dstPath, c)
            os.mkdir(path)
            generatePages_recur(cpath,templatePath,path)

def extract_title(markdown):
    blocks = markdown.split('\n')
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
    raise Exception("missing title")

main()