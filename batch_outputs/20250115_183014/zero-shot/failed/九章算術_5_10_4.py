"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the step-by-step solution:

1. **Understanding the problem**:
   - The canal has a trapezoidal cross-section with:
     - Top width = 1丈8尺 = 18尺
     - Bottom width = 3尺6寸 = 3.6尺
     - Depth = 1丈8尺 = 18尺
   - Length = 51824尺
   - The volume of the canal is calculated using the formula for the volume of a trapezoidal prism:
     \[
     V = \frac{(上廣 + 下廣)}{2} \times 深 \times 長
     \]
   - The volume is given as 174585尺6寸 = 174585.6尺³.

   - A worker can dig 300尺³ per day. We need to calculate how many workers are required (`a`) and how much work is left (`b`).

2. **Python code**:


"""


from fractions import Fraction

# Given dimensions of the canal
top_width = Fraction(18)  # 1丈8尺 = 18尺
bottom_width = Fraction(3.6)  # 3尺6寸 = 3.6尺
depth = Fraction(18)  # 1丈8尺 = 18尺
length = Fraction(51824)  # 51824尺

# Calculate the volume of the canal
average_width = (top_width + bottom_width) / 2  # (上廣 + 下廣) / 2
volume = average_width * depth * length  # Volume formula

# Worker capacity
worker_capacity = Fraction(300)  # Each worker can dig 300尺³

# Calculate the number of workers required and the leftover work
a = volume // worker_capacity  # Number of workers (integer division)
b = volume % worker_capacity  # Remaining work (modulus)

# Results
a, b


"""


3. **Explanation of the code**:
   - The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values.
   - The volume of the canal is calculated using the formula for the volume of a trapezoidal prism.
   - The number of workers (`a`) is determined by dividing the total volume by the capacity of one worker (integer division).
   - The leftover work (`b`) is calculated using the modulus operator.

4. **Output**:
   - `a` represents the number of workers required.
   - `b` represents the leftover work in 尺³.
"""


"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 40194626674287507/140737488355328"""
