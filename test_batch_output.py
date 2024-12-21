import json
import sys
from pathlib import Path
from collections import defaultdict
import numpy as np

from utils import *

filename = sys.argv[1]
with open(filename) as infile:
	results = [json.loads(l) for l in infile.readlines()]

total_failed = 0

passed = defaultdict(list)

for r in results:
	identifier = r["custom_id"]
	timestamp, problem_id = identifier.split("#")
	problem = problems_by_id[problem_id]
	for i, choice in enumerate(r["response"]["body"]["choices"]):
		content = choice["message"]["content"]
		
		if "```python" in content:
			content = content.split("```python")[1]
			content = content.split("```")[0]
		
		passed_check, message = check_script_against_answer(content, problems_by_id[problem_id])
		
		passed[i].append(passed_check)
		
		if not passed_check:
			print(f"Script for {problem_id} failed:")
			print(message)
			total_failed += 1
		
		code_path = Path(f"batch_outputs/{timestamp}/{'passed' if passed_check else 'failed'}")
		code_path.mkdir(exist_ok = True, parents = True)
		
		with open(code_path / (problem_id + "_" + str(i) + ".py"), "w") as outfile:
			if "preceding_question" in problem:
				outfile.write("#" + problem["preceding_question"] + "\n")
			if "preceding_answer" in problem:
				outfile.write("#" + problem["preceding_answer"] + "\n")
			outfile.write("#" + problem["question"] + "\n")
			outfile.write("#" + procedures_by_id[problem["procedure_id"]]["text"] + "\n")
			outfile.write("#" + format_answer_for_prompt_with_numbers(problem["answer_structured"]) + "\n")
			outfile.write(content)

for i, p in passed.items():
	print(f"Run #{i}: {sum(p)} / {len(results)} passed")

print(f"Passed in any: {np.sum(np.sum(list(passed.values()), axis = 0) > 0)} / {len(results)}")
