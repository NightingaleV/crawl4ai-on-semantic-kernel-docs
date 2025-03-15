"""In this script"""

import fitz  # PyMuPDF
import html2text


def pdf_to_markdown(pdf_path, output_md):
    doc = fitz.open(pdf_path)
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # Keep links
    converter.bypass_tables = False  # Convert tables if present

    markdown_text = ""

    for page in doc:
        html = page.get_text("html")
        md_page = converter.handle(html)
        markdown_text += md_page + "\n\n"

    with open(output_md, "w", encoding="utf-8") as f:
        f.write(markdown_text)


if __name__ == "__main__":
    pdf_file = "python-api-semantic_kernel_py_toc-semantic-kernel-python.pdf"
    output_file = "./data/api/api_docs.md"
    pdf_to_markdown(pdf_file, output_file)
