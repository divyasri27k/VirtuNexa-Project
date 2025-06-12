from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_pdf, output_dir):
    reader = PdfReader(input_pdf)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        with open(os.path.join(output_dir, f"page_{i+1}.pdf"), "wb") as f:
            writer.write(f)