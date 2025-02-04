"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
術曰：冪自乘，為實。股自乘，為方法，從。開方除之，所得又開方，即句。
答曰：句 a 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
gu = Fraction(16, 1) + Fraction(1, 2)  # 股 = 16 1/2
mian = Fraction(164, 1) + Fraction(14, 25)  # 冪 = 164 14/25

# Step 1: Calculate the square of 股 (gu)
gu_squared = gu * gu

# Step 2: Divide 冪 (mian) by 股 squared
result = mian / gu_squared

# Step 3: Take the square root of the result to find 句 (ju)
a = math.sqrt(float(result))  # Convert to float for square root calculation

# Convert back to Fraction for the final result
a = Fraction(a).limit_denominator()

# The value of 句 (a) is now stored in the variable `a`
#----- content ends here -----


"""


The variable `a` contains the value of 句 (ju) as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 769101/989248"""
