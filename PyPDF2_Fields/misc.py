from PyPDF2 import PdfFileWriter
from PyPDF2.generic import BooleanObject,\
	IndirectObject,\
	NameObject


_KEY_ACROFORM = "/AcroForm"
_KEY_NEED_APPEARANCES = "/NeedAppearances"


def make_writer_from_reader(pdf_reader, editable):
	"""
	Creates a PdfFileWriter instance from the content of a PdfFileReader
	instance. Depending on parameter editable, it will be possible to modify
	the fields of the file produced by the returned writer.

	Args:
		pdf_reader (PdfFileReader): an instance of PdfFileReader
		editable (bool): If True, the fields in the file created by the
			returned writer can be modified.

	Returns:
		PdfFileWriter: an instance that contains the pages of pdf_reader
	"""
	pdf_writer = PdfFileWriter()

	if editable:
		for page in pdf_reader.pages:
			pdf_writer.addPage(page)

	else:
		pdf_writer.cloneDocumentFromReader(pdf_reader)

	return pdf_writer


def pair_fields_name_and_val(pdf_fields, filter_none):
	"""
	Creates a dictionary that maps the name of a PDF file's fields to their
	value.

	Args:
		pdf_fields (dict): It maps the name of the file's fields to an object
			of type PyPDF2.generic.Field. It is obtained through
			PdfFileReader's method getFields.
		filter_none (bool): If this argument is True, None values are excluded
			from the returned dictionary.

	Returns:
		dict: It maps the fields' name to their value.
	"""
	name_val_dict = dict()

	for mapping_name, field in pdf_fields.items():
		field_val = field.value

		if not filter_none or field_val is not None:
			name_val_dict[mapping_name] = field_val

	return name_val_dict


def set_need_appearances(pdf_writer, bool_val):
	"""
	Sets property _root_object["/AcroForm"]["/NeedAppearances"] of the given
	PdfFileWriter instance to a Boolean value. Setting it to True can be
	necessary to make the text fields' content visible in the file produced
	by pdf_writer.

	Args:
		bool_val (bool): the Boolean value to which /NeedAppearances will be
			set
	"""
	# https://stackoverflow.com/questions/47288578/pdf-form-filled-with-pypdf2-does-not-show-in-print
	catalog = pdf_writer._root_object

	# Get the AcroForm tree and add /NeedAppearances attribute
	if _KEY_ACROFORM not in catalog:
		pdf_writer._root_object.update({NameObject(_KEY_ACROFORM):
			IndirectObject(len(pdf_writer._objects), 0, pdf_writer)})

	need_appearances = NameObject(_KEY_NEED_APPEARANCES)
	pdf_writer._root_object[_KEY_ACROFORM][need_appearances]\
		= BooleanObject(bool_val)
