import pytest

from ..PyPDF2_Fields import RadioBtnGroup


def getitem_exception_test(index):
	button_group = make_radio_button_group()
	except_msg = f"Radio button group LeGroupe does not have index {index}."
	with pytest.raises(IndexError, match=except_msg):
		button_group[index]


def make_radio_button_group():
	return RadioBtnGroup("LeGroupe", "BtnA", "BtnB", "BtnC")


def test_init_exception():
	except_msg = "At least one button name must be provided."
	with pytest.raises(ValueError, match=except_msg):
		button_group = RadioBtnGroup("LeGroupe")


def test_eq_true():
	button_group1 = make_radio_button_group()
	button_group2 = RadioBtnGroup("LeGroupe", "BtnA", "BtnB", "BtnC")

	assert button_group1 == button_group2


def test_eq_false_button_name():
	button_group1 = make_radio_button_group()
	button_group2 = RadioBtnGroup("LeGroupe", "BtnA", "BtnX", "BtnC")

	assert button_group1 != button_group2


def test_eq_false_group_name():
	button_group1 = make_radio_button_group()
	button_group2 = RadioBtnGroup("AutreGroupe", "BtnA", "BtnB", "BtnC")

	assert button_group1 != button_group2


def test_eq_false_different_type():
	button_group1 = make_radio_button_group()
	button_group2 = "AutreGroupe"

	assert button_group1 != button_group2


def test_getitem_a():
	button_group = make_radio_button_group()
	assert button_group[0] == "BtnA"
	assert button_group[-3] == "BtnA"


def test_getitem_b():
	button_group = make_radio_button_group()
	assert button_group[1] == "BtnB"
	assert button_group[-2] == "BtnB"


def test_getitem_c():
	button_group = make_radio_button_group()
	assert button_group[2] == "BtnC"
	assert button_group[-1] == "BtnC"


def test_getitem_exception_positive_index():
	getitem_exception_test(3)


def test_getitem_exception_negative_index():
	getitem_exception_test(-4)


def test_has_index():
	button_group = make_radio_button_group()
	assert not button_group.has_index(3)
	assert button_group.has_index(2)
	assert button_group.has_index(-3)
	assert not button_group.has_index(-4)


def test_index():
	button_group = make_radio_button_group()
	assert button_group.index("BtnA") == 0
	assert button_group.index("BtnB") == 1
	assert button_group.index("BtnC") == 2


def test_index_exception():
	button_group = make_radio_button_group()
	button_name = "Inexistant"
	except_msg =\
		f"Radio button group LeGroupe does not have button {button_name}."
	with pytest.raises(ValueError, match=except_msg):
		button_group.index(button_name)


def test_iterator():
	button_group = make_radio_button_group()
	actual_names = tuple(button_group)
	expected_names = ("BtnA", "BtnB", "BtnC")
	assert actual_names == expected_names


def test_length():
	button_group = make_radio_button_group()
	assert len(button_group) == 3


def test_name():
	button_group = make_radio_button_group()
	assert button_group.name == "LeGroupe"

def test_repr():
	button_group = make_radio_button_group()
	actual_repr = repr(button_group)
	expected_repr = "RadioBtnGroup('LeGroupe', 'BtnA', 'BtnB', 'BtnC')"
	assert actual_repr == expected_repr
	assert eval(actual_repr) == button_group
