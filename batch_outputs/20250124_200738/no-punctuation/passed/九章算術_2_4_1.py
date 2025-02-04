"""
今有粟一斗欲為小䵂問得幾何
術曰以粟求小䵂二十七之百而一
荅曰為小䵂 a升 
"""

#----- content starts here -----
"""
Suppose there is one dou of millet. It is desired to turn it into xiao mi (small husked rice).
Question: how much does one obtain?

The procedure says: when seeking xiao mi from millet, multiply by 27 and divide by 100.

The answer says: it makes *a* sheng of xiao mi.
"""

# 粟一斗
粟 = 1

# Convert to 升 (1 斗 = 10 升)
粟升 = 10 * 粟

# 以粟求小䵂，二十七之
小䵂 = 27 * 粟升

# 百而一
a = Fraction(小䵂, 100)#----- content ends here -----

"""
"""
