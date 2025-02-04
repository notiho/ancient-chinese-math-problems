"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. The bucket is filled with millet, and then the mixture is pounded to remove the husks. After pounding, 7 dou of rice is obtained.
Question: how much rice was originally in the bucket?

Answer: *a* dou.
"""

# Total capacity of the bucket
total_capacity = 10  # in dou

# After pounding, 7 dou of rice is obtained
resulting_rice = 7  # in dou

# Millet contributes 3/5 of its volume as rice
millet_to_rice_ratio = Fraction(3, 5)

# Let the original rice amount be x (in dou)
# The millet amount is (10 - x)
# The resulting rice is the original rice + rice obtained from millet:
# x + (10 - x) * (3/5) = 7
# Solve for x

from fractions import Fraction

x = (resulting_rice - total_capacity * millet_to_rice_ratio) / (1 - millet_to_rice_ratio)

# The original amount of rice
a = Fraction(x).limit_denominator()

a  # Output the result#----- content ends here -----

"""
"""
