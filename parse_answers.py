import json
import glob
import regex
from fractions import Fraction

filenames = glob.glob("dataset/*_problems_*.json")

single_digits = "一二三四五六七八九"
powers_of_ten = "十百千萬"
digit_chars = single_digits + powers_of_ten

integer_re = f"(?=[{digit_chars}]+)(([{single_digits}]?千)?([{single_digits}]?百)?([{single_digits}]?十)?[{single_digits}]?萬)?([{single_digits}]?千)?([{single_digits}]?百)?([{single_digits}]?十)?[{single_digits}]?"

units_of_measurement = "寸尺丈步歩頃畝畆里斗升頃畝錢箇兩銖枚返斛石雞鹿人矢日月斤鈞翭匹度乘疋周盤㪷文貫端合勺隻顆戸家秉束分氂毫絲忽觔功領抄撮帀枝磚黍"

quantity_re = regex.compile(f"(?P<x>{integer_re})(分(?P<u>[{units_of_measurement}]?)之(?P<y>{integer_re})|(?P<u>[{units_of_measurement}]?)((?P<h>半|少半|[大太]半)(?P=u)?)?)")
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
				assert(rst == 0)
				rst += single_digits.index(c) + 1
				i += 1
			else:
				assert(prev_power_of_ten is None or powers_of_ten.index(prev_power_of_ten) < powers_of_ten.index(c))
				prev_power_of_ten = c
				
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
		elif match.group("h") in ["太半", "大半"]:
			rst += Fraction(2, 3)
		else:
			assert(False)
	
	return [rst, unit]

max_slots = 0

for f in filenames:
	with open(f) as infile:
		try:
			data = json.loads(infile.read())
		except json.decoder.JSONDecodeError as e:
			raise Exception(f"Error when parsing JSON file: '{f}'") from e
	
	for problem in data:
		if "answer_structured_manual" in problem:
			continue
		
		answer = problem["answer"]
		
		prev_quantity_end = 0
		
		sequence = []
		
		num_slots = 0
		
		fractions_without_units = []
		
		for i in quantity_re.finditer(answer):
			num_slots += 1
			if i.start() != prev_quantity_end:
				sequence.append(answer[prev_quantity_end:i.start()])
			q = parse_quantity(i)
			
			if q[0].denominator != 1 and q[1] == "":
				fractions_without_units.append(q)
			
			# Add fractional value of same unit as previous item to that item
			if len(sequence) > 0 and i.start() == prev_quantity_end and sequence[-1][1] == q[1]:
				sequence[-1][0] += q[0]
			else:
				sequence.append(q)
			
			prev_quantity_end = i.end()
		
		max_slots = max(max_slots, num_slots)
		
		if len(fractions_without_units) > 0:
			print(f"Detected fraction without unit ({problem['id']}): '{answer}'\t{fractions_without_units}")
		
		if len(sequence) == 0:
			print(f"{problem['id']}: Unable to parse: '{answer}'")
		else:
			if prev_quantity_end != len(answer):
				sequence.append(answer[prev_quantity_end:])
			sequence = [[str(x[0]), x[1]] if isinstance(x, list) else x for x in sequence]
			problem["answer_structured"] = sequence
	
	with open(f, "w") as outfile:
		json.dump(data, outfile, ensure_ascii = False, indent = 4)

print(f"Max slots: {max_slots}")
