"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person makes roughly husked millet (糲米), one makes semi-polished millet (粺米), and one makes fully polished millet (鑿米). 
The resulting amount of rice for each person must be equal.

Question: how much millet does each person take, and how much rice does each person produce?

Answer: 糲米 takes *a* dou of millet, 粺米 takes *b* dou of millet, 鑿米 takes *c* dou of millet, and each produces *d* dou of rice.
"""

from fractions import Fraction

# Total millet
total_millet = 7

# Conversion ratios for each type of rice
# 糲米: 3/5 of the millet becomes rice
# 粺米: 2/5 of the millet becomes rice
# 鑿米: 1/2 of the millet becomes rice
conversion_ratios = [Fraction(3, 5), Fraction(2, 5), Fraction(1, 2)]

# Let the amount of rice produced by each person be equal
# Let d be the amount of rice produced by each person
# Then for each type of rice:
# 糲米: a * (3/5) = d
# 粺米: b * (2/5) = d
# 鑿米: c * (1/2) = d

# Solve for a, b, c in terms of d
a = Fraction(5, 3) * Fraction(1, 1)  # a = d * (5/3)
b = Fraction(5, 2) * Fraction(1, 1)  # b = d * (5/2)
c = Fraction(2, 1) * Fraction(1, 1)  # c = d * (2)

# The total millet used must equal 7 dou
# a + b + c = 7
# Substitute the values of a, b, c in terms of d
# (5/3)d + (5/2)d + 2d = 7

# Solve for d
d = Fraction(1, (Fraction(5, 3) + Fraction(5, 2) + 2)) * total_millet

# Calculate a, b, c
a = Fraction(5, 3) * d
b = Fraction(5, 2) * d
c = 2 * d

# Output results
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 252/121, Actual: 70/37
Variable 'b' has wrong value. Expected: 280/121, Actual: 105/37
Variable 'c' has wrong value. Expected: 315/121, Actual: 84/37
Variable 'd' has wrong value. Expected: 756/605, Actual: 42/37"""
