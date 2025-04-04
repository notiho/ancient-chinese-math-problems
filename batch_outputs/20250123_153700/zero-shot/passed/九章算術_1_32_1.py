"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a步 。
"""

"""
This problem describes a circular field (宛田) with a circumference (周) of 30 steps and a diameter (徑) of 16 steps. The area of the field is calculated using the formula given: multiply the diameter by the circumference, then divide by 4.

Here is the Python code to compute the area:


"""


from fractions import Fraction

# Given values
circumference = 30  # 周 (steps)
diameter = 16       # 徑 (steps)

# Compute the area
a = Fraction(diameter * circumference, 4)  # Divide by 4

# The result is stored in variable 'a'


"""


The area of the circular field is stored in the variable `a` as a fraction in steps².
"""


"""
"""
