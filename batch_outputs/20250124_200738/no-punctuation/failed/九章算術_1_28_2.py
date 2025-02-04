"""
今有箕田舌廣二十步踵廣五步正從三十步問為田幾何
術曰并踵舌而半之以乘正從畝法而一
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (Ji Tian) with the top width (舌廣) being 20 bu, the bottom width (踵廣) being 5 bu, and the length (正從) being 30 bu.
Question: how large is the field?

The procedure says: Add the bottom width and the top width, then halve it. Multiply it by the length. Divide by the mu-divisor, 240, to get the number of mu.

The answer says: *a* mu.
"""

# 舌廣二十步
舌廣 = 20

# 踵廣五步
踵廣 = 5

# 正從三十步
正從 = 30

# 并踵舌而半之
平均廣 = (舌廣 + 踵廣) / 2

# 以乘正從
積步 = 平均廣 * 正從

# 畝法二百四十步
畝法 = 240

# 畝法而一
a = Fraction(積步, 畝法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
