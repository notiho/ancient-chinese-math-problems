"""
又有箕田，舌廣一百一十七步，踵廣五十步，正從一百三十五步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a(=1503/32)畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (called a "ji field") with the tongue width (舌廣) of 117 bu, the heel width (踵廣) of 50 bu, and the length (正從) of 135 bu.
Question: how large is the field?

The procedure says: Add the heel and tongue widths and halve them. Multiply this by the length.
Divide by the mu-divisor (畝法), obtaining the number of mu.

Answer: *a*(=1503/32) mu.
"""

from fractions import Fraction

# 舌廣一百一十七步
舌廣 = 117

# 踵廣五十步
踵廣 = 50

# 正從一百三十五步
正從 = 135

# 畝法二百四十步
畝法 = 240

# 并踵、舌而半之
平均廣 = Fraction(舌廣 + 踵廣, 2)

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一
a = Fraction(積步, 畝法)  # 1503/32#----- content ends here -----

"""
"""
