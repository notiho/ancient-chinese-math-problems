"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a(=143) ，雞母主 b(=286) ，雞翁主 c(=572) 。
"""

#----- content starts here -----
"""
Suppose there are three chickens pecking at a total of 1100 grains of millet. 
The chick pecks 1 grain, the hen pecks 2 grains, and the rooster pecks 4 grains.
The owner demands repayment of the millet. How much should each chicken repay?

The procedure says: Place the 1100 grains of millet as the dividend.
Add together the grains pecked by the three chickens (1 + 2 + 4 = 7) as the divisor.
Divide the dividend by the divisor to obtain 143 grains, which is the amount the chick must repay.
Double it to obtain the amount the hen must repay, and double it again to obtain the amount the rooster must repay.

Answer: The chick repays *a*(=143), the hen repays *b*(=286), and the rooster repays *c*(=572).
"""

# 置粟一千一粒為實
實 = 1100

# 副并三雞所啄粟七粒為法
法 = 1 + 2 + 4

# 除之，得一百四十三粒為雞雛主所償之數
雞雛 = Fraction(實, 法)

# 遞倍之，即得母、翁主所償之數
雞母 = 2 * 雞雛
雞翁 = 4 * 雞雛

a = 雞雛  # 143
b = 雞母  # 286
c = 雞翁  # 572#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
