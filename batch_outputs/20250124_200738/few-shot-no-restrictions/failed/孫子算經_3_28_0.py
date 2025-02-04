"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

#----- content starts here -----
"""
Suppose there are three chickens sharing 1100 grains of millet. 
The chick eats 1 grain, the hen eats 2 grains, and the rooster eats 4 grains (in one cycle).
The owner demands repayment of the millet. How much should each chicken repay?

The procedure says: Place the 1100 grains of millet as the dividend.
Add together the millet eaten by the three chickens in one cycle (1 + 2 + 4 = 7 grains) as the divisor.
Divide the total millet by the divisor to get the number of cycles (143 cycles).
The chick repays 1 grain per cycle, the hen repays 2 grains per cycle, and the rooster repays 4 grains per cycle.

Answer: The chick repays *a* grains, the hen repays *b* grains, and the rooster repays *c* grains.
"""

# Total millet
粟 = 1100

# Millet eaten per cycle
雞雛啄 = 1
雞母啄 = 2
雞翁啄 = 4
每輪啄粟 = 雞雛啄 + 雞母啄 + 雞翁啄

# Total cycles
總輪數 = 粟 // 每輪啄粟

# Repayment for each chicken
a = 總輪數 * 雞雛啄  # Chick repayment
b = 總輪數 * 雞母啄  # Hen repayment
c = 總輪數 * 雞翁啄  # Rooster repayment

a, b, c  # Chick, Hen, Rooster repayments#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 157
Variable 'b' has wrong value. Expected: 286, Actual: 314
Variable 'c' has wrong value. Expected: 572, Actual: 628"""
