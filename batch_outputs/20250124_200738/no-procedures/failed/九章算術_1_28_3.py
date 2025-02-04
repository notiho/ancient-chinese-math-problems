"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田). The top width (舌廣) is 20 bu, the bottom width (踵廣) is 5 bu, and the length (正從) is 30 bu.
Question: how large is the field?

Answer: it is *a* mu.
"""

# 舌廣 (top width)
舌廣 = 20

# 踵廣 (bottom width)
踵廣 = 5

# 正從 (length)
正從 = 30

# Calculate the area in square bu using the formula for the area of a trapezoid: (top + bottom) * height / 2
area_in_bu = (舌廣 + 踵廣) * 正從 / 2

# Convert the area from square bu to mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

a  # The area in mu#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
