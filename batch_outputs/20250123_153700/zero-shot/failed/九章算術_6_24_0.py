"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
術曰：置發、耕、耰畝數，令互乘人數，并以為法。畝數相乘為實。實如法得一畝。
荅曰： a畝 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating how much land one person can manage in one day if they perform all three tasks (plowing, tilling, and sowing) themselves. The tasks have different rates of completion per day.

Here is the Python code:


"""


from fractions import Fraction

# Rates of work per day
plowing_rate = 7  # 7 畝 per day
tilling_rate = 3  # 3 畝 per day
sowing_rate = 5   # 5 畝 per day

# Multiply the rates together
numerator = plowing_rate * tilling_rate * sowing_rate

# Add the rates together
denominator = plowing_rate + tilling_rate + sowing_rate

# Calculate the amount of land one person can manage in one day
a = Fraction(numerator, denominator)

# Result
a  # The answer is in 畝


"""


The variable `a` will contain the solution in terms of 畝 (mu), which is the unit of land area in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 105/71, Actual: 7"""
