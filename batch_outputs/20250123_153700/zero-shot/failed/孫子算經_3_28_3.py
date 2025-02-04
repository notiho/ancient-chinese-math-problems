"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves three chickens (a chick, a hen, and a rooster) sharing 1100 grains of millet. The chick eats 1 grain, the hen eats 2 grains, and the rooster eats 4 grains. The task is to determine how many grains each chicken is responsible for repaying.

Here is the Python code:


"""


from fractions import Fraction

# Total grains of millet
total_grains = 1100

# The sum of grains eaten by the three chickens in one cycle
grains_per_cycle = 1 + 2 + 4

# Calculate the number of cycles
cycles = total_grains // grains_per_cycle

# Chick's share
a = Fraction(1, grains_per_cycle) * total_grains

# Hen's share (2 times the chick's share)
b = 2 * a

# Rooster's share (4 times the chick's share)
c = 4 * a

# The results
a, b, c


"""


After running this code, the variables `a`, `b`, and `c` will contain the respective shares of the chick, hen, and rooster in terms of grains of millet.
"""


"""
Variable 'a' has wrong value. Expected: 143, Actual: 1100/7
Variable 'b' has wrong value. Expected: 286, Actual: 2200/7
Variable 'c' has wrong value. Expected: 572, Actual: 4400/7"""
