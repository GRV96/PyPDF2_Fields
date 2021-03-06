"""
This demo of library PyPDF2_Fields creates a copy of a report template and sets
some of its fields to an arbitrary value.
"""


from argparse import ArgumentParser
from pathlib import Path
from PyPDF2 import PdfFileReader

from PyPDF2_Fields import\
	make_writer_from_reader,\
	RadioBtnGroup,\
	set_need_appearances,\
	update_page_fields


parser = ArgumentParser(description=__doc__)

parser.add_argument("-e", "--editable", action="store_true",
	help="Makes the generated document editable.")

parser.add_argument("-u", "--unset-na", action="store_true",
	help="Sets property NeedAppearances of the generated document to False.")

args = parser.parse_args()
editable = args.editable
need_appearances = not args.unset_na

local_dir = Path(__file__).parent.resolve()
path_empty_fields = local_dir/"tests/fields_empty.pdf"
# Included in gitignore. Update if you change it.
path_filled_fields = local_dir/"demo_update_fields_result.pdf"

reader = PdfFileReader(path_empty_fields.open(mode="rb"), strict=False)
writer = make_writer_from_reader(reader, editable)

field_content = {
	"Détails3": "Dépense 3",
	"Montant$2": 2,
	"Group2": 1,
	"Group4": 0,
	# "Yes" in French. Makes the box checked.
	"Boite1": "/Oui",
	# "No" in French. Makes the box unchecked. Optional.
	"Boite3": "/Non",
	"Date": "2022-01-21",
	"Province": "Québec"
}

radio_btn_group1 = RadioBtnGroup(
	"Group1", "/Choix1", "/Choix2")
radio_btn_group2 = RadioBtnGroup(
	"Group2", "/Choix1", "/Choix2")
radio_btn_group4 = RadioBtnGroup(
	"Group4", "/Dépôt", "/Chèque")

update_page_fields(writer.getPage(0), field_content,
	radio_btn_group1, radio_btn_group2, radio_btn_group4)

set_need_appearances(writer, need_appearances)
writer.write(path_filled_fields.open(mode="wb"))
