from enum import Enum


_FIELD_TYPE = "/FT"
_KEY_KIDS = "/Kids"
_KEY_TU = "/TU"
_TYPE_BUTTON = "/Btn"
_TYPE_TEXT = "/Tx"


class PdfFieldType(Enum):
	"""
	This enumeration represents the field types that a PDF file can contain.
	"""
	NONE = -1
	ACTION_BTN = 0
	CHECKBOX = 1
	RADIO_BTN_GROUP = 2
	TEXT_FIELD = 3


def get_field_type(pdf_field):
	"""
	Determines the type of the given PDF field: text field, checkbox or radio
	button group.

	Args:
		pdf_field (PyPDF2.generic.Field): a dictionary that represents a field
			of a PDF file. This argument can be a value of the dictionary
			returned by PdfFileReader's method getFields.

	Returns:
		PdfFieldType: the type of pdf_field. PdfFieldType.NONE indicates that
			no type was determined
	"""
	type_val = pdf_field.get(_FIELD_TYPE)

	if type_val == _TYPE_TEXT:
		return PdfFieldType.TEXT_FIELD

	elif type_val == _TYPE_BUTTON:
		if _KEY_KIDS in pdf_field:
			return PdfFieldType.RADIO_BTN_GROUP

		elif _KEY_TU in pdf_field:
			return PdfFieldType.ACTION_BTN

		else:
			return PdfFieldType.CHECKBOX

	else:
		return PdfFieldType.NONE
