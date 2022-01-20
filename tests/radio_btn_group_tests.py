import pytest

from ..src import RadioBtnGroup


def make_radio_button_group():
	return RadioBtnGroup("LeGroupe", "BtnA", "BtnB", "BtnC")


def test_init_except():
	except_msg = "At least one button name must be provided."
	with pytest.raises(ValueError, match=except_msg):
		button_group = RadioBtnGroup("LeGroupe")


def test_name():
	button_group = make_radio_button_group()
	assert button_group.name == "LeGroupe"
