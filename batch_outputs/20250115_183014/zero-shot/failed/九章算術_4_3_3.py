"""
今有田廣一步半、三分步之一、四分步之一、五分步之一。求田一畝，問︰從幾何？
術曰：下有五分，以一為六十，半為三十，三分之一為二十，四分之一為一十五，五分之一為一十二，并之得一百三十七，以為法。置田二百四十步，亦以一為六十乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
田廣 = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5)  # Sum of fractions
田一畝 = 240  # 240 steps

# Convert each fraction to a common denominator (1 step = 60 units)
田廣_in_units = 田廣 * 60  # Convert to units
田一畝_in_units = 田一畝 * 60  # Convert to units

# Calculate the number of steps
a = 田一畝_in_units / 田廣_in_units

# Result
a  # This is the number of steps


"""


The variable `a` will contain the solution in steps.
"""


"""
Variable 'a' has wrong value. Expected: 14400/137, Actual: 14400/77"""
