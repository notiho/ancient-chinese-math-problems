"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
荅曰： a斗 。
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. The bucket is filled with millet, and then the mixture is pounded. After pounding, 7 dou of rice is obtained.
Question: how much rice was originally in the bucket?

Answer: *a* dou.
"""

# Total bucket capacity
total_capacity = 10  # in dou

# Rice obtained after pounding
rice_after_pounding = 7  # in dou

# The ratio of rice to millet after pounding is 7:3 (since the bucket was filled to 10 dou)
# Let the original amount of rice be "a" dou.
# After pounding, the amount of rice remains the same, so:
# a / (10 - a) = 7 / 3

from fractions import Fraction

# Solve for "a"
a = Fraction(7, 10) * total_capacity

# The original amount of rice is:
a  # in dou
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 7"""
