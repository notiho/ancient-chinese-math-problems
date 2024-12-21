#今有粟一斗欲爲糲米問得幾何
#術曰以粟求糲米三之五而一
#荅曰爲糲米 a升

"""
Suppose there is one dou of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

The procedure says: when seeking roughly husked millet with husked millet, multiply by 3 and divide by 5.

The answer says: *a* sheng of roughly unhusked millet.
"""

# 粟一斗
粟 = 1

# Convert to 升
粟 = 10 * 粟

# 以粟求糲米三之
糲米 = 3 * 粟

# 五而一
a = Fraction(糲米, 5)
