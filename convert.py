import markdown
import argparse

def convert_markdown_to_html(input_file, output_file):
    # Read the Markdown file
    with open(input_file, "r", encoding="utf-8") as file:
        markdown_text = file.read()

    # Configure Markdown with the arithmatex extension
    md = markdown.Markdown(
        extensions=[
            "pymdownx.arithmatex",  # Enable LaTeX math support
            "extra",                # Other Markdown extensions
        ],
        extension_configs={
            "pymdownx.arithmatex": {
                "generic": True,  # Use generic LaTeX delimiters (\[ ... \], \( ... \))
            }
        }
    )

    # Convert Markdown to HTML
    html_content = md.convert(markdown_text)

    # Add MathJax script and wrap in HTML structure
    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Document</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Write the HTML file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_output)

    print(f"HTML file '{output_file}' generated with MathJax!")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML with MathJax support.")
    parser.add_argument("input_file", help="Path to the input Markdown file")
    parser.add_argument("output_file", help="Path to the output HTML file")

    # Parse arguments
    args = parser.parse_args()

    # Call the conversion function
    convert_markdown_to_html(args.input_file, args.output_file)