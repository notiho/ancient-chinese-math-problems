"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

#----- content starts here -----

# 置粟一千一粒為實
實 = 1100

# 雛啄一，母啄二，翁啄四
雛啄 = 1
母啄 = 2
翁啄 = 4

# 副并三雞所啄粟七粒為法
法 = 雛啄 + 母啄 + 翁啄

# 除之，得一百四十三粒為雞雛主所償之數
a = Fraction(實, 法)

# 遞倍之，即得母、翁主所償之數
b = 2 * a
c = 4 * a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
