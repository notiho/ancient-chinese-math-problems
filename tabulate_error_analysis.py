import sys
import glob
import csv
from pathlib import Path

directory = sys.argv[1]

timestamp = Path(directory).parts[-2]

with open("error_analysis/error_analysis.csv", "w") as outfile:
	writer = csv.writer(outfile)
	writer.writerow(["timestamp", "problem_id", "error_type"])
	
	for code_filename in glob.glob(directory + "*.py"):
		with open(code_filename) as infile:
			lines = infile.readlines()
		
		error_lines = [l for l in lines if l.startswith("#ERR:")]
		
		if len(error_lines) == 0:
			print(f"Warning: no errors marked in '{code_filename}'")
		
		for i in error_lines:
			writer.writerow([timestamp, "_".join(Path(code_filename).name.split("_")[:3]),
				i[len("#ERR: "):].strip()])
