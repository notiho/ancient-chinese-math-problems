import glob
from pathlib import Path

from utils import load_all_problems, check_script_against_answer

filenames = sorted(glob.glob("example_code/*.py"))

problems = load_all_problems()
problems_by_id = { p["id"]: p for p in problems }

for filename in filenames:
	with open(filename) as infile:
		script_source = infile.read()
	
	problem_id = Path(filename).stem
	
	passed_check, message = check_script_against_answer(script_source, problems_by_id[problem_id])
	
	if not passed_check:
		print(f"Script for {problem_id} failed:")
		print(message)
