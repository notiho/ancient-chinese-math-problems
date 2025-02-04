"""
今有惡粟二十斗，舂之，得糲米九斗。今欲求粺米十斗，問︰惡粟幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 20 dou of coarse millet (惡粟), and after pounding it, 9 dou of roughly husked millet (糲米) is obtained.
Now, it is desired to obtain 10 dou of finely husked millet (粺米).
Question: how much coarse millet (惡粟) is required?

Answer: *a* dou.
"""

# Given data
惡粟_已知 = 20  # 20 dou of coarse millet
糲米_已知 = 9   # 9 dou of roughly husked millet
粺米_目標 = 10  # 10 dou of finely husked millet

# Conversion ratio from coarse millet to roughly husked millet
rough_ratio = Fraction(糲米_已知, 惡粟_已知)

# Conversion ratio from roughly husked millet to finely husked millet
fine_ratio = Fraction(粺米_目標, 糲米_已知)

# Total conversion ratio from coarse millet to finely husked millet
total_ratio = rough_ratio * fine_ratio

# Calculate required coarse millet
a = Fraction(粺米_目標, total_ratio)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2000/81, Actual: 20"""
