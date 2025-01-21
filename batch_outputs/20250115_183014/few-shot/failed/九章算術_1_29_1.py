"""
又有箕田，舌廣一百一十七步，踵廣五十步，正從一百三十五步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

"""
Suppose there is a trapezoidal field (箕田) with the wider side (舌廣) being 117 bu, the narrower side (踵廣) being 50 bu, and the length (正從) being 135 bu.
Question: how large is the field?

The procedure says: Add the narrower side and the wider side, then halve it. Multiply this by the length. Divide by the mu-divisor (240), obtaining the number of mu.

The answer says: *a* mu.
"""

# 舌廣一百一十七步
舌廣 = 117

# 踵廣五十步
踵廣 = 50

# 正從一百三十五步
正從 = 135

# 畝法二百四十步
畝法 = 240

# 并踵、舌而半之
平均廣 = (舌廣 + 踵廣) / 2

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一
a = Fraction(積步, 畝法)
"""
Code error: both arguments should be Rational instances"""
