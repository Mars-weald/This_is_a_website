import os, shutil, sys

from blocks import *

if len(sys.argv) >= 2:
    basepath = sys.argv[1]
else:
    basepath = "/"

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("public")
    os.mkdir("docs")
    file_copier("static", "public")
    generate_pages_recursive("content", "template.html", "docs", basepath)

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for thing in os.listdir(dir_path_content):
        if os.path.isdir(os.path.join(dir_path_content, thing)):
            os.mkdir(os.path.join(dest_dir_path, thing))
            generate_pages_recursive(os.path.join(dir_path_content, thing), template_path, os.path.join(dest_dir_path, thing), basepath)
        elif os.path.isfile(os.path.join(dir_path_content, thing)):
            if thing.endswith(".md"):
                base = open(os.path.join(dir_path_content, thing), "r")
                base_md = base.read()
                base.close()

                templater = open(template_path)
                template = templater.read()
                templater.close()  

                node = markdown_to_html_node(base_md)
                html = node.to_html()
                title = extract_title(base_md)
                template = template.replace("{{ Title }}", title)
                template = template.replace("{{ Content }}", html)
                template = template.replace('href="/', f'href="{basepath}')
                template = template.replace('src="/', f'src="{basepath}')
                name = os.path.join(dest_dir_path, thing)[:-3] + ".html"
                with open(name, "w") as page:
                    page.write(template)
            else:
                continue
        

if __name__ == "__main__":
    main()
