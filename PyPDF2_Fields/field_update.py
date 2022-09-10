from PyPDF2.generic import\
	NameObject,\
	TextStringObject

from .field_types import\
	PdfFieldType,\
	get_field_type


_KEY_ANNOTS = "/Annots"
_KEY_AS = "/AS"
_KEY_KIDS = "/Kids"
_KEY_PARENT = "/Parent"
_KEY_T = "/T"
_KEY_V = "/V"


def _make_radio_btn_group_dict(radio_btn_groups):
	"""
	Creates a dictionary that associates each given radio button group with
	its name. The name is a property of class RadioBtnGroup.

	Args:
		radio_btn_groups: a list, set or tuple that contains instances of
			RadioBtnGroup

	Returns:
		dict: Its keys are the groups' names; its values are the groups.
	"""
	btn_groups = dict()

	for group in radio_btn_groups:
		btn_groups[group.name] = group

	return btn_groups


def update_page_fields(page, field_content, *radio_btn_groups):
	"""
	Sets the fields in the given PdfFileWriter page to the values contained in
	argument field_content. Every key in this dictionary must be the name of a
	field in page. Text fields can be set to any object, which will be
	converted to a string. Checkboxes must be set to a string that represents
	their checked or unchecked state. For a radio button group, the value must
	be the index of the selected button. The index must correspond to a button
	name contained in the RadioBtnGroup instance in argument *radio_btn_groups
	that bears the group's name. This function ignores fields of type action
	button.

	Args:
		page (PyPDF2.pdf.PageObject): a page from a PdfFileWriter instance
		field_content (dict): Its keys are field names; its values are the data
			to put in the fields.
		*radio_btn_groups: RadioBtnGroup instances that represent the radio
			button groups in page. This argument is optional if no radio button
			group is being set.

	Raises:
		IndexError: if argument field_content sets a radio button group to an
			incorrect index
	"""
	# This function is based on PdfFileWriter.updatePageFormFieldValues and an answer to this question:
	# https://stackoverflow.com/questions/35538851/how-to-check-uncheck-checkboxes-in-a-pdf-with-python-preferably-pypdf2
	if len(radio_btn_groups) > 0:
		radio_buttons = True
		btn_group_dict = _make_radio_btn_group_dict(radio_btn_groups)

	else:
		radio_buttons = False

	page_annots = page[_KEY_ANNOTS]

	for writer_annot in page_annots:
		writer_annot = writer_annot.getObject()
		annot_name = writer_annot.get(_KEY_T)
		field_type = get_field_type(writer_annot)

		if annot_name in field_content:
			field_value = field_content[annot_name]
			_update_text_field_or_checkbox(
				writer_annot, field_value, field_type)

		elif radio_buttons and annot_name is None:
			_update_radio_btn_group(
				writer_annot, field_content, btn_group_dict)


def _update_radio_btn_group(writer_annot, field_content, btn_group_dict):
	annot_parent = writer_annot.get(_KEY_PARENT).getObject()

	if annot_parent is not None:
		annot_parent_name = annot_parent.get(_KEY_T).getObject()
		annot_parent_type = get_field_type(annot_parent)

		if annot_parent_name in field_content\
				and annot_parent_type == PdfFieldType.RADIO_BTN_GROUP:
			button_index = field_content[annot_parent_name]
			button_group = btn_group_dict.get(annot_parent_name)

			if button_group is not None:
				# This instruction can raise an IndexError.
				button_name = button_group[button_index]

				# This function needs the RadioBtnGroup instances
				# because the index of the selected button is
				# required here.
				annot_parent[NameObject(_KEY_KIDS)].getObject()\
					[button_index].getObject()[NameObject(_KEY_AS)]\
					= NameObject(button_name)

				annot_parent[NameObject(_KEY_V)]\
					= NameObject(button_name)


def _update_text_field_or_checkbox(writer_annot, field_value, field_type):
	if field_type == PdfFieldType.TEXT_FIELD:
		writer_annot.update({
			NameObject(_KEY_V): TextStringObject(field_value)
		})

	elif field_type == PdfFieldType.CHECKBOX:
		writer_annot.update({
			NameObject(_KEY_AS): NameObject(field_value),
			NameObject(_KEY_V): NameObject(field_value)
		})
