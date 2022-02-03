"""
This demo of library PyPDF2_Fields extracts data from a PDF file's fields and
prints their name-value pairs in the console.
"""


from argparse import ArgumentParser
from pathlib import Path
from PyPDF2 import PdfFileReader
from sys import argv

from PyPDF2_Fields import pdf_field_name_val_dict


parser = ArgumentParser(description=__doc__)

parser.add_argument("-f", "--file", type=Path,
	help="the path to the file whose fields will be printed")

parser.add_argument("-e", "--empty", action="store_true",
	help="print the empty fields.")

args = parser.parse_args()
pdf_file_path = args.file
filter_none = not args.empty

reader = PdfFileReader(pdf_file_path.open(mode="rb"), strict=False)

fields = reader.getFields()

field_names_vals = pdf_field_name_val_dict(fields, filter_none)

for name, value in field_names_vals.items():
	print(f"{name}: {value}")
