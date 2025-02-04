"""
今有粟一斗。問：為糲米幾何？
術曰：置粟一斗十升，以糲米率三十乘之，得三百升為實，以粟率五十為法，除之，即得。
答曰： a升 。
"""

"""
Suppose there is one dou of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place 1 dou as 10 sheng. Multiply it by the rate for roughly husked millet, which is 30, obtaining 300 sheng as the dividend. Divide it by the rate for unhusked millet, which is 50, as the divisor. The result is the answer.

Answer: *a* sheng.
"""

from fractions import Fraction

# 置粟一斗十升
粟 = 10  # 1斗 = 10升

# 以糲米率三十乘之，得三百升為實
糲米率 = 30
實 = 粟 * 糲米率

# 以粟率五十為法
粟率 = 50
法 = 粟率

# 除之，即得
a = Fraction(實, 法)  # a升
"""
"""
