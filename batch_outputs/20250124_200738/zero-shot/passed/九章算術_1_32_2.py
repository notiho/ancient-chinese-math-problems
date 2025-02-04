"""
今有宛田，下周三十步，徑十六步。問：為田幾何？
術曰：以徑乘周，四而一。
荅曰： a步 。
"""

"""
This problem describes a circular field where the circumference (周) is 30 steps and the diameter (徑) is 16 steps. The formula provided suggests that the area of the field is calculated as `(diameter * circumference) / 4`.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
diameter = 16  # 徑 in steps
circumference = 30  # 周 in steps

# Calculate the area
a = Fraction(diameter * circumference, 4)  # a = (diameter * circumference) / 4

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will represent the area of the field in square steps.
"""


"""
"""
