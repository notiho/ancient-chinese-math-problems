"""
今有三雞共啄粟一千一粒雛啄一母啄二翁啄四主責本粟三雞主各償幾何
術曰置粟一千一粒為實副并三雞所啄粟七粒為法除之得一百四十三粒為雞雛主所償之數遞倍之即得母翁主所償之數
答曰雞雛主 a 雞母主 b 雞翁主 c 
"""

"""
Suppose there are three chickens sharing 1100 grains of millet. 
The chick eats 1 grain, the hen eats 2 grains, and the rooster eats 4 grains in the same time.
The owner demands the millet to be repaid proportionally by the three chickens.
Question: how much does each chicken's owner repay?

The procedure says: Place 1100 grains of millet as the dividend.
Add together the grains eaten by the three chickens (1 + 2 + 4 = 7 grains) as the divisor.
Divide the dividend by the divisor, obtaining 143 grains as the amount repaid by the chick's owner.
Double it to obtain the amount repaid by the hen's owner, and double it again to obtain the amount repaid by the rooster's owner.

Answer: the chick's owner repays *a* grains, the hen's owner repays *b* grains, and the rooster's owner repays *c* grains.
"""

# 置粟一千一粒為實
實 = 1100

# 副并三雞所啄粟七粒為法
法 = 1 + 2 + 4

# 除之得一百四十三粒為雞雛主所償之數
雞雛主 = Fraction(實, 法)

# 遞倍之即得母翁主所償之數
雞母主 = 2 * 雞雛主
雞翁主 = 4 * 雞雛主

a = 雞雛主
b = 雞母主
c = 雞翁主
"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
