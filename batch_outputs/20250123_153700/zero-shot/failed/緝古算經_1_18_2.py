"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction
import math

# Given values
mian = 726  # 冪 (the product of 股 and 弦)
ju = Fraction(7, 10)  # 句 (the given value of the other side)

# Step 1: Square the given 句 (ju)
ju_squared = ju ** 2

# Step 2: Divide 冪 (mian) by the squared 句 (ju_squared)
result = mian / ju_squared

# Step 3: Take the square root of the result to find 股 (a)
a = math.sqrt(result)

# 股 (a) is the answer
a


"""


The variable `a` will contain the value of 股 after the computation.
"""


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 38.491981672307084"""
