"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a(=25/16)畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (called a "ji field"), with the tongue width (舌廣) being 20 bu, the heel width (踵廣) being 5 bu, and the length (正從) being 30 bu.
Question: how large is the field?

The procedure says: Add the heel and tongue widths, then halve the sum. Multiply this by the length. Divide by the mu-divisor (240 bu² per mu) to obtain the result in mu.

The answer says: *a*(=25/16) mu.
"""

# 舌廣二十步
舌廣 = 20

# 踵廣五步
踵廣 = 5

# 正從三十步
正從 = 30

# 畝法二百四十步
畝法 = 240

# 并踵、舌而半之
平均廣 = Fraction(舌廣 + 踵廣, 2)

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一
a = Fraction(積步, 畝法) # 25/16
#----- content ends here -----

"""
"""
