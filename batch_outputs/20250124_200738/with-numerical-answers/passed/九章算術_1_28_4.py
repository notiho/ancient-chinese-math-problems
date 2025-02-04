"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a(=25/16)畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田) with the top width (舌廣) of 20 bu, the bottom width (踵廣) of 5 bu, and the length (正從) of 30 bu.
Question: how large is the field?

The procedure says: Add the bottom width and the top width, then halve it. Multiply this by the length. Divide by the mu-divisor (240) to obtain the number of mu.

The answer says: *a*(=25/16) mu.
"""

# 舌廣二十步
舌廣 = 20

# 踵廣五步
踵廣 = 5

# 正從三十步
正從 = 30

# 并踵、舌而半之
平均廣 = Fraction(舌廣 + 踵廣, 2)

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一
畝法 = 240
a = Fraction(積步, 畝法) # 25/16#----- content ends here -----

"""
"""
