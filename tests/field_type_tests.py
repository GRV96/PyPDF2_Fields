from dataclasses import field
from email.policy import strict
import pytest

from pathlib import Path
from PyPDF2 import PdfFileReader

from ..src import\
	PdfFieldType,\
	get_field_type

_FIELDS_EMPTY_PATH = Path(__file__).parent/"fields_empty.pdf"


def test_field_type_text():
	reader =\
		PdfFileReader(_FIELDS_EMPTY_PATH.open(mode="rb"), strict=False)
	fields = reader.getFields()
	field_matricule = fields["Matricule"]

	assert get_field_type(field_matricule) == PdfFieldType.TEXT_FIELD


def test_field_type_checkbox():
	reader =\
		PdfFileReader(_FIELDS_EMPTY_PATH.open(mode="rb"), strict=False)
	fields = reader.getFields()
	field_boite3 = fields["Boite3"]

	assert get_field_type(field_boite3) == PdfFieldType.CHECKBOX


def test_field_type_radio_btn_group():
	reader =\
		PdfFileReader(_FIELDS_EMPTY_PATH.open(mode="rb"), strict=False)
	fields = reader.getFields()
	field_group1 = fields["Group1"]

	assert get_field_type(field_group1) == PdfFieldType.RADIO_BTN_GROUP
