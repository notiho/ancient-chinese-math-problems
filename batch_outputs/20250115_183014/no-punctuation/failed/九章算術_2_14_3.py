"""
今有粟七斗五升七分升之四欲為稻問得幾何
術曰以粟求稻六之五而一
荅曰為稻 a斗 
"""

"""
Suppose there are 7 dou, 5 sheng, and 7/10 of a sheng of millet. It is desired to turn it into rice.
Question: how much rice does one obtain?

The procedure says: when seeking rice from millet, multiply by 6 and divide by 5.

The answer says: it makes *a* dou of rice.
"""

from fractions import Fraction

# 粟七斗五升七分升之四
粟 = 7 * 10 + 5 + Fraction(7, 10)  # Convert to sheng (1 dou = 10 sheng)

# 以粟求稻，六之
稻 = 6 * 粟

# 五而一
稻 = Fraction(稻, 5)

# Convert back to dou
a = Fraction(稻, 10)  # 1 dou = 10 sheng
"""
Variable 'a' has wrong value. Expected: 1587/175, Actual: 2271/250"""
