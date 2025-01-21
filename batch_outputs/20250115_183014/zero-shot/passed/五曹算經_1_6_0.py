"""
今有弧田弦八十步矢五步。問：為田㡬何？
術曰：列弦八十步半之得四十步以矢五步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular segment (弧田). The formula provided in the problem is to take half of the chord (弦) and multiply it by the height (矢). Here's the Python code:


"""


from fractions import Fraction

# Given values
chord = 80  # 弦 in 步
height = 5  # 矢 in 步

# Calculation
half_chord = Fraction(chord, 2)  # 半弦
a = half_chord * height  # Area of the segment in 步

# Result
a  # The area in 步


"""


The solution is stored in the variable `a`.
"""


"""
"""
