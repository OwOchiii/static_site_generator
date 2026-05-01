from block import markdown_to_html_node
from extract_markdown import extract_title
from pathlib import Path

def generate_page(from_path, template_path, to_path, basepath):
    print(f"Generating page from '{from_path}' to '{to_path}' using '{template_path}'")
    from_path = Path(from_path)
    template_path = Path(template_path)
    to_path = Path(to_path)
    markdown = from_path.open("r").read()
    template = template_path.open("r").read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_string = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    html_string = html_string.replace('href="/', f'href="{basepath}')
    html_string = html_string.replace('src="/', f'src="{basepath}')
    to_path.open("w").write(html_string)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_path_content = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)
    dest_dir_path.mkdir(parents=True, exist_ok=True)
    for filename in dir_path_content.iterdir():
        if filename.is_file() and filename.suffix == ".md":
            from_path = filename
            to_path = dest_dir_path / filename.with_suffix(".html").name
            generate_page(from_path, template_path, to_path, basepath)
        elif filename.is_dir():
            generate_pages_recursive(filename, template_path, dest_dir_path / filename.name, basepath)
