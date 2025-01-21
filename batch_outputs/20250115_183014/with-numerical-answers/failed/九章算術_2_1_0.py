"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a(=567/500)斗 。
"""

"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much does one obtain?

The procedure says: when seeking polished millet with unhusked millet, multiply by 27 and divide by 50.

The answer says: *a*(=567/500) dou of polished millet.
"""

# 粟二斗一升
粟斗 = 2
粟升 = 1

# Convert to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求粺米，二十七之
粺米 = 27 * 粟

# 五十而一
a = Fraction(粺米, 50) # 567/500 (in dou)
"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
