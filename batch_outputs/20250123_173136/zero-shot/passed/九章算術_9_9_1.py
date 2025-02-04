"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
去閫 = Fraction(1, 10)  # 去閫一尺 = 1/10 丈
不合 = Fraction(2, 100)  # 不合二寸 = 2/100 丈

# Calculation
門廣 = (去閫 ** 2 / (不合 / 2)) + (不合 / 2)

# Answer
a = 門廣  # The width of the door in 丈


"""


The variable `a` will hold the width of the door in 丈.
"""


"""
"""
