import fitz
import os

DPI = 300
PDF_DIRECTORY = f"{os.getcwd()}/label-studio/pdfs"
IMAGE_DIRECTORY = f"{os.getcwd()}/label-studio/images"

zoom = DPI / 72
magnify = fitz.Matrix(zoom, zoom)

pdfs = os.listdir(PDF_DIRECTORY)

for pdf in pdfs:
    doc = fitz.open(f'{PDF_DIRECTORY}/{pdf}')

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=magnify)
        pix.save(f"{IMAGE_DIRECTORY}/{pdf.split('.pdf')[0]}_{i}.png")
