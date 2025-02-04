"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
荅曰： a人 功。內少 b尺 。
"""

"""
To solve this problem, we need to calculate the volume of the canal and then determine how many workers are required to complete the task, given the work rate of each worker.

---

### Problem Breakdown:

1. **Canal Dimensions:**
   - Top width = 1 zhang 8 chi = 18 chi
   - Bottom width = 3 chi 6 cun = 3.6 chi
   - Depth = 1 zhang 8 chi = 18 chi
   - Length = 51,824 chi

2. **Volume Calculation:**
   The formula for the volume of a trapezoidal prism is:
   \[
   V = \text{Length} \times \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth}
   \]

3. **Worker Calculation:**
   - Total volume = 17,458,560 chi³ (as given in the problem).
   - Each worker can complete 300 chi³ of work.
   - Divide the total volume by the work rate to find the number of workers required.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Canal dimensions
top_width = 18  # in chi
bottom_width = 3.6  # in chi
depth = 18  # in chi
length = 51824  # in chi

# Volume calculation
volume = length * (top_width + bottom_width) / 2 * depth

# Verify the given volume
given_volume = 17458560  # in chi³
assert round(volume) == given_volume, "Calculated volume does not match the given volume."

# Worker calculation
work_rate_per_worker = 300  # in chi³
workers = given_volume // work_rate_per_worker  # Number of full workers
remaining_work = given_volume % work_rate_per_worker  # Remaining work in chi³

# Output results
a = workers  # Number of workers
b = remaining_work  # Remaining work in chi³

print(f"Number of workers required: {a}")
print(f"Remaining work: {b} chi³")
#----- content ends here -----


"""


---

### Explanation of Results:
- **Number of workers required (`a`)**: This is the total number of workers needed to complete the task.
- **Remaining work (`b`)**: This is the leftover work (in chi³) that cannot be completed by the last worker.


"""


"""
Code error: Calculated volume does not match the given volume."""
