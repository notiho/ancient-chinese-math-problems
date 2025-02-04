"""
又有箕田，舌廣一百一十七步，踵廣五十步，正從一百三十五步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田). The top width (舌廣) is 117 bu, the bottom width (踵廣) is 50 bu, and the length (正從) is 135 bu.
Question: how large is the field?

Answer: it makes *a* mu.
"""

# 舌廣
舌廣 = 117

# 踵廣
踵廣 = 50

# 正從
正從 = 135

# Area of a trapezoid: (top width + bottom width) * length / 2
area_in_bu = (舌廣 + 踵廣) * 正從 / 2

# Convert to mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

a  # Output the result in mu#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
