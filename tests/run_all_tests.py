from os import system
from pathlib import Path


local_dir = Path(__file__).parent.resolve()

system(f"pytest {local_dir/'field_type_tests.py'}")
