"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

"""
Suppose there are three chickens pecking at a total of 1100 grains of millet. 
The chick pecks 1 grain, the hen pecks 2 grains, and the rooster pecks 4 grains.
The owner demands repayment of the millet. How much should each chicken repay?

The procedure says: Place the 1100 grains of millet as the dividend.
Add together the millet pecked by the three chickens (1 + 2 + 4 = 7 grains) as the divisor.
Divide the dividend by the divisor to find the number of grains the chick owes.
Double this for the hen, and double again for the rooster to find their respective repayments.

Answer: The chick owes *a* grains, the hen owes *b* grains, and the rooster owes *c* grains.
"""

# 置粟一千一粒為實
實 = 1100

# 副并三雞所啄粟七粒為法
法 = 1 + 2 + 4

# 除之，得一百四十三粒為雞雛主所償之數
雞雛償 = Fraction(實, 法)

# 遞倍之，即得母、翁主所償之數
雞母償 = 2 * 雞雛償
雞翁償 = 4 * 雞雛償

a = 雞雛償
b = 雞母償
c = 雞翁償
"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
