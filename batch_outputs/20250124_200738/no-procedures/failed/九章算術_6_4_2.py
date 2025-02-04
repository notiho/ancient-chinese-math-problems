"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person makes roughly husked millet (糲米), one makes semi-polished millet (粺米), and one makes fully polished millet (鑿米).
The resulting amount of millet (米) for each person must be equal.

Question: how much millet (粟) does each person take to process, and how much millet (米) does each person produce?

Answer:
- 糲米 takes *a* dou of millet.
- 粺米 takes *b* dou of millet.
- 鑿米 takes *c* dou of millet.
- Each person produces *d* dou of millet.
"""

from fractions import Fraction

# Total millet
total_millet = 7

# Conversion ratios for each type of millet:
# 糲米: 3/5 of the millet remains after processing
# 粺米: 2/5 of the millet remains after processing
# 鑿米: 1/5 of the millet remains after processing
conversion_ratios = [Fraction(3, 5), Fraction(2, 5), Fraction(1, 5)]

# Let the resulting amount of millet (米) for each person be equal, denoted as d
# The amount of millet (粟) each person takes is proportional to the inverse of their conversion ratio
# Let d be the resulting amount of millet for each person
d = Fraction(total_millet, sum(Fraction(1, ratio) for ratio in conversion_ratios))

# Calculate the amount of millet (粟) each person takes
a = d / conversion_ratios[0]  # 糲米
b = d / conversion_ratios[1]  # 粺米
c = d / conversion_ratios[2]  # 鑿米

# Output the results
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 252/121, Actual: 14/11
Variable 'b' has wrong value. Expected: 280/121, Actual: 21/11
Variable 'c' has wrong value. Expected: 315/121, Actual: 42/11
Variable 'd' has wrong value. Expected: 756/605, Actual: 42/55"""
