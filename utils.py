import glob
import json
from fractions import Fraction
from pathlib import Path
from func_timeout import func_timeout, FunctionTimedOut

titles_to_pinyin = {
	"九章算術": "jiuzhang",
	"海島算經": "haidao",
	"孫子算經": "sunzi",
	"五曹算經": "wucao",
	"夏侯陽算經": "xiahouyang",
	"張邱建算經": "zhangqiujian",
	"緝古算經": "jigu"
}

"""度之所起起于忽欲知其忽蠶吐絲為忽十忽為一絲
十絲為一毫十毫為一氂十氂為一分十分為一寸十
寸為一尺十尺為一丈十丈為一引五十引為一端四
十尺為一匹六尺為一步二百四十步為一畆三百步
為一里

稱之所起起于黍十黍為一絫十絫為一銖二十四銖
為一兩十六兩為一觔三十觔為一鈞四鈞為一石

量之所起起于粟六粟為一圭十圭為一撮十撮為一
抄十抄為一勺十勺為一合十合為一升十升為一斗
十斗為一斛"""

unit_conversions = [
	[
		("疋", 1),
		("丈", 4),
		("尺", 10),
		("寸", 10),
		("分", 10)
	],
	[
		("匹", 1),
		("丈", 4),
		("尺", 10),
		("寸", 10),
		("分", 10)
	],
	[
		("端", 1),
		("引", 50),
		("丈", 10),
		("尺", 10),
		("寸", 10),
		("分", 10)
	],
	[
		("里", 1),
		("步", 300)
	],
	[
		("頃", 1),
		("畆", 100),
		("歩", 240),
		("尺", 6)
	],
	[
		("頃", 1),
		("畝", 100),
		("歩", 240),
		("尺", 6)
	],
	[
		("頃", 1),
		("畝", 100),
		("步", 240),
		("尺", 6)
	],
	[
		("石", 1),
		("鈞", 4),
		("斤", 30),
		("兩", 16),
		("銖", 24),
		("絫", 10),
		("黍", 10)
	],
	[
		("石", 1),
		("鈞", 4),
		("斤", 30),
		("两", 16),
		("銖", 24),
		("絫", 10),
		("黍", 10)
	],
	[
		("石", 1),
		("鈞", 4),
		("觔", 30),
		("兩", 16),
		("銖", 24)
	],
	[
		("斛", 1),
		("㪷", 10),
		("升", 10),
		("合", 10),
		("勺", 10),
		("抄", 10),
		("撮", 10)
	],
	[
		("斛", 1),
		("斗", 10),
		("升", 10),
		("合", 10),
		("勺", 10),
		("抄", 10),
		("撮", 10)
	],
	[
		("貫", 1),
		("文", 1000),
		("分", 10),
		("氂", 10),
		("毫", 10),
		("絲", 10),
		("忽", 10)
	]
]

def try_convert_smaller_into_larger_unit(x, u1, u2):
	for conversions in unit_conversions:
		if u1 in [c[0] for c in conversions] and u2 in [c[0] for c in conversions]:
			i = next(i for i, c in enumerate(conversions) if c[0] == u1)
			
			while conversions[i][0] != u2:
				x /= conversions[i][1]
				i -= 1
				if i < 0:
					return None
			
			return x
	return None

def load_all_problems():
	problem_files = glob.glob("dataset/*_problems_*.json")
	problems = []

	for f in problem_files:
		with open(f) as infile:
			try:
				problems.extend(json.loads(infile.read()))
			except json.decoder.JSONDecodeError as e:
				raise Exception(f"Error when parsing JSON file: '{f}'") from e
	
	for p in problems:
		if "answer_structured_manual" in p:
			p["answer_structured"] = p["answer_structured_manual"]
	
	return problems

problems = load_all_problems()
problems_by_id = { p["id"]: p for p in problems }

def load_procedures_by_id():
	procedure_files = glob.glob("dataset/*_procedures_*.json")
	procedures = []

	for f in procedure_files:
		with open(f) as infile:
			try:
				procedures.extend(json.loads(infile.read()))
			except json.decoder.JSONDecodeError as e:
				raise Exception(f"Error when parsing JSON file: '{f}'") from e
	
	return { p["id"]: p for p in procedures }

procedures_by_id = load_procedures_by_id()

def format_answer_for_prompt(answer, include_punctuation):
	rst = []
	cur_slot_index = 0
	for x in answer:
		if isinstance(x, list):
			cur_slot_letter = chr(ord('a') + cur_slot_index if cur_slot_index < 26 else ord('a') + cur_slot_index - 26)
			rst.append(cur_slot_letter + x[1])
			cur_slot_index += 1
		else:
			rst.append(x if include_punctuation else remove_punctuation(x))
	return " ".join(rst)

def format_answer_for_prompt_with_numbers(answer, include_punctuation):
	rst = []
	cur_slot_index = 0
	for x in answer:
		if isinstance(x, list):
			cur_slot_letter = chr(ord('a') + cur_slot_index if cur_slot_index < 26 else ord('a') + cur_slot_index - 26)
			rst.append(cur_slot_letter + "(=" + str(x[0]) + ")" + x[1])
			cur_slot_index += 1
		else:
			rst.append(x if include_punctuation else remove_punctuation(x))
	return " ".join(rst)

def check_script_against_answer(script_source, problem):
	script_source = "from fractions import Fraction\n"  + script_source
	
	answer = problem["answer_structured"]
	
	variables = dict()
	
	try:
		func_timeout(3, exec, args = (script_source, variables))
	except FunctionTimedOut:
		return (False, "Timed out")
	except Exception as e:
		return (False, "Code error: " + str(e))
	
	cur_slot_index = 1
	slot_problems = []
	for x in answer:
		if isinstance(x, list):
			var_name = chr(ord('`') + cur_slot_index)
			
			if not var_name in variables:
				slot_problems.append(f"Missing variable in output: '{var_name}'")
			elif not variables[var_name] == Fraction(x[0]):
				try:
					actual_value_str = str(variables[var_name])
				except ValueError as err:
					actual_value_str = "Too large to be printed"
				slot_problems.append(f"Variable '{var_name}' has wrong value. Expected: {x[0]}, Actual: {actual_value_str}")
			
			cur_slot_index += 1
	
	if slot_problems == []:
		return (True, "")
	else:
		return (False, "\n".join(slot_problems))

def problem_to_message(problem, procedure, include_punctuation, include_procedure, include_numerical_answers):
	punctuated_suffix = "_punctuated" if include_punctuation else ""
	user_message = ""
	if "preceding_question" in problem:
		user_message += problem["preceding_question" + punctuated_suffix] + "\n"
	if "preceding_answer" in problem:
		user_message += problem["preceding_answer" + punctuated_suffix] + "\n"
		
	user_message += problem["question" + punctuated_suffix] + "\n"
	
	if include_procedure:
		assert "text" + punctuated_suffix in procedure, f"Punctuated version requested for {procedure['id']} but does not exist"
		user_message += procedure["text" + punctuated_suffix] + "\n"
		if "referenced_procedure" in procedure:
			user_message += procedures_by_id[procedure["referenced_procedure"]]["text" + punctuated_suffix] + "\n"
	if include_numerical_answers:
		user_message += format_answer_for_prompt_with_numbers(problem["answer_structured"], include_punctuation)
	else:
		user_message += format_answer_for_prompt(problem["answer_structured"], include_punctuation)
	
	return {
		"role": "user",
		"content": user_message
	}

def problem_solution_to_messages(problem_id, include_punctuation, include_translation, include_procedure, include_numerical_answers):
	problem = problems_by_id[problem_id]
	procedure = procedures_by_id[problem["procedure_id"]]
	
	code_path_suffix = ""
	if not include_procedure:
		code_path_suffix = "_english"
	elif include_numerical_answers:
		code_path_suffix = "_with_solution"
	
	code_path = Path(f"example_code/{problem['id']}{code_path_suffix}.py")
	with open(code_path) as infile:
		code_lines = infile.readlines()
	
	first_blank = next(i for i, l in enumerate(code_lines) if l == "\n")
	code_lines = code_lines[first_blank + 1:]
	
	if not include_translation:
		block_quote_start = next(i for i, l in enumerate(code_lines) if l.startswith('"""'))
		block_quote_end = block_quote_start + 1 + next(i for i, l in enumerate(code_lines[block_quote_start + 1:]) if l.startswith('"""'))
		code_lines = code_lines[block_quote_end + 1:]
	
	return [problem_to_message(problem, procedure, include_punctuation = include_punctuation, include_procedure = include_procedure,
		include_numerical_answers = include_numerical_answers), {
		"role": "assistant",
		"content": "".join(code_lines)
	}]

punctuation_symbols = "。：︰；，、？「」"

def remove_punctuation(s):
	rst = ""
	for c in s:
		if not c in punctuation_symbols:
			rst += c
	return rst


def pretty_print_messages(messages):
	for m in messages:
		print(f"[{m['role']}] {m['content']}")


def is_contained_in_question_procedure_text(query, problem_id):
	problem = problems_by_id[problem_id]
	procedure = procedures_by_id[problem["procedure_id"]]
	
	return query in problem["question"] or query in problem.get("question_punctuated", "") or \
		query in problem.get("previous_question", "") or query in problem.get("previous_question_punctuated", "") or \
		query in problem.get("previous_answer", "") or query in problem.get("previous_answer_punctuated", "") or \
		query in procedure["text"] or query in procedure.get("text_punctuated", "") or \
		(query in procedures_by_id[procedure["referenced_procedure"]]["text"] if "referenced_procedure" in procedure else False) or \
		(query in procedures_by_id[procedure["referenced_procedure"]].get("text_punctuated") if "referenced_procedure" in procedure else False)
		
