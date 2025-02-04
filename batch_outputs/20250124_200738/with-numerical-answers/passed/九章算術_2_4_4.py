"""
今有粟一斗，欲為小䵂。問︰得幾何？
術曰：以粟求小䵂，二十七之，百而一。
荅曰：為小䵂 a(=27/10)升 。
"""

#----- content starts here -----
"""
Suppose there is one dou of millet. It is desired to turn it into xiaoqu (a type of processed grain).
Question: how much does one obtain?

The procedure says: when seeking xiaoqu from millet, multiply by 27 and divide by 100.

The answer says: *a*(=27/10) sheng of xiaoqu.
"""

# 粟一斗
粟 = 1

# Convert to 升 (1 斗 = 10 升)
粟 = 10 * 粟

# 以粟求小䵂，二十七之
小䵂 = 27 * 粟

# 百而一
a = Fraction(小䵂, 100) # 27/10#----- content ends here -----

"""
"""
