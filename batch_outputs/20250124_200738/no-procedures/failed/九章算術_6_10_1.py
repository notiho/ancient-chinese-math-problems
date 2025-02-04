"""
今有惡粟二十斗，舂之，得糲米九斗。今欲求粺米十斗，問︰惡粟幾何？
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 20 dou of coarse millet (惡粟), and after pounding it, 9 dou of roughly husked millet (糲米) are obtained.
Now, it is desired to obtain 10 dou of finely husked millet (粺米).
Question: how much coarse millet (惡粟) is required?

Answer: *a* dou.
"""

# Given values
惡粟 = 20  # 20 dou of coarse millet
糲米 = 9   # 9 dou of roughly husked millet obtained from 20 dou of coarse millet

# Conversion ratio from coarse millet to roughly husked millet
conversion_ratio_rough = Fraction(糲米, 惡粟)

# Conversion ratio from roughly husked millet to finely husked millet
# Typically, finely husked millet is obtained by taking 80% of roughly husked millet
conversion_ratio_fine = Fraction(8, 10)

# Total conversion ratio from coarse millet to finely husked millet
total_conversion_ratio = conversion_ratio_rough * conversion_ratio_fine

# Desired amount of finely husked millet
desired_fine_millet = 10  # 10 dou

# Calculate the required amount of coarse millet
a = Fraction(desired_fine_millet, total_conversion_ratio)

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2000/81, Actual: 250/9"""
