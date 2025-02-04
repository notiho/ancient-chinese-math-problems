"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person makes roughly husked millet (糲米), one makes semi-polished millet (粺米), and one makes fully polished millet (鑿米). 
The resulting amounts of millet must be equal for all three.

Question: how much millet does each person take to process, and how much millet does each person produce?

Answer: 糲米 takes *a* dou of millet, 粺米 takes *b* dou of millet, 鑿米 takes *c* dou of millet, and each produces *d* dou of millet.
"""

from fractions import Fraction

# Total millet
total_millet = 7

# Conversion ratios for each type of millet:
# 糲米: 3/5 of the millet remains after processing
# 粺米: 2/5 of the millet remains after processing
# 鑿米: 1/5 of the millet remains after processing

# Let the amount of millet taken by 糲米, 粺米, and 鑿米 be a, b, and c respectively.
# The resulting millet for each type must be equal, so:
# a * (3/5) = b * (2/5) = c * (1/5)

# Let the resulting millet for each type be d.
# Then:
# a = d / (3/5) = (5/3) * d
# b = d / (2/5) = (5/2) * d
# c = d / (1/5) = 5 * d

# The total millet taken must equal 7 dou:
# a + b + c = 7
# (5/3) * d + (5/2) * d + 5 * d = 7

# Solve for d:
d = Fraction(7, (5/3) + (5/2) + 5)

# Calculate a, b, and c:
a = (5/3) * d
b = (5/2) * d
c = 5 * d

# Final results:
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)
d = Fraction(d)

# Output results
a, b, c, d#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
