"""
今有竿，不知長短，度其影，得一丈五尺，別立一表，長一尺五寸，影得五寸。問：竿長幾何？
術曰：置竿影一丈五尺，以表長一尺五寸乘之，上十之，得二十二丈五尺，以表影五寸除之，即得。
答曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the length of a pole ("竿") based on the ratio of its shadow to the shadow of a smaller reference stick ("表"). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
pole_shadow = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10 丈
reference_length = Fraction(1, 1) + Fraction(5, 10)  # 1尺5寸 = 1 + 5/10 尺
reference_shadow = Fraction(5, 10)  # 5寸 = 5/10 尺

# Calculation
a = (pole_shadow * reference_length * 10) / reference_shadow  # Length of the pole in 丈

# Result
a  # Length of the pole in 丈
#----- content ends here -----


"""


This code calculates the length of the pole (`a`) in units of 丈 using the given ratios.
"""


"""
Variable 'a' has wrong value. Expected: 9/2, Actual: 45"""
