"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

"""
To translate the ancient Chinese math problem into Python code, we will compute the value of the unknown `a` (the width of the door). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
去閫 = Fraction(1, 10)  # 去閫一尺 = 1/10 丈
不合 = Fraction(2, 100)  # 不合二寸 = 2/100 丈

# Calculation
step1 = 去閫 ** 2  # 去閫一尺自乘
step2 = step1 / 不合  # 所得，以不合二寸半之而一
step3 = step2 + (不合 / 2)  # 所得，增不合之半

# The width of the door
a = step3

# Result
a  # a is the width of the door in 丈
#----- content ends here -----


"""


The variable `a` will contain the width of the door in 丈 as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 51/100"""
