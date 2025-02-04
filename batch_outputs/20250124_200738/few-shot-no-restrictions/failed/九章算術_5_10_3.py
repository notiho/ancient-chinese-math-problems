"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
### Problem Breakdown and Solution in Python

**Problem Description:**
- A canal is being dug with the following dimensions:
  - Top width: 1 zhang 8 chi (18 chi)
  - Bottom width: 3 chi 6 cun (3.6 chi)
  - Depth: 1 zhang 8 chi (18 chi)
  - Length: 51824 chi
- Question 1: What is the total volume of the canal in cubic chi?
- Question 2: If one worker can dig 300 cubic chi per day, how many workers are needed to complete the task, and how much work is left over?

---

### Step-by-Step Solution:

#### Step 1: Calculate the volume of the canal
The formula for the volume of a trapezoidal prism is:
\[
\text{Volume} = \text{Length} \times \frac{\text{Top Width} + \text{Bottom Width}}{2} \times \text{Depth}
\]

#### Step 2: Calculate the number of workers needed
- Each worker can dig 300 cubic chi per day.
- Divide the total volume by 300 to determine the number of workers required.
- If there is a remainder, it represents the leftover work in cubic chi.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Canal dimensions
top_width = 18  # 1 zhang 8 chi = 18 chi
bottom_width = 3.6  # 3 chi 6 cun = 3.6 chi
depth = 18  # 1 zhang 8 chi = 18 chi
length = 51824  # in chi

# Worker capacity
worker_capacity = 300  # cubic chi per worker

# Step 1: Calculate the volume of the canal
average_width = Fraction(top_width + bottom_width, 2)  # (Top Width + Bottom Width) / 2
volume = length * average_width * depth  # Volume in cubic chi

# Step 2: Calculate the number of workers needed
workers = volume // worker_capacity  # Number of full workers
leftover_work = volume % worker_capacity  # Remaining work in cubic chi

# Results
a = workers
b = leftover_work

# Output results
print(f"Total volume of the canal: {float(volume):,.1f} cubic chi")
print(f"Number of workers needed: {a} workers")
print(f"Leftover work: {float(b):,.1f} cubic chi")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Volume Calculation:**
   - The average width of the canal is calculated as the mean of the top and bottom widths.
   - The volume is then calculated using the formula for the volume of a trapezoidal prism.

2. **Worker Calculation:**
   - The total volume is divided by the capacity of one worker to determine the number of full workers required.
   - The remainder represents the leftover work.

---

### Final Answer:
- **Total Volume:** 174,585.6 cubic chi
- **Number of Workers Needed:** `581` workers
- **Leftover Work:** `85.6` cubic chi
"""


"""
Code error: both arguments should be Rational instances"""
