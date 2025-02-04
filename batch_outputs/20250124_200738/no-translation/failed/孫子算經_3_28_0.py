"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

#----- content starts here -----

# 粟一千一粒
粟 = 1100

# 雛啄一，母啄二，翁啄四
雛啄 = 1
母啄 = 2
翁啄 = 4

# 副并三雞所啄粟七粒為法
法 = 雛啄 + 母啄 + 翁啄

# 置粟一千一粒為實，除之
雛償 = Fraction(粟, 法)

# 遞倍之，即得母、翁主所償之數
母償 = 2 * 雛償
翁償 = 4 * 雛償

# 答案
a = 雛償
b = 母償
c = 翁償#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
