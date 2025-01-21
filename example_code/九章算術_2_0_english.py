#今有粟一斗，欲為糲米。問︰得幾何？

#荅曰：為糲米 a升 。

"""
Suppose there is one dou of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

The answer says: *a* sheng of roughly unhusked millet.
"""

# 粟一斗
粟 = 1

# Convert to sheng
粟 = 10 * 粟

# Multiply by 3 and divide by 5 to get husked millet
a = Fraction(3 * 粟, 5)
