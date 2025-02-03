import markdown
from markdown_katex.extension import KaTeXExtension
import sys

def convert_markdown_to_html(input_file, output_file):
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convert markdown to HTML with KaTeX extension for LaTeX math
    html = markdown.markdown(text, extensions=[KaTeXExtension()])

    # Write the HTML to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Conversion complete. The HTML file is saved as '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python try.py <input_markdown_file> <output_html_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)