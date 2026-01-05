import os, shutil

from blocks import *

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    file_copier("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

def file_copier(path, destination):
    for thing in os.listdir(path):
        if os.path.isfile(os.path.join(path, thing)):
            shutil.copy(os.path.join(path, thing), destination)
        elif os.path.isdir(os.path.join(path, thing)):
            os.mkdir(f"{destination}/{thing}")
            file_copier(os.path.join(path, thing), os.path.join(destination, thing))

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            heading1 = line
            heading1 = heading1.lstrip("# ")
            return heading1.strip()
    raise Exception("No title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path form {from_path} to {dest_path} using {template_path}")
    start = open(from_path, "r")
    start_md = start.read()
    start.close()

    templater = open(template_path)
    template = templater.read()
    templater.close()

    node = markdown_to_html_node(start_md)
    html = node.to_html()
    title = extract_title(start_md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    with open(dest_path, "w") as page:
        page.write(template)
    

        

if __name__ == "__main__":
    main()
