import sys
import random
import shutil
from pathlib import Path
from collections import Counter

n = 50

base_dir = Path(sys.argv[1])

target_dir = Path("error_analysis") / "/".join(base_dir.parts[-2:])
target_dir.mkdir(parents = True)

random.seed(1234)

candidate_files = sorted((base_dir / "failed").glob("*.py"))
candidate_problems = Counter("_".join(i.stem.split("_")[:3]) for i in candidate_files)
candidate_problems = sorted(i for i, c in candidate_problems.most_common() if c == 5)

selection = random.sample(candidate_problems, n)

for s in selection:
	possible_files = [f for f in candidate_files if f.stem.startswith(s + "_")]
	shutil.copy(random.choice(possible_files), target_dir)
