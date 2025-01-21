"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
去閫 = Fraction(1, 10)  # 1 尺 = 1/10 丈
不合 = Fraction(2, 100)  # 2 寸 = 2/100 丈

# Calculation
門廣 = (去閫 ** 2 / 不合 + 不合 / 2)

# Result
a = 門廣  # 門廣 is the width of the door in 丈


"""


The variable `a` will hold the value of the door's width in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 51/100"""
