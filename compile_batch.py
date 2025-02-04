import json
import datetime
import tiktoken
import glob
from pathlib import Path

from utils import *

system_prompt_few_shot = """Translate ancient Chinese math problems into Python code, ensuring that each section of code adheres to the structure of the procedure ("術") provided. Put the part of the procedure that corresponds to each block of code as a comment before the block. Ensure that the complete procedure is encoded. Use the class "Fraction" to represent numbers that might not be integers and use the appropriate units for each calculation. Don't use any other external functions."""
system_prompt_few_shot_no_restrictions = """Translate ancient Chinese math problems into Python code. Ensure that the complete procedure is encoded. Use the class "Fraction" to represent numbers that might not be integers and use the appropriate units for each calculation."""
system_prompt_zero_shot = """Translate ancient Chinese math problems into Python code that computes the values of the unknowns replaced by letters ("a", ...) in the answer ("荅" or "答"). Write the solutions into variables that have exactly the same name as the unknowns. Use the class "Fraction" to represent numbers that might not be integers and use the appropriate units for each calculation. Don't use any other external functions."""
system_prompt_few_shot_no_procedure = """Translate ancient Chinese math problems into Python code. Use the class "Fraction" to represent numbers that might not be integers and use the appropriate units for each calculation. Don't use any other external functions."""


model = "gpt-4o-2024-11-20"
temperature = 0.2
num_choices = 5

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

previous_input_ids_by_body = dict()
for filename in glob.glob("batch_inputs/*/*/*.jsonl"):
	if not Path(filename.replace("batch_inputs", "batch_outputs")).is_file():
		continue
	with open(filename) as infile:
		for l in infile:
			i = json.loads(l)
			previous_input_ids_by_body[json.dumps(i["body"])] = i["custom_id"]

def estimate_tokens(s):
	encoding = tiktoken.encoding_for_model(model)
	return len(encoding.encode(s))

configurations = [
	"zero-shot",
	"few-shot",
	"few-shot-no-restrictions",
	"no-punctuation",
	"no-punctuation-extended-dataset",
	"no-translation",
	"no-procedures",
	"with-numerical-answers"
]

exemplar_problems = ["九章算術_1_0",
	"九章算術_2_0", "九章算術_3_0",
	"九章算術_4_0", "九章算術_5_0"]

def get_system_prompt(configuration):
	if configuration == "zero-shot":
		return system_prompt_zero_shot
	elif configuration == "no-procedures":
		return system_prompt_few_shot_no_procedure
	elif configuration == "few-shot-no-restrictions":
		return system_prompt_few_shot_no_restrictions
	else:
		return system_prompt_few_shot

def get_exemplar_messages(configuration):
	if configuration == "zero-shot":
		return []
	else:
		include_punctuation = "no-punctuation" not in configuration
		include_procedure = configuration != "no-procedures"
		include_numerical_answers = configuration == "with-numerical-answers"
		include_translation = configuration != "no-translation"
		
		rst = []
		
		for i in exemplar_problems:
			rst.extend(problem_solution_to_messages(i, include_punctuation = include_punctuation,
				include_procedure = include_procedure, include_numerical_answers = include_numerical_answers,
				include_translation = include_translation))
		
		return rst

request_count = 0
total_tokens = 0
can_reuse = 0

for configuration in configurations:
	messages = [{
		"role": "system",
		"content": get_system_prompt(configuration)
	}] + get_exemplar_messages(configuration)

	directory = Path(f"batch_inputs/{timestamp}/{configuration}")
	directory.mkdir(parents = True)
	
	cur_configuration_request_count = 0
	
	for p in problems:
		include_punctuation = "no-punctuation" not in configuration
		include_procedure = configuration != "no-procedures"
		include_numerical_answers = configuration == "with-numerical-answers"
		
		if p["id"] in exemplar_problems:
			continue
		
		if "basic_fraction" in p:
			continue
		
		if not "question_punctuated" in p and configuration != "no-punctuation-extended-dataset":
			continue
		elif "question_punctuated" in p and configuration == "no-punctuation-extended-dataset":
			continue
		
		request_count += 1
		cur_configuration_request_count += 1
		
		cur_messages = messages + [problem_to_message(p, procedures_by_id[p["procedure_id"]], include_punctuation = include_punctuation,
			include_procedure = include_procedure, include_numerical_answers = include_numerical_answers)]
		
		if cur_configuration_request_count == 1:
			print("\n\n" + configuration)
			pretty_print_messages(cur_messages)
		
		body = {
			"model": model,
			"temperature": temperature,
			"seed": 1,
			"messages": cur_messages,
			"n": num_choices
		}
		
		if json.dumps(body) in previous_input_ids_by_body:
			can_reuse += 1
			with open(f"batch_inputs/{timestamp}/reuse.txt", "a") as outfile:
				outfile.write(previous_input_ids_by_body[json.dumps(body)] + "\n")
		else:
			file_index = 0
			
			filename = directory / f"{timestamp}_{titles_to_pinyin[p['source_title']]}_{p['source_juan']}_{file_index}.jsonl"
			while filename.is_file() and filename.stat().st_size >= 50_000:
				file_index += 1
				filename = directory / f"{timestamp}_{titles_to_pinyin[p['source_title']]}_{p['source_juan']}_{file_index}.jsonl"
			
			with open(filename, "a") as outfile:
				outfile.write(json.dumps({
					"custom_id": f"{timestamp}#{configuration}#{p['id']}",
					"method": "POST",
					"url": "/v1/chat/completions",
					"body": body
				}, ensure_ascii = False) + "\n")
			total_tokens += sum(estimate_tokens(i["content"]) for i in cur_messages)


print(f"Wrote {len(problems)} queries, estimated tokens: {total_tokens}, reuse problems: {can_reuse}")
