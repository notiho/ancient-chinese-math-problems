"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a trapezoidal field (箕田). The width of the top (舌廣) is 20 bu, the width of the bottom (踵廣) is 5 bu, and the length (正從) is 30 bu.
Question: how large is the field?

Answer: *a* mu.
"""

from fractions import Fraction

# 舌廣 (top width)
舌廣 = 20

# 踵廣 (bottom width)
踵廣 = 5

# 正從 (length)
正從 = 30

# Area of a trapezoid = (top width + bottom width) * length / 2
area_in_bu = (舌廣 + 踵廣) * 正從 / 2

# Convert bu^2 to mu (1 mu = 240 bu^2)
a = Fraction(area_in_bu, 240)

# Output the result
a
"""
Code error: both arguments should be Rational instances"""
