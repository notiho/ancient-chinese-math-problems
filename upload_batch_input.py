import sys
import json
import tqdm
from pathlib import Path
from glob import glob
from openai import OpenAI

directory = sys.argv[1]

client = OpenAI()

meta_filename = Path(directory) / "index.json"

assert not meta_filename.is_file()

files = []

for filename in tqdm.tqdm(glob(directory + "/*/*.jsonl")):
    f = client.files.create(
        file = open(filename, "rb"),
        purpose = "batch"
    )
    files.append({"id": f.id, "local_filename": filename})

with open(meta_filename, "w") as outfile:
    json.dump(files, outfile, indent = 4)
