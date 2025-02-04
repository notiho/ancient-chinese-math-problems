"""
今有粟一斗。問：為糲米幾何？
術曰：置粟一斗十升，以糲米率三十乘之，得三百升為實，以粟率五十為法，除之，即得。
答曰： a(=6)升 。
"""

#----- content starts here -----
"""
Suppose there is one dou of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place 1 dou as 10 sheng.
Multiply it by the rate for roughly husked millet, 30, obtaining 300 sheng as the dividend.
Use the rate for unhusked millet, 50, as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a*(=6) sheng.
"""

# 粟一斗十升
粟 = 10

# 糲米率三十
糲米率 = 30

# 以糲米率三十乘之，得三百升為實
實 = 粟 * 糲米率

# 粟率五十為法
粟率 = 50

# 除之，即得
a = Fraction(實, 粟率) # 6#----- content ends here -----

"""
"""
