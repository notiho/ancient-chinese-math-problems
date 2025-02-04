"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
荅曰： a人 功。內少 b尺 。
"""

"""
To solve this problem, we need to calculate the volume of the canal and then determine how many workers are needed based on their daily work capacity.

---

### Step 1: Calculate the volume of the canal
The canal has a trapezoidal cross-section:
- Top width = 1 zhang 8 chi = 18 chi
- Bottom width = 3 chi 6 cun = 3.6 chi
- Depth = 1 zhang 8 chi = 18 chi
- Length = 51824 chi

The formula for the volume of a trapezoidal prism is:
\[
\text{Volume} = \text{Length} \times \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth}
\]

---

### Step 2: Calculate the number of workers needed
Each worker can dig **300 chi³** per day. To find the number of workers:
\[
\text{Workers Needed} = \frac{\text{Volume}}{300}
\]
If the volume is not perfectly divisible by 300, there will be some remainder.

---

### Python Code:


"""


from fractions import Fraction

# Canal dimensions
top_width = 18  # chi
bottom_width = 3 + Fraction(6, 10)  # 3 chi 6 cun = 3.6 chi
depth = 18  # chi
length = 51824  # chi

# Calculate the volume of the canal
volume = length * (top_width + bottom_width) / 2 * depth

# Convert volume to chi³
volume_in_chi_cubed = volume

# Worker capacity
worker_capacity = 300  # chi³ per worker

# Calculate the number of workers needed
workers_needed = volume_in_chi_cubed // worker_capacity
remaining_volume = volume_in_chi_cubed % worker_capacity

# Output results
a = workers_needed  # Number of workers
b = remaining_volume  # Remaining volume in chi³

# Print results
print(f"Volume of the canal: {volume_in_chi_cubed} chi³")
print(f"Workers needed: {a} workers")
print(f"Remaining volume: {b} chi³")


"""


---

### Explanation of Results:
1. **Volume of the canal**: The total volume of the canal is calculated based on its trapezoidal cross-section and length.
2. **Workers needed**: The total number of workers is determined by dividing the volume by the capacity of each worker (300 chi³/day).
3. **Remaining volume**: If the volume is not perfectly divisible by 300, the remainder represents the volume that is left after assigning full tasks to the workers.


"""


"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 1428/5"""
