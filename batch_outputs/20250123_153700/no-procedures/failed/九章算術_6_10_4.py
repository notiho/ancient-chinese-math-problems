"""
今有惡粟二十斗，舂之，得糲米九斗。今欲求粺米十斗，問︰惡粟幾何？
荅曰： a斗 。
"""

"""
Suppose there are 20 dou of coarse millet (惡粟), and after pounding it, 9 dou of roughly husked millet (糲米) is obtained.
Now, it is desired to obtain 10 dou of finely husked millet (粺米).
Question: how much coarse millet (惡粟) is needed?

Answer: *a* dou.
"""

# 惡粟二十斗 produces 糲米九斗
coarse_millet = 20
roughly_husked_millet = 9

# Conversion ratio from coarse millet to roughly husked millet
conversion_ratio = Fraction(roughly_husked_millet, coarse_millet)

# 粺米 (finely husked millet) is typically 80% of 糲米 (roughly husked millet)
finely_husked_to_roughly_husked_ratio = Fraction(8, 10)

# To get 10 dou of 粺米, calculate how much 糲米 is needed
required_roughly_husked_millet = Fraction(10, finely_husked_to_roughly_husked_ratio)

# Using the conversion ratio, calculate how much coarse millet is needed
a = Fraction(required_roughly_husked_millet, conversion_ratio)

# Result
a
"""
Variable 'a' has wrong value. Expected: 2000/81, Actual: 250/9"""
