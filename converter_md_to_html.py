import sys
import os
import markdown
from bs4 import BeautifulSoup

def convert_markdown_to_html(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Convert Markdown to HTML with correct extensions
    html_content = markdown.markdown(
        content,
        extensions=[
            "fenced_code",
            "tables",
            "mdx_math",     # For LaTeX equations
            "mermaid",      # Correct extension name for Mermaid.js
            "attr_list"     # Required for some extensions
        ]
    )
    return html_content

def inject_into_template(html_content, template_file, output_file):
    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()
    
    soup = BeautifulSoup(template, "html.parser")
    container = soup.find("div", class_="container")
    if container:
        container.clear()
        container.append(BeautifulSoup(html_content, "html.parser"))
    
    # Ensure Mermaid.js is initialized
    if not soup.find("script", string=lambda t: "mermaid.initialize" in str(t)):
        mermaid_script = soup.new_tag("script")
        mermaid_script.string = "mermaid.initialize({ startOnLoad: true });"
        soup.body.append(mermaid_script)
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(soup))

def main(markdown_file, output_file):
    html_content = convert_markdown_to_html(markdown_file)
    inject_into_template(html_content, "template.html", output_file)
    print(f"Converted {markdown_file} to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter_md_to_html.py <input.md> <output.html>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)
    
    main(input_file, output_file)