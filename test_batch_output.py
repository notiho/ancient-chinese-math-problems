import json
import sys
import glob
import csv
from pathlib import Path

from utils import *

directory = sys.argv[1]
results = []
for filename in glob.glob(directory + "*/*.jsonl"):
	with open(filename) as infile:
		results.extend(json.loads(l) for l in infile.readlines())

input_directory = Path("batch_inputs") / Path(directory).parts[-1]
inputs_by_id = dict()
for filename in input_directory.glob("*/*.jsonl"):
	with open(filename) as infile:
		for l in infile:
			i = json.loads(l)
			inputs_by_id[i["custom_id"]] = i["body"]["messages"]


with open(directory + "statistics.csv", "w", newline = "") as outfile:
	csv_writer = csv.writer(outfile)
	csv_writer.writerow(["id", "run", "configuration", "problem_id", "passed", "error"])
	for r in results:
		identifier = r["custom_id"]
		timestamp, configuration, problem_id = identifier.split("#")
		problem = problems_by_id[problem_id]
		for i, choice in enumerate(r["response"]["body"]["choices"]):
			content = choice["message"]["content"]
			
			preamble = None
			postscript = None
			
			if "```python" in content:
				preamble = ""
				code = ""
				
				while "```python" in content:
					next_code_start = content.index("```python")
					next_code_end = content.find("```", next_code_start + len("```python"))
					if next_code_end == -1:
						next_code_end = len(content)
					preamble += content[:next_code_start]
					code += content[next_code_start + len("```python"):next_code_end]
					content = content[next_code_end + len("```"):]
				
				postscript = content
				content = code
			
			passed_check, message = check_script_against_answer(content, problems_by_id[problem_id])
			
			csv_writer.writerow([identifier, i, configuration, problem_id, passed_check, message])
			
			code_path = Path(f"batch_outputs/{timestamp}/{configuration}/{'passed' if passed_check else 'failed'}")
			code_path.mkdir(exist_ok = True, parents = True)
			
			with open(code_path / (problem_id + "_" + str(i) + ".py"), "w") as code_outfile:
				code_outfile.write('"""\n')
				code_outfile.write(inputs_by_id[r["custom_id"]][-1]["content"] + "\n")
				code_outfile.write('"""\n\n')
				
				if preamble is not None:
					code_outfile.write('"""\n')
					code_outfile.write(preamble)
					code_outfile.write('\n"""\n\n')
				
				code_outfile.write(content)
				
				if postscript is not None:
					code_outfile.write('\n\n"""\n')
					code_outfile.write(postscript)
					code_outfile.write('\n"""\n\n')
				
				code_outfile.write('\n"""\n' + message + '"""\n')
