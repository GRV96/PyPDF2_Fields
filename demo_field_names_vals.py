"""
This demo of library PyPDF2_Fields prints the name, type and value of a PDF
file's fields in the console.
"""


from argparse import ArgumentParser
from pathlib import Path
from PyPDF2 import PdfFileReader

from PyPDF2_Fields import\
	PdfFieldType,\
	get_field_type,\
	pair_fields_name_and_val


def field_type_to_str(field_type):
	if field_type == PdfFieldType.NONE:
		return "none"

	elif field_type == PdfFieldType.OTHER:
		return "other"

	elif field_type == PdfFieldType.ACTION_BTN:
		return "action btn"

	elif field_type == PdfFieldType.CHECKBOX:
		return "checkbox"

	elif field_type == PdfFieldType.RADIO_BTN_GROUP:
		return "radio btn group"

	elif field_type == PdfFieldType.TEXT_FIELD:
		return "text"


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

field_names_vals = pair_fields_name_and_val(fields, filter_none)

for name, value in field_names_vals.items():
	field = fields[name]
	field_type = get_field_type(field)
	type_str = field_type_to_str(field_type)
	print(f"{name} ({type_str}): {value}")
