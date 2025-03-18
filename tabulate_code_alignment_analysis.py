import sys
import glob
import csv
from pathlib import Path
from collections import Counter

directory = sys.argv[1]

error_types = Counter()

for code_filename in glob.glob(directory + "*.py"):
	with open(code_filename) as infile:
		lines = infile.readlines()
	
	error_lines = [l for l in lines if l.startswith("#ERR:") or l.startswith("#NO_ERR")]
	
	if len(error_lines) == 0:
		print(f"Warning: no errors marked in '{code_filename}'")
	
	error_types.update(error_lines)

for i, n in error_types.most_common():
	print(i.strip(), n)
