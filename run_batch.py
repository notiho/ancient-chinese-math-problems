import sys
import json
import time
from pathlib import Path
from glob import glob
from openai import OpenAI

directory = sys.argv[1]

previous_outputs_by_id = dict()
for filename in glob("batch_outputs/*/*/*.jsonl"):
	with open(filename) as infile:
		for l in infile:
			i = json.loads(l)
			previous_outputs_by_id[i["custom_id"]] = l

with open(Path(directory) / "reuse.txt") as reuses:
	for i in reuses:
		i = i.strip()
		filename = Path(f"batch_outputs/{Path(directory).name}/{'/'.join(i.split('#')[1:])}_reuse.jsonl")
		filename.parent.mkdir(parents = True, exist_ok = True)
		with open(filename, "w") as outfile:
			outfile.write(previous_outputs_by_id[i])

client = OpenAI()

meta_filename = Path(directory) / "index.json"

with open(meta_filename) as infile:
	files = json.loads(infile.read())

wait_period = 60

for f in files:
	if not "batch_id" in f:
		batch = client.batches.create(
			input_file_id = f["id"],
			endpoint = "/v1/chat/completions",
			completion_window = "24h",
			metadata = {
				"local_filename": f["local_filename"]
			}
		)
		f["batch_id"] = batch.id
		f["batch_status"] = ""
		with open(meta_filename, "w") as outfile:
			json.dump(files, outfile, indent = 4)
	
	while f["batch_status"] != "completed":
		time.sleep(30)
		batch = client.batches.retrieve(f["batch_id"])
		f["batch_status"] = batch.status
		print(f"Got status {f['batch_status']} for file {f['local_filename']}")
		with open(meta_filename, "w") as outfile:
			json.dump(files, outfile, indent = 4)
		if f["batch_status"] == "failed":
			if batch.errors.data[0].code == "token_limit_exceeded":
				print(f"Token limit exceeded. Try again later.")
				del f["batch_id"]
				del f["batch_status"]
				with open(meta_filename, "w") as outfile:
					json.dump(files, outfile, indent = 4)
			else:
				print("Unkown error: " + str(batch.errors))
			
			sys.exit(0)
	
	if "batch_status" in f and not "local_output_filename" in f:
		batch = client.batches.retrieve(f["batch_id"])
		output_file = client.files.content(batch.output_file_id)
		
		output_filename = Path(f["local_filename"].replace("batch_inputs", "batch_outputs"))
		output_filename.parent.mkdir(parents = True, exist_ok = True)
		with open(output_filename, "w") as outfile:
			outfile.write(output_file.text)
		f["local_output_filename"] = str(output_filename)
		with open(meta_filename, "w") as outfile:
			json.dump(files, outfile, indent = 4)
		
		# Wait before running next batch
		time.sleep(wait_period)
