"""
今有田廣一步半、三分步之一、四分步之一、五分步之一。求田一畝，問︰從幾何？
術曰：下有五分，以一為六十，半為三十，三分之一為二十，四分之一為一十五，五分之一為一十二，并之得一百三十七，以為法。置田二百四十步，亦以一為六十乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the number of steps (`a`) in a field based on the given fractions of a step.

Here is the Python code:


"""


from fractions import Fraction

# Given values
field_area = 240  # in steps
one_step = 60  # converting one step to smaller units

# Fractions of a step
half_step = Fraction(1, 2) * one_step
third_step = Fraction(1, 3) * one_step
fourth_step = Fraction(1, 4) * one_step
fifth_step = Fraction(1, 5) * one_step

# Sum of the fractions
total_fraction = half_step + third_step + fourth_step + fifth_step

# Calculate the number of steps (a)
a = Fraction(field_area * one_step, total_fraction)

# Output the result
a


"""


### Explanation:
1. Each fraction of a step is converted into smaller units (`one_step = 60`).
2. The fractions are summed up to get the total fraction (`total_fraction`).
3. The total field area (`field_area = 240`) is multiplied by `one_step` to get the total area in smaller units.
4. The number of steps (`a`) is calculated by dividing the total area by the total fraction.

### Solution:
The variable `a` will contain the number of steps in the field.
"""


"""
Variable 'a' has wrong value. Expected: 14400/137, Actual: 14400/77"""
