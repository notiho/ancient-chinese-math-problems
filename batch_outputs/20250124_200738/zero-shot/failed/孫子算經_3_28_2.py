"""
今有三雞共啄粟一千一粒，雛啄一，母啄二，翁啄四。主責本粟，三雞主各償幾何？
術曰：置粟一千一粒為實，副并三雞所啄粟七粒為法，除之，得一百四十三粒為雞雛主所償之數，遞倍之，即得母、翁主所償之數。
答曰：雞雛主 a ，雞母主 b ，雞翁主 c 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_grains = 1100  # Total grains of millet
grains_per_chick = 1  # Grains eaten by the chick
grains_per_hen = 2  # Grains eaten by the hen
grains_per_rooster = 4  # Grains eaten by the rooster

# Total grains eaten by all three chickens in one round
grains_per_round = grains_per_chick + grains_per_hen + grains_per_rooster

# Calculate the number of rounds
rounds = total_grains // grains_per_round

# Calculate the grains each type of chicken must repay
a = Fraction(grains_per_chick * rounds)  # Grains repaid by the chick
b = Fraction(grains_per_hen * rounds)  # Grains repaid by the hen
c = Fraction(grains_per_rooster * rounds)  # Grains repaid by the rooster

# Results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. **Inputs**: The total grains of millet (`total_grains`) and the grains eaten per round by each type of chicken (`grains_per_chick`, `grains_per_hen`, `grains_per_rooster`) are given.
2. **Grains per round**: The sum of grains eaten by all three chickens in one round is calculated as `grains_per_round`.
3. **Number of rounds**: The total number of rounds is calculated by dividing the total grains by the grains eaten per round.
4. **Repayment**: Each chicken repays the grains it ate in proportion to its consumption per round.

The variables `a`, `b`, and `c` represent the grains repaid by the chick, hen, and rooster, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 143, Actual: 157
Variable 'b' has wrong value. Expected: 286, Actual: 314
Variable 'c' has wrong value. Expected: 572, Actual: 628"""
