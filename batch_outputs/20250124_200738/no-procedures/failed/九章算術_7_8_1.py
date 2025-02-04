"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. The bucket is filled with millet, and then the mixture is pounded. After processing, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

Answer: *a* dou.
"""

# Total bucket capacity
桶容量 = 10  # in dou

# Rice obtained after pounding
得米 = 7  # in dou

# The proportion of rice in the original mixture is the same as the proportion of rice in the processed mixture.
# Let the original amount of rice be `a` dou.
# Then, the proportion of rice in the original mixture is `a / 10`.
# After pounding, the rice obtained is proportional to the original rice: `得米 = a / 10 * 桶容量`.

# Solve for `a`:
a = Fraction(得米, 桶容量) * 桶容量

# Simplify:
a = Fraction(7)  # The original amount of rice is 7 dou.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 7"""
