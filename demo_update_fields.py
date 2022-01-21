from pathlib import Path
from PyPDF2 import PdfFileReader

from src import\
	make_writer_from_reader,\
	RadioBtnGroup,\
	set_need_appearances,\
	update_page_fields,\
	pdf_field_name_val_dict

file_empty_fields = Path("tests/fields_empty.pdf")
file_filled_fields = Path("demo_result.pdf")
reader = PdfFileReader(file_empty_fields.open(mode="rb"), strict=False)
writer = make_writer_from_reader(reader, True)

field_content = {
	"Détails3": "Dépense 3",
	"Montant$2": 2,
	"Group2": 1,
	"Group4": 0,
	"Boite1": True,
	"Date": "2021-03-01"
}

radio_btn_group1 = RadioBtnGroup(
	"Group1", "/Choix1", "/Choix2")
radio_btn_group2 = RadioBtnGroup(
	"Group2", "/Choix1", "/Choix2")
radio_btn_group4 = RadioBtnGroup(
	"Group4", "/Dépôt", "/Chèque")

update_page_fields(writer.getPage(0), field_content,
	radio_btn_group1, radio_btn_group2, radio_btn_group4)

set_need_appearances(writer, True) # To make field values visible
writer.write(file_filled_fields.open(mode="wb"))
