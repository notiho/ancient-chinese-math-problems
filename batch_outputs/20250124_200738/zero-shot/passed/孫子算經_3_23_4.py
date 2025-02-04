"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
shadow_of_pole = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10 丈
height_of_stick = Fraction(1, 10) + Fraction(5, 100)  # 1尺5寸 = 1/10 + 5/100 丈
shadow_of_stick = Fraction(5, 100)  # 5寸 = 5/100 丈

# Calculation
a = (shadow_of_pole * height_of_stick) / shadow_of_stick

# The length of the pole (竿長)
a  # Result in 丈
#----- content ends here -----


"""


This code calculates the length of the pole (`a`) in 丈 using the given proportions.
"""


"""
"""
