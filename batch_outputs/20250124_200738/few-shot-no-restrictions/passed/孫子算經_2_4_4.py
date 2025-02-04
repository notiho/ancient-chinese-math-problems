"""
今有粟一斗。問：為糲米幾何？
術曰：置粟一斗十升，以糲米率三十乘之，得三百升為實，以粟率五十為法，除之，即得。
答曰： a升 。
"""

#----- content starts here -----
"""
Suppose there is one dou of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place the unhusked millet as 1 dou, which is 10 sheng.
Multiply it by the rate of roughly husked millet, which is 30, obtaining 300 sheng as the dividend.
Use the rate of unhusked millet, which is 50, as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* sheng.
"""

from fractions import Fraction

# 粟一斗 (1斗 = 10升)
粟 = 10  # in 升

# 糲米率 (rate for 糲米)
糲米率 = 30

# 粟率 (rate for 粟)
粟率 = 50

# 以糲米率三十乘之，得三百升為實
實 = 粟 * 糲米率

# 以粟率五十為法，除之，即得
a = Fraction(實, 粟率)

# Answer
a  # in 升#----- content ends here -----

"""
"""
