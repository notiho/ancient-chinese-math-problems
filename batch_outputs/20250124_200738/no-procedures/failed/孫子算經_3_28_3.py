"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

#----- content starts here -----
"""
Suppose there are three chickens (a chick, a hen, and a rooster) that together pecked at 1100 grains of millet.
The chick pecks 1 grain at a time, the hen pecks 2 grains at a time, and the rooster pecks 4 grains at a time.
The owner demands repayment of the millet. How much should each chicken repay?

Answer: the chick repays *a* grains, the hen repays *b* grains, and the rooster repays *c* grains.
"""

# Total millet pecked
total_millet = 1100

# Chick's share, Hen's share, Rooster's share (based on their pecking ratios)
shares = [1, 2, 4]

# Total ratio sum
total_ratio = sum(shares)

# Calculate each chicken's repayment
a = Fraction(shares[0] * total_millet, total_ratio)  # Chick's repayment
b = Fraction(shares[1] * total_millet, total_ratio)  # Hen's repayment
c = Fraction(shares[2] * total_millet, total_ratio)  # Rooster's repayment

a, b, c  # Outputs the repayment for each chicken#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
