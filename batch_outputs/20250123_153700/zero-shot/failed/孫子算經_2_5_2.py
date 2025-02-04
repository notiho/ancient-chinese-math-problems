"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
粟數 = Fraction(21)  # 粟數 is 21升 (2斗1升 = 21升)
粺米率 = Fraction(27)  # 粺米率 is 27
粟率 = Fraction(50)  # 粟率 is 50

# Calculation
實 = 粟數 * 粺米率  # 實 = 粟數 × 粺米率
a = 實 / 粟率  # a = 實 ÷ 粟率

# Result
a  # a斗


"""


The variable `a` will hold the result in terms of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
