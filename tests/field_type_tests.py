import pytest

from pathlib import Path
from PyPDF2 import PdfFileReader

from ..PyPDF2_Fields import\
	PdfFieldType,\
	get_field_type


_FIELDS_EMPTY_PATH = Path(__file__).parent.resolve()/"fields_empty.pdf"
_MODE_RB = "rb"


def field_type_test(field_name, expected_type):
	reader =\
		PdfFileReader(_FIELDS_EMPTY_PATH.open(mode=_MODE_RB), strict=False)
	fields = reader.getFields()
	tested_field = fields[field_name]

	assert get_field_type(tested_field) == expected_type


def test_inexistent_field_type():
	a_dict = {"/FT": "aucun"}
	assert get_field_type(a_dict) == PdfFieldType.NONE


def test_no_field_type_key():
	a_dict = {"x": "y"}
	assert get_field_type(a_dict) == PdfFieldType.NONE


def test_field_type_action_btn():
	field_type_test("Initialisation", PdfFieldType.ACTION_BTN)
	field_type_test("Valider-BAS", PdfFieldType.ACTION_BTN)
	field_type_test("Valider-HAUT", PdfFieldType.ACTION_BTN)


def test_field_type_checkbox():
	field_type_test("Boite3", PdfFieldType.CHECKBOX)


def test_field_type_radio_btn_group():
	field_type_test("Group1", PdfFieldType.RADIO_BTN_GROUP)


def test_field_type_text():
	field_type_test("Matricule", PdfFieldType.TEXT_FIELD)
