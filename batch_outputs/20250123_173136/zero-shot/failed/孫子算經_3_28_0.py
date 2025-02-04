"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's how we can compute the values of the unknowns `a`, `b`, and `c`:


"""


from fractions import Fraction

# Total grains of millet
total_grains = 1100

# The sum of grains pecked by the three chickens in one round
grains_per_round = 1 + 2 + 4

# Compute the number of grains each chicken is responsible for
a = Fraction(total_grains, grains_per_round)  # Chick (雛) responsibility
b = 2 * a  # Hen (母) responsibility
c = 4 * a  # Rooster (翁) responsibility

# The results
a, b, c


"""


This code calculates the values of `a`, `b`, and `c` using the given information. The results will be in the form of fractions, as required.
"""


"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
