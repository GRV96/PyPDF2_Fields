import pytest

from pathlib import Path
from PyPDF2 import PdfFileReader

from ..src import\
	PdfFieldType,\
	get_field_type


_FIELDS_EMPTY_PATH = Path(__file__).parent/"fields_empty.pdf"
_MODE_RB = "rb"


def field_type_test(field_name, expected_type):
	reader =\
		PdfFileReader(_FIELDS_EMPTY_PATH.open(mode=_MODE_RB), strict=False)
	fields = reader.getFields()
	tested_field = fields[field_name]

	assert get_field_type(tested_field) == expected_type


def test_field_type_text():
	field_type_test("Matricule", PdfFieldType.TEXT_FIELD)


def test_field_type_checkbox():
	field_type_test("Boite3", PdfFieldType.CHECKBOX)


def test_field_type_radio_btn_group():
	field_type_test("Group1", PdfFieldType.RADIO_BTN_GROUP)
