"""
今有田廣一步半、三分步之一、四分步之一、五分步之一。求田一畝，問︰從幾何？
術曰：下有五分，以一為六十，半為三十，三分之一為二十，四分之一為一十五，五分之一為一十二，并之得一百三十七，以為法。置田二百四十步，亦以一為六十乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the total area of the field in terms of "步" (steps) and determine how many steps correspond to one "畝" (a traditional Chinese unit of area). Let's translate the problem into Python code.


"""


from fractions import Fraction

# Given data
田廣 = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5)  # The width of the field in fractional steps
田步 = 240  # Total length of the field in steps

# Convert the width to a common denominator and sum
分母 = 5  # The least common denominator is 60 (1/2, 1/3, 1/4, 1/5)
半步 = 30  # Half a step in terms of the denominator
三分之一步 = 20
四分之一步 = 15
五分之一步 = 12

# Sum the widths
田廣 = 半步 + 三分之一步 + 四分之一步 + 五分之一步  # Total width in terms of the denominator
法 = 田廣  # This is the divisor for the calculation

# Calculate the total area in terms of steps
實 = 田步 * 60  # Convert the length to the same unit as the width
a = Fraction(實, 法)  # Calculate the number of steps corresponding to one 畝

# Result
a


"""


The variable `a` will contain the number of steps corresponding to one 畝.
"""


"""
Variable 'a' has wrong value. Expected: 14400/137, Actual: 14400/77"""
