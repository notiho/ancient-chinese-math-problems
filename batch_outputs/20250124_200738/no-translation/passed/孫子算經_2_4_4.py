"""
今有粟一斗。問：為糲米幾何？
術曰：置粟一斗十升，以糲米率三十乘之，得三百升為實，以粟率五十為法，除之，即得。
答曰： a升 。
"""

#----- content starts here -----

# 置粟一斗十升
粟 = 10  # 一斗等於十升

# 以糲米率三十乘之，得三百升為實
糲米率 = 30
實 = 粟 * 糲米率

# 以粟率五十為法
粟率 = 50
法 = 粟率

# 除之，即得
a = Fraction(實, 法)#----- content ends here -----

"""
"""
