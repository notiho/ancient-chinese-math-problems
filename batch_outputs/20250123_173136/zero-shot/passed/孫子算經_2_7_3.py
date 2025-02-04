"""
今有粟七斗九升。問：為御米幾何？
術曰：置七斗九升以御米率二十一乘之，得一千六百五十九，為實，以粟率五十除之，即得。
答曰： a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
粟 = Fraction(7, 1) + Fraction(9, 10)  # 7斗9升 = 7 + 9/10 斗
御米率 = Fraction(21, 1)  # 御米率 = 21
粟率 = Fraction(50, 1)  # 粟率 = 50

# Calculation
實 = 粟 * 御米率  # 實 = 粟 × 御米率
a = 實 / 粟率  # a = 實 ÷ 粟率

# Result
a斗 = a  # Answer in 斗


"""


The variable `a斗` will contain the result in the unit of "斗".
"""


"""
"""
