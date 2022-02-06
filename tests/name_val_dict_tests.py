import pytest

from pathlib import Path
from PyPDF2 import PdfFileReader

from ..PyPDF2_Fields import\
	make_writer_from_reader,\
	pdf_field_name_val_dict,\
	RadioBtnGroup,\
	set_need_appearances,\
	update_page_fields


_FIELDS_EMPTY_PATH = Path(__file__).parent.resolve()/"fields_empty.pdf"
_TEST_FILE_NAME = "name_val_test_file.pdf"

_MODE_RB = "rb"
_MODE_WB = "wb"

# Group4 does not cause problems in the demo, but here, it contains a
# strange binary string. It is ignored in the tests for this reason.

# The value of these fields is calculated automatically
# if and only if the test file is filled manually.
# "Réclamation$", "TotalMontant", "TotalccMontant$"

_EXPECTED_VALUES = {
	"Détails4": "Dépense 4",
	"Réclamation$": 0,
	"Montant$7": 7,
	"Group1": "/Choix1",
	#"Group4": "/Ch#E8que",
	"Boite1": "/Oui",
	"Boite3": "/Non",
	"Date": "2022-02-03",
	"Province": "Québec",
	"NomSupHiérarchique": "Guyllaume Rousseau",
	"TotalMontant": 0,
	"TotalccMontant$": 0,
	"libelSiEtudiant":\
		"Inscrire adresse et courriel si le demandeur est un(e) étudiant(e) :"
}


def _field_content_test(test_dir_path, ignore_none):
	reader = _make_test_file_and_reader(test_dir_path)
	fields = reader.getFields()
	field_names_vals = pdf_field_name_val_dict(fields, ignore_none)

	expected_names = list(_EXPECTED_VALUES.keys())
	expected_names.sort()

	actual_names = list(field_names_vals.keys())
	actual_names.sort()

	if ignore_none:
		assert actual_names == expected_names

	else:
		for name in expected_names:
			assert name in actual_names

	for field_value in expected_names:
		actual_value = field_names_vals.get(field_value)
		expected_value = _EXPECTED_VALUES.get(field_value)
		assert str(actual_value) == str(expected_value)
		del field_names_vals[field_value]

	if ignore_none:
		assert len(field_names_vals) == 0

	else:
		for field_value in field_names_vals.values():
			assert field_value is None


def _make_reader_for_template():
	return PdfFileReader(_FIELDS_EMPTY_PATH.open(mode=_MODE_RB), strict=False)


def _make_reader_for_test_file(test_file_path):
	return PdfFileReader(test_file_path.open(mode=_MODE_RB), strict=False)


def _make_test_file_and_reader(test_dir_path):
	template_reader = _make_reader_for_template()
	writer = make_writer_from_reader(template_reader, False)

	field_content = {
		"Détails4": "Dépense 4",
		"Montant$7": 7,
		"Group1": 0,
		#"Group4": 1,
		# "Yes" in French. Makes the box checked.
		"Boite1": "/Oui",
		# "No" in French. Makes the box unchecked. Optional.
		"Boite3": "/Non",
		"Date": "2022-02-03",
		"Province": "Québec",
		"NomSupHiérarchique": "Guyllaume Rousseau"
	}

	radio_btn_group1 = RadioBtnGroup(
		"Group1", "/Choix1", "/Choix2")
	radio_btn_group2 = RadioBtnGroup(
		"Group2", "/Choix1", "/Choix2")
	radio_btn_group4 = RadioBtnGroup(
		"Group4", "/Dépôt", "/Chèque")

	update_page_fields(writer.getPage(0), field_content,
		radio_btn_group1, radio_btn_group2, radio_btn_group4)

	set_need_appearances(writer, True)

	test_file_path = test_dir_path/_TEST_FILE_NAME
	writer.write(test_file_path.open(mode=_MODE_WB))

	return _make_reader_for_test_file(test_file_path)


def test_name_val_dict_dont_filter_none(tmp_path):
	_field_content_test(tmp_path, False)


def test_name_val_dict_filter_none(tmp_path):
	_field_content_test(tmp_path, True)
