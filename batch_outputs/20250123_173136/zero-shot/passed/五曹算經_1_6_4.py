"""
今有弧田弦八十步矢五步。問：為田㡬何？
術曰：列弦八十步半之得四十步以矢五步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular segment (弧田). The formula provided in the problem is to take half the chord length (弦) and multiply it by the height (矢).

Here is the Python code:


"""


from fractions import Fraction

# Given values
chord_length = 80  # 弦 in 步
height = 5         # 矢 in 步

# Calculation
a = Fraction(chord_length, 2) * height  # 半弦乘以矢

# Result
a  # Area of the field in 步


"""


The solution is stored in the variable `a`, which represents the area of the field in 步.
"""


"""
"""
