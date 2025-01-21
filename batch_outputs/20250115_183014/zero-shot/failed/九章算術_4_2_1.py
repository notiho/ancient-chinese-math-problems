"""
今有田廣一步半、三分步之一、四分步之一。求田一畝，問︰從幾何？
術曰：下有四分，以一為一十二，半為六，三分之一為四，四分之一為三，并之得二十五，以為法。置田二百四十步，亦以一為一十二乘之，為實。實如法而一，得從步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
田廣 = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)  # The width of the field in steps
田一畝 = 240  # The area of the field in steps

# Convert the width into a common denominator (denominator of 12)
田廣 = Fraction(12, 12) * 田廣  # Convert to a denominator of 12
法 = 田廣  # This is the divisor (法)

# Convert the area into the same denominator (denominator of 12)
實 = Fraction(12, 12) * 田一畝  # Convert to a denominator of 12

# Calculate the length of the field (從步)
a = 實 / 法  # Divide the area by the width to get the length

# The result is stored in variable 'a'


"""


The variable `a` will contain the length of the field in steps.
"""


"""
Variable 'a' has wrong value. Expected: 576/5, Actual: 2880/13"""
