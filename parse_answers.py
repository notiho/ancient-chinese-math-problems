import json
import glob
import regex
from fractions import Fraction

filenames = glob.glob("dataset/*_problems_*.json")

number_chars = "一二三四五六七八九十百千萬"
single_digits = "一二三四五六七八九"
powers_of_ten = "十百千萬"

units_of_measurement = "寸尺丈步畝里斗升頃畝錢箇兩銖枚返斛石雞鹿人矢日斤鈞翭匹"

quantity_re = regex.compile(f"(?P<x>[{number_chars}]+)(分(?P<u>[{units_of_measurement}]?)之(?P<y>[{number_chars}]+)|(?P<u>[{units_of_measurement}]?)((?P<h>半|少半|太半)(?P=u)?)?)")
print(quantity_re.pattern)

def parse_integer(s):
	if "萬" in s:
		left, right = s.split("萬")
		return parse_integer(left) * 10_000 + parse_integer(right)
	else:
		rst = 0
		prev_power_of_ten = None
		
		i = 0
		while i < len(s):
			c = s[len(s) - i - 1]
			if c in single_digits:
				assert(prev_power_of_ten is None)
				rst += single_digits.index(c) + 1
				i += 1
			else:
				assert(prev_power_of_ten is None or powers_of_ten.index(prev_power_of_ten) < powers_of_ten.index(c))
				
				if i == len(s) - 1 or s[len(s) - i - 2] in powers_of_ten:
					rst += 10 ** (powers_of_ten.index(c) + 1)
					i += 1
				else:
					rst += (1 + single_digits.index(s[len(s) - i - 2])) * 10 ** + (powers_of_ten.index(c) + 1)
					i += 2
		
		return rst

def parse_quantity(match):
	x = parse_integer(match.group("x"))
	unit = match.group("u")
	y = parse_integer(match.group("y")) if match.group("y") else None
	
	if y:
		rst = Fraction(y, x)
	else:
		rst = Fraction(x, 1)
	
	if match.group("h"):
		if match.group("h") == "半":
			rst += Fraction(1, 2)
		elif match.group("h") == "少半":
			rst += Fraction(1, 3)
		elif match.group("h") == "太半":
			rst += Fraction(2, 3)
		else:
			assert(False)
	
	return [rst, unit]

for f in filenames:
	with open(f) as infile:
		try:
			data = json.loads(infile.read())
		except json.decoder.JSONDecodeError as e:
			raise Exception(f"Error when parsing JSON file: '{f}'") from e
	
	for problem in data:
		answer = problem["answer"]
		
		prev_quantity_end = 0
		
		sequence = []
		
		for i in quantity_re.finditer(answer):
			if i.start() != prev_quantity_end:
				sequence.append(answer[prev_quantity_end:i.start()])
			q = parse_quantity(i)
			
			if len(sequence) > 0 and i.start() == prev_quantity_end and sequence[-1][1] == q[1]:
				assert(q != "")
				sequence[-1][0] += q[0]
			else:
				sequence.append(q)
			
			prev_quantity_end = i.end()
		
		if len(sequence) == 0:
			print(f"Unable to parse: '{answer}'")
		else:
			if prev_quantity_end != len(answer):
				sequence.append(answer[prev_quantity_end:])
			sequence = [[str(x[0]), x[1]] if isinstance(x, list) else x for x in sequence]
			problem["answer_structured"] = sequence
	
	with open(f, "w") as outfile:
		json.dump(data, outfile, ensure_ascii = False, indent = 4)
