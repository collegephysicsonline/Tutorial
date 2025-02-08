import sys
import os
import markdown
from bs4 import BeautifulSoup
import re

# Function to convert Markdown to HTML
def convert_markdown_to_html(markdown_file):
    # Read the Markdown file
    with open(markdown_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(
        markdown_content,
        extensions=[
            "fenced_code",  # Support for code blocks
            "tables",       # Support for tables
            "toc",          # Table of contents
        ],
    )

    # Ensure proper wrapping of math expressions for MathJax
    #html_content = re.sub(r"(?<!\\)\$\$([^$]+?)\$\$", r"\\\[\1\\\]", html_content)  # Block math
    #html_content = re.sub(r"(?<!\\)\$([^$]+?)\$", r"\\\(\1\\\)", html_content)  # Inline math
    # Ensure proper escaping of backslashes for MathJax
    html_content = re.sub(r"\$`([^`]+?)`\$", r"\\[\1\\]", html_content)  # Inline math with $` `$
    #html_content = re.sub(r"(?<!\\)\\\[([^\\]+?)\\\]", r"\\\[\1\\\]", html_content)  # Block math with \[ \]
    # Ensure MathJax script is included for LaTeX rendering
    mathjax_script = '''<script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js">
    </script>'''

    # Wrap the content for better rendering
    wrapper_div = f'<div class="arithmatex">{html_content}</div>'
    final_content = mathjax_script + wrapper_div

    return final_content

# Function to inject HTML content into the template
def inject_into_template(html_content, template_file, output_file):
    # Read the template file
    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()

    # Use BeautifulSoup to inject the HTML content into the template
    soup = BeautifulSoup(template, "html.parser")

    # Find the container where the content should be injected
    container = soup.find("div", {"class": "container"})
    if container:
        # Replace the container's content with the converted HTML
        container.clear()
        container.append(BeautifulSoup(html_content, "html.parser"))

    # Ensure the style.css is linked correctly
    style_link = soup.find("link", {"href": "style.css"})
    if not style_link:
        # If the link to style.css is missing, add it
        style_tag = soup.new_tag("link", rel="stylesheet", href="style.css")
        soup.head.append(style_tag)

    # Write the final HTML to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(soup))

# Main function
def main(markdown_file, output_file):
    # Convert Markdown to HTML
    html_content = convert_markdown_to_html(markdown_file)

    # Inject the HTML content into the template
    template_file = "template.html"
    inject_into_template(html_content, template_file, output_file)

    print(f"Successfully converted {markdown_file} to {output_file}")

# Run the script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python markdown_to_html.py <markdown_file.md> <output_file.html>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Error: File {markdown_file} does not exist.")
        sys.exit(1)

    main(markdown_file, output_file)
