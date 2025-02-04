"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. The bucket is filled with millet, and then the mixture is pounded. After processing, 7 dou of rice is obtained.
Question: how much rice was originally in the bucket?

Answer: the original amount of rice is *a* dou.
"""

# Total bucket capacity
bucket_capacity = 10  # in dou

# After pounding, the proportion of rice in the mixture is 7/10
# Let the original amount of rice be x (in dou)
# The millet added is (bucket_capacity - x)
# After pounding, the resulting rice is 7 dou

# Solve for x:
# x / bucket_capacity = 7 / 10
a = Fraction(7, 10) * bucket_capacity

# The original amount of rice is:
a  # in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 7"""
