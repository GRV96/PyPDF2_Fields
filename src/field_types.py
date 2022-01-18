from enum import Enum


_FIELD_TYPE = "/FT"
_KEY_KIDS = "/Kids"
_TYPE_BUTTON = "/Btn"
_TYPE_TEXT = "/Tx"


class PdfFieldType(Enum):
	"""
	This enumeration represents the field types that a PDF file can contain.
	"""
	TEXT_FIELD = 0
	CHECKBOX = 1
	RADIO_BTN_GROUP = 2


def get_field_type(pdf_field):
	"""
	Determines the type of the given PDF field: text field, checkbox or radio
	button group.

	Args:
		pdf_field (dict): a dictionary that represents a field of a PDF file.
			This argument can be a value of the dictionary returned by
			PdfFileReader's method getFields.

	Returns:
		PdfFieldType: the type of pdf_field or None if no type is determined
	"""
	type_val = pdf_field.get(_FIELD_TYPE)

	if type_val == _TYPE_TEXT:
		return PdfFieldType.TEXT_FIELD

	elif type_val == _TYPE_BUTTON:
		if _KEY_KIDS in pdf_field:
			return PdfFieldType.RADIO_BTN_GROUP

		else:
			return PdfFieldType.CHECKBOX

	else:
		return None
