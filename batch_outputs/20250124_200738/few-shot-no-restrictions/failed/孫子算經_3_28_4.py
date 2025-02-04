"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

#----- content starts here -----
"""
Suppose there are three chickens pecking at a total of 1100 grains of millet. 
The chick pecks 1 grain, the hen pecks 2 grains, and the rooster pecks 4 grains. 
The owner demands repayment of the millet. 
How much should each chicken repay?

The procedure says: Place the 1100 grains of millet as the dividend. 
Add together the amounts pecked by the three chickens (1 + 2 + 4 = 7 grains) as the divisor. 
Divide the millet by the divisor to get the amount the chick must repay. 
Double it to get the amount the hen must repay, and double that to get the amount the rooster must repay.

Answer: The chick repays *a*, the hen repays *b*, and the rooster repays *c*.
"""

# Total millet pecked
粟 = 1100

# Pecking rates
雛啄 = 1
母啄 = 2
翁啄 = 4

# Total pecking rate (法)
法 = 雛啄 + 母啄 + 翁啄

# Divide millet by the total pecking rate to get the chick's repayment
a = Fraction(粟, 法)

# Hen's repayment is double the chick's repayment
b = 2 * a

# Rooster's repayment is double the hen's repayment
c = 2 * b

a, b, c  # Chick, hen, and rooster repayments#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
