"""
今有田廣一步半、三分步之一、四分步之一。求田一畝，問︰從幾何？
術曰：下有四分，以一為一十二，半為六，三分之一為四，四分之一為三，并之得二十五，以為法。置田二百四十步，亦以一為一十二乘之，為實。實如法而一，得從步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the number of steps ("a") required to form one "畝" (a unit of area) based on the given dimensions of the field.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
field_width = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)  # Field width in steps
field_area = 240  # Total area in steps

# Convert the width to a denominator of 12 (common denominator)
field_width_in_twelfths = Fraction(1, 2) * 12 + Fraction(1, 3) * 12 + Fraction(1, 4) * 12

# Calculate the number of steps required for one 畝
a = Fraction(field_area * 12, field_width_in_twelfths)

# Result
a
#----- content ends here -----


"""


This code calculates the value of "a" in steps. The result will be stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 576/5, Actual: 2880/13"""
