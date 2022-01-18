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
