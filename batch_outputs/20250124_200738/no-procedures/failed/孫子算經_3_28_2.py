"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

#----- content starts here -----
"""
Suppose there are three chickens pecking at 1100 grains of millet. The chick pecks 1 grain, the hen pecks 2 grains, and the rooster pecks 4 grains at a time.
The owner demands repayment of the millet. How much should each chicken repay?

Answer: The chick repays *a* grains, the hen repays *b* grains, and the rooster repays *c* grains.
"""

# Total millet pecked
total_millet = 1100

# Pecking rates
chick_rate = 1
hen_rate = 2
rooster_rate = 4

# Total rate
total_rate = chick_rate + hen_rate + rooster_rate

# Calculate shares
a = Fraction(chick_rate * total_millet, total_rate)  # Chick's share
b = Fraction(hen_rate * total_millet, total_rate)   # Hen's share
c = Fraction(rooster_rate * total_millet, total_rate)  # Rooster's share

# Results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
