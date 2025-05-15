import os

from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating Page {from_path} to {dest_path} using {template_path}")

    # -- md
    with open(from_path, 'r') as fh:
        md = fh.read()
    
    # -- html templte
    with open(template_path, 'r') as fh:
        template = fh.read()
    
    # -- convert md to html
    content = markdown_to_html_node(md).to_html()

    # -- get title
    title = extract_title(md)

    # -- inject content and title into template file
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    
    # -- 
    Path(dest_path).parent.mkdir(exist_ok=True, parents=True)
    
    # -- 
    with open(dest_path, "w") as fh:
        fh.write(template)
    
    return None


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_pages_recursive(dir_path_content: str, template_path: str, dst_dir_path: str):
    contents = os.listdir(dir_path_content)

    os.makedirs(dst_dir_path, exist_ok=True)


    for item in contents:
        item_path = os.path.join(dir_path_content, item)

        if os.path.isfile(item_path) and item.endswith('.md'):
            dst_file = os.path.join(dst_dir_path, item.replace(".md", '.html'))
            generate_page(item_path, template_path, dst_file)

        elif os.path.isdir(item_path):
            new_dst_dir = os.path.join(dst_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dst_dir)
