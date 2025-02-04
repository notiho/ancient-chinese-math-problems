"""
今有箕田舌廣二十步踵廣五步正從三十步問為田幾何
術曰并踵舌而半之以乘正從畝法而一
荅曰 a畝 
"""

"""
Suppose there is a trapezoidal field (Ji Tian) where the tongue width (舌廣) is 20 bu, the heel width (踵廣) is 5 bu, and the length (正從) is 30 bu.
Question: how large is the field?

The procedure says: Add the heel and tongue, then halve it. Multiply it by the length. Divide by the mu-divisor (240), obtaining the number of mu.

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
a = Fraction(積步, 畝法)
"""
Code error: both arguments should be Rational instances"""
