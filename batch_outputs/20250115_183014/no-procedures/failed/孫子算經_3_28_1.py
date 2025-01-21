"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

"""
Suppose there are three chickens (a chick, a hen, and a rooster) that together pecked at 1100 grains of millet.
The chick pecks 1 grain, the hen pecks 2 grains, and the rooster pecks 4 grains at a time.
The owner demands repayment of the millet. How much should each chicken repay?

Answer: the chick repays *a*, the hen repays *b*, and the rooster repays *c*.
"""

# Total millet pecked
total_millet = 1100

# Pecking ratio: chick:hen:rooster = 1:2:4
ratios = [1, 2, 4]

# Total ratio sum
total_ratio = sum(ratios)

# Calculate repayment for each chicken
a = Fraction(ratios[0] * total_millet, total_ratio)  # Chick's repayment
b = Fraction(ratios[1] * total_millet, total_ratio)  # Hen's repayment
c = Fraction(ratios[2] * total_millet, total_ratio)  # Rooster's repayment

a, b, c  # Outputs the repayment for each chicken
"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
