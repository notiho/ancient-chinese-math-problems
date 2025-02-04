"""
又有箕田舌廣一百一十七步踵廣五十步正從一百三十五步問為田幾何
術曰并踵舌而半之以乘正從畝法而一
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a Ji field (a trapezoidal field) where the tongue width (top width) is 117 bu, the heel width (bottom width) is 50 bu, and the length is 135 bu.
Question: how large is the field?

The procedure says: Add the heel and tongue widths, then halve the sum.
Multiply this by the length.
Divide by the mu-divisor, 240, to obtain the number of mu.

The answer says: *a* mu.
"""

# 舌廣一百一十七步
舌廣 = 117

# 踵廣五十步
踵廣 = 50

# 正從一百三十五步
正從 = 135

# 并踵舌而半之
平均廣 = Fraction(舌廣 + 踵廣, 2)

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一 (畝法為240)
畝法 = 240
a = Fraction(積步, 畝法)#----- content ends here -----

"""
"""
