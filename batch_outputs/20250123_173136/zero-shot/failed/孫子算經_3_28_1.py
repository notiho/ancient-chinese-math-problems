"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Total grains of millet
total_grains = 1100

# Sum of grains pecked by the three chickens in one unit of time
grains_per_unit = 1 + 2 + 4

# Calculate the grains each chicken is responsible for
a = Fraction(total_grains, grains_per_unit)  # Chicken chick's share
b = 2 * a  # Chicken hen's share
c = 4 * a  # Chicken rooster's share

# The results are stored in variables a, b, and c


"""


Now, the variables `a`, `b`, and `c` represent the number of grains each chicken is responsible for:
- `a` is the chick's share.
- `b` is the hen's share.
- `c` is the rooster's share.
"""


"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
