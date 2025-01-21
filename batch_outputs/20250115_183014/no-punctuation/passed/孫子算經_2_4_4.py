"""
今有粟一斗問為糲米幾何
術曰置粟一斗十升以糲米率三十乘之得三百升為實以粟率五十為法除之即得
答曰 a升 
"""

"""
Suppose there is one dou of millet. 
Question: how much roughly husked millet does it make?

The procedure says: Place 1 dou of millet, which is 10 sheng.
Multiply it by the rate for roughly husked millet, 30, obtaining 300 sheng as the dividend.
Take the millet rate, 50, as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* sheng.
"""

# 粟一斗十升
粟 = 10

# 糲米率三十
糲米率 = 30

# 以糲米率三十乘之，得三百升為實
實 = 粟 * 糲米率

# 粟率五十為法
粟率 = 50

# 除之即得
a = Fraction(實, 粟率)
"""
"""
