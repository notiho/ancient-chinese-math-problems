"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
### Problem Breakdown and Solution in Python

#### Problem Description:
1. **Volume Calculation**:
   - A trench has the following dimensions:
     - Top width: 1 zhang 6 chi 3 cun (1丈6尺3寸)
     - Bottom width: 1 zhang (1丈)
     - Depth: 6 chi 3 cun (6尺3寸)
     - Length: 13 zhang 2 chi 1 cun (13丈2尺1寸)
   - Question: What is the total volume of the trench?

2. **Labor Calculation**:
   - A worker can dig 871 cubic chi (871尺) of soil.
   - Adjustments:
     - 1/5 of the work is for removing soil (出土功).
     - Half of the remaining work is for handling gravel, sand, and stones (沙礫水石之功).
   - Question: How many workers are required to dig the trench?

---

### Step 1: Volume Calculation

The trench is trapezoidal in cross-section. The formula for the volume of a trapezoidal prism is:

\[
\text{Volume} = \text{Length} \times \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth}
\]

Convert all dimensions to **chi (尺)** for consistency:
- 1 zhang (丈) = 10 chi (尺)
- 1 chi (尺) = 10 cun (寸)

---

### Step 2: Labor Calculation

The number of workers required is calculated as follows:
1. Adjust the worker's capacity:
   - Subtract 1/5 for soil removal.
   - Subtract half of the remaining capacity for handling gravel, sand, and stones.
2. Divide the total trench volume by the adjusted worker capacity.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Volume Calculation
# Convert dimensions to chi (尺)
top_width = 1 * 10 + 6 + Fraction(3, 10)  # 1丈6尺3寸
bottom_width = 1 * 10  # 1丈
depth = 6 + Fraction(3, 10)  # 6尺3寸
length = 13 * 10 + 2 + Fraction(1, 10)  # 13丈2尺1寸

# Calculate the volume of the trench
average_width = (top_width + bottom_width) / 2
volume = length * average_width * depth

# Step 2: Labor Calculation
# Worker capacity adjustments
worker_capacity = 871  # 本人功
soil_removal = Fraction(1, 5) * worker_capacity  # 出土功 (1/5)
remaining_capacity = worker_capacity - soil_removal
gravel_work = Fraction(1, 2) * remaining_capacity  # 沙礫水石之功 (1/2)
adjusted_capacity = remaining_capacity - gravel_work  # Final adjusted capacity

# Calculate the number of workers required
workers = volume / adjusted_capacity

# Results
a = workers
print(f"Trench Volume: {volume} cubic chi")
print(f"Number of Workers Required: {a} people")
#----- content ends here -----


"""


---

### Explanation of Results:
1. **Trench Volume**:
   - The total volume of the trench is calculated in cubic chi (尺³).

2. **Number of Workers**:
   - The number of workers required is calculated based on the adjusted worker capacity.

---

### Final Answer:
- Trench Volume: 10,943.8 cubic chi (尺³)
- Number of Workers: *a* people (calculated value).
"""


"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/696800"""
