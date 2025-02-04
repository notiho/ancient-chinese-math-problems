"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal canal and determining the number of workers required to complete the task.

### Problem Breakdown:
1. The canal has the following dimensions:
   - Top width: 1丈8尺 = 18尺
   - Bottom width: 3尺6寸 = 3.6尺
   - Depth: 1丈8尺 = 18尺
   - Length: 51824尺

2. The volume of the canal is calculated using the formula for the volume of a trapezoidal prism:
   \[
   V = \frac{\text{(Top Width + Bottom Width)}}{2} \times \text{Depth} \times \text{Length}
   \]

3. Each worker can dig 300 cubic 尺 per day. We need to calculate the number of workers required to complete the task and any remainder work left.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Canal dimensions
top_width = Fraction(18)  # 1丈8尺 = 18尺
bottom_width = Fraction(3.6)  # 3尺6寸 = 3.6尺
depth = Fraction(18)  # 1丈8尺 = 18尺
length = Fraction(51824)  # Length in 尺

# Calculate the volume of the canal
volume = (top_width + bottom_width) / 2 * depth * length  # Volume in cubic 尺

# Worker capacity
worker_capacity = Fraction(300)  # Each worker can dig 300 cubic 尺

# Calculate the number of workers required
a = volume // worker_capacity  # Number of full workers required
b = volume % worker_capacity  # Remaining work in cubic 尺

# Results
a = int(a)  # Convert to integer for the number of workers
b = float(b)  # Convert to float for the remaining work in 尺

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of Variables:
- `a`: The number of workers required to complete the task.
- `b`: The remaining work in cubic 尺 after the workers have completed their full capacity.

### Final Answer:
The Python code will compute the values of `a` (number of workers) and `b` (remaining work in 尺).
"""


"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 285.6000000000414"""
