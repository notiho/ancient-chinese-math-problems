import sys
import csv
import regex
from pathlib import Path
from utils import *

directory = Path(sys.argv[1])
timestamp = directory.name

content_start_marker = "#----- content starts here -----\n"
content_end_marker = "#----- content ends here -----\n"

with open(directory / "comment_alignments.csv", "w", newline = "") as outfile:
	writer = csv.writer(outfile)
	writer.writerow(["timestamp", "configuration", "problem_id", "run", "comment", "code_lines", "aligned"])
	
	for code_filename in directory.glob("*/passed/*.py"):
		configuration = code_filename.parent.parent.name
		problem_id = "_".join(code_filename.name.split("_")[:3])
		run = code_filename.stem.split("_")[-1]
		
		with open(code_filename) as infile:
			content = infile.read()
		content = content[content.index(content_start_marker) + len(content_start_marker):content.index(content_end_marker)]
		content_without_comment_blocks = ""
		in_comment = False
		for l in content.split("\n"):
			if l.startswith('"""'):
				in_comment = not in_comment
			else:
				if not in_comment:
					content_without_comment_blocks += l  + "\n"
		assert not in_comment
		
		blocks = content_without_comment_blocks.split("\n\n")
		
		for b in blocks:
			b = b.strip()
			if b.startswith("#"):
				comment = b.split("\n")[0][1:].strip()
				# Remove explanation in parenthesis
				if "(" in comment:
					comment = comment.split("(")[0].strip()
				can_be_aligned = is_contained_in_question_procedure_text(comment, problem_id)
				writer.writerow([timestamp, configuration, problem_id, run, comment, "\n".join(b.split("\n")[1:]), can_be_aligned])
			else:
				if len(b.strip()) > 0:
					writer.writerow([timestamp, configuration, problem_id, run, "", b.strip(), False])
