"""
今有粟一斗，欲為小䵂。問︰得幾何？
荅曰：為小䵂 a升 。
"""

"""
Suppose there is 1 dou of millet. It is desired to turn it into "small xiao" (a processed form of millet).
Question: how much does one obtain?

The answer says: it makes *a* sheng of "small xiao."
"""

# 粟一斗
粟 = 1  # 1 dou

# Convert dou to sheng (1 dou = 10 sheng)
粟_in_sheng = 10 * 粟

# To process into "small xiao," multiply by 2/3
a = Fraction(2 * 粟_in_sheng, 3)

# Result
a
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 20/3"""
