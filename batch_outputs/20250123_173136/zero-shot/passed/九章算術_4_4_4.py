"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一。求田一畝，問︰從幾何？
術曰：下有六分，以一為一百二十，半為六十，三分之一為四十，四分之一為三十，五分之一為二十四，六分之一為二十，并之得二百九十四以為法。置田二百四十步，亦以一為一百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the value of "a" (the number of steps). Here's the Python code:


"""


from fractions import Fraction

# Given values
田廣 = Fraction(1, 1) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6)
田步 = 240

# Convert the unit "1" to 120 (as stated in the problem)
unit_conversion = 120

# Calculate the 法 (denominator for the calculation)
法 = 田廣 * unit_conversion

# Calculate the actual value of a (steps)
a = (田步 * unit_conversion) / 法

# The result is stored in variable "a"
a


"""


This will compute the value of "a" in steps.
"""


"""
"""
