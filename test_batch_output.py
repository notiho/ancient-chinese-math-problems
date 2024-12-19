import json
import sys
from pathlib import Path

from utils import *

filename = sys.argv[1]
with open(filename) as infile:
	results = [json.loads(l) for l in infile.readlines()]

total_failed = 0

for r in results:
	identifier = r["custom_id"]
	timestamp, problem_id = identifier.split("#")
	problem = problems_by_id[problem_id]
	content = r["response"]["body"]["choices"][0]["message"]["content"]
	
	if "```python" in content:
		content = content.split("```python")[1]
		content = content.split("```")[0]
	
	code_path = Path(f"batch_outputs/{timestamp}")
	code_path.mkdir(exist_ok = True)
	
	with open(code_path / (problem_id + ".py"), "w") as outfile:
		if "preceding_question" in problem:
			outfile.write("#" + problem["preceding_question"] + "\n")
		if "preceding_answer" in problem:
			outfile.write("#" + problem["preceding_answer"] + "\n")
		outfile.write("#" + problem["question"] + "\n")
		outfile.write("#" + procedures_by_id[problem["procedure_id"]]["text"] + "\n")
		outfile.write("#" + format_answer_for_prompt_with_numbers(problem["answer_structured"]) + "\n")
		outfile.write(content)
	
	passed_check, message = check_script_against_answer(content, problems_by_id[problem_id])
	
	if not passed_check:
		print(f"Script for {problem_id} failed:")
		print(message)
		total_failed += 1

print(f"{len(results) - total_failed} / {len(results)} passed")
