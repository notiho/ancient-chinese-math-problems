"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
術曰：并三廣，以深乘之，又以袤乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the volume of a frustum-like shape. The formula provided in the problem is:

1. Add the three widths (下廣, 上廣, 末廣).
2. Multiply the sum by the depth (深).
3. Multiply the result by the length (袤).
4. Divide the final result by 6.

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(6)  # 下廣 (6尺)
upper_width = Fraction(10)  # 上廣 (1丈 = 10尺)
end_width = Fraction(8)  # 末廣 (8尺)
depth = Fraction(3)  # 深 (3尺)
length = Fraction(7)  # 袤 (7尺)

# Compute the volume
a = (lower_width + upper_width + end_width) * depth * length / Fraction(6)

# The result is stored in variable 'a'
a  # Volume in cubic 尺


"""


The variable `a` will contain the computed volume in cubic 尺.
"""


"""
"""
