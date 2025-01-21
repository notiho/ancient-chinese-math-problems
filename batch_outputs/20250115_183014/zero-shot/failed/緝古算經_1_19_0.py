"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
術曰：冪自乘，為實。股自乘，為方法，從。開方除之，所得又開方，即句。
答曰：句 a 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a right triangle where the "股" (leg) is given, and the product of the "句" (another leg) and the hypotenuse ("弦") is also given. We need to compute the value of "句" (denoted as `a`).

Here is the Python code:


"""


from fractions import Fraction
import math

# Given values
股 = Fraction(33, 2)  # 股 = 16 1/2
冪 = Fraction(164, 25)  # 冪 = 164 14/25

# Step 1: Compute the square of 股 (leg)
股自乘 = 股 * 股

# Step 2: Compute the square of 冪 (product of 句 and 弦)
冪自乘 = 冪 * 冪

# Step 3: Subtract 股自乘 from 冪自乘
實 = 冪自乘 - 股自乘

# Step 4: Take the square root of 實 to find 句
a = math.sqrt(實)

# Result
a = Fraction(a).limit_denominator()  # Convert to Fraction for exact representation


"""


The variable `a` will contain the value of "句" (the unknown leg).
"""


"""
Code error: math domain error"""
