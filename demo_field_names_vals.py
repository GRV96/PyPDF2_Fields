"""
This demo of library PyPDF2_Fields extracts data from a PDF file's fields and
prints their name-value pairs in the console.
"""


from pathlib import Path
from PyPDF2 import PdfFileReader
from sys import argv

from PyPDF2_Fields import pdf_field_name_val_dict


pdf_file_path = Path(argv[1])

reader = PdfFileReader(pdf_file_path.open(mode="rb"), strict=False)

fields = reader.getFields()

field_names_vals = pdf_field_name_val_dict(fields, False)

for name, value in field_names_vals.items():
	print(f"{name}: {value}")
