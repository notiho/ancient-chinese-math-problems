"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (a "ji" field) where the wider side (tongue) is 20 bu, the narrower side (heel) is 5 bu, and the length (zhengcong) is 30 bu.
Question: how large is the field?

The procedure says: Add the heel and tongue, then halve it. Multiply this by the length. Divide by the mu-divisor (240), obtaining the number of mu.

Answer: *a* mu.
"""

# 舌廣二十步
舌廣 = 20

# 踵廣五步
踵廣 = 5

# 正從三十步
正從 = 30

# 并踵、舌而半之
平均廣 = (舌廣 + 踵廣) / 2

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一 (畝法為240步)
畝法 = 240
a = Fraction(積步, 畝法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
