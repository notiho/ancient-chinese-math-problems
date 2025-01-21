"""
今有惡粟二十斗，舂之，得糲米九斗。今欲求粺米十斗，問︰惡粟幾何？
荅曰： a斗 。
"""

"""
Suppose there are 20 dou of coarse millet (惡粟), and after pounding it, 9 dou of roughly husked millet (糲米) is obtained.
Now, it is desired to obtain 10 dou of finely husked millet (粺米).
Question: how much coarse millet (惡粟) is required?

Answer: *a* dou.
"""

# Given:
# 20 dou of coarse millet produces 9 dou of roughly husked millet.
# We need to calculate how much coarse millet is required to produce 10 dou of finely husked millet.

# Conversion ratio from coarse millet to roughly husked millet
coarse_to_rough_ratio = Fraction(9, 20)

# Conversion ratio from roughly husked millet to finely husked millet
rough_to_fine_ratio = Fraction(9, 10)

# Total conversion ratio from coarse millet to finely husked millet
coarse_to_fine_ratio = coarse_to_rough_ratio * rough_to_fine_ratio

# To produce 10 dou of finely husked millet, calculate the required coarse millet
a = Fraction(10, coarse_to_fine_ratio)

# Final result
a
"""
"""
