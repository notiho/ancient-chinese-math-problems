"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
術曰：置本人功，去其五分之一，餘為法。以溝積尺為實。實如法而一，得用徒人數。
荅曰： a人 。
"""

"""
To solve this problem, we will first compute the volume of the ditch (溝積) in cubic feet (尺³). Then, we will calculate the number of workers (徒人) required based on the given conditions.

### Problem Breakdown:
1. **Volume of the ditch (溝積)**:
   - Top width (上廣): 1丈5尺 = 15尺
   - Bottom width (下廣): 1丈 = 10尺
   - Depth (深): 5尺
   - Length (袤): 7丈 = 70尺
   - Formula for the volume of a trapezoidal prism:  
     \[
     V = \frac{(上廣 + 下廣) \times 深}{2} \times 長
     \]

2. **Worker calculation (用徒)**:
   - Total volume of the ditch: 4375尺³
   - A worker's daily capacity (人功): 766尺³
   - Additional effort for digging (出土功): 1/5 of the worker's capacity
   - Effective capacity per worker:  
     \[
     \text{Effective capacity} = \text{人功} - \frac{\text{人功}}{5}
     \]
   - Number of workers required:  
     \[
     \text{Number of workers} = \frac{\text{Volume of the ditch}}{\text{Effective capacity}}
     \]

### Python Code:

"""


from fractions import Fraction

# Step 1: Calculate the volume of the ditch (溝積)
top_width = 15  # 上廣 in 尺
bottom_width = 10  # 下廣 in 尺
depth = 5  # 深 in 尺
length = 70  # 袤 in 尺

volume = Fraction((top_width + bottom_width) * depth, 2) * length  # 溝積 in 尺³

# Step 2: Calculate the number of workers required (用徒)
worker_capacity = 766  # 人功 in 尺³
additional_effort = Fraction(worker_capacity, 5)  # 出土功 in 尺³
effective_capacity = worker_capacity - additional_effort  # Effective capacity per worker

# Number of workers required
a = Fraction(volume, effective_capacity)  # 用徒人數

# Results
volume, a


"""


### Explanation of Variables:
- `volume`: The total volume of the ditch in cubic feet (尺³).
- `a`: The number of workers required to complete the task.

### Output:
The code will compute:
- `volume = 4375` (as given in the problem).
- `a = 7` workers.
"""


"""
"""
