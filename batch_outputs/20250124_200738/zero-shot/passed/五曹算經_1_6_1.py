"""
今有弧田弦八十步矢五步。問：為田㡬何？
術曰：列弦八十步半之得四十步以矢五步乘之即得。
答曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the area of a circular segment (弧田). The given values are:

- 弦 (chord) = 80 steps (步)
- 矢 (sagitta or height of the arc) = 5 steps (步)

The formula provided in the problem is to take half of the chord (弦), multiply it by the sagitta (矢), and that gives the area.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
chord = 80  # 弦 in steps
sagitta = 5  # 矢 in steps

# Calculation
a = Fraction(chord, 2) * sagitta  # 半弦乘矢

# Result
a  # Area in steps²
#----- content ends here -----


"""


The variable `a` will contain the area of the circular segment in terms of steps².
"""


"""
"""
