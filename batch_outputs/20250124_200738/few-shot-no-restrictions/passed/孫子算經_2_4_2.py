"""
今有粟一斗。問：為糲米幾何？
術曰：置粟一斗十升，以糲米率三十乘之，得三百升為實，以粟率五十為法，除之，即得。
答曰： a升 。
"""

#----- content starts here -----
"""
Suppose there is 1 dou of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place 1 dou of millet, which is 10 sheng. 
Multiply it by the rate for roughly husked millet, which is 30, obtaining 300 sheng as the dividend.
Use the rate for unhusked millet, which is 50, as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a* sheng.
"""

from fractions import Fraction

# 粟一斗 (1斗 = 10升)
粟 = 10  # in 升

# 糲米率 30
糲米率 = 30

# 粟率 50
粟率 = 50

# 以糲米率三十乘之，得三百升為實
實 = 粟 * 糲米率

# 以粟率五十為法，除之，即得
a = Fraction(實, 粟率)

# Output the result
a  # a升#----- content ends here -----

"""
"""
