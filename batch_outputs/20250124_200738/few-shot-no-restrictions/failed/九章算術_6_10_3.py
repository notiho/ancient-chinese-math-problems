"""
今有惡粟二十斗，舂之，得糲米九斗。今欲求粺米十斗，問︰惡粟幾何？
術曰：置糲米九斗，以九乘之，為法。亦置粺米十斗，以十乘之，又以惡粟二十斗乘之，為實。實如法得一斗。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 20 dou of poor-quality millet. After pounding it, 9 dou of roughly husked millet are obtained.
Now, it is desired to obtain 10 dou of finely husked millet.
Question: how much poor-quality millet is required?

The procedure says: Place the 9 dou of roughly husked millet, multiply it by 9, obtaining the divisor.
Also place the 10 dou of finely husked millet, multiply it by 10, and multiply it again by the 20 dou of poor-quality millet, obtaining the dividend.
Perform the division, obtaining the number of dou of poor-quality millet.

Answer: *a* dou.
"""

from fractions import Fraction

# Given values
惡粟 = 20  # 20 dou of poor-quality millet
糲米 = 9    # 9 dou of roughly husked millet
粺米 = 10   # 10 dou of finely husked millet

# Calculate the divisor (法)
法 = 糲米 * 糲米  # 9 * 9

# Calculate the dividend (實)
實 = 粺米 * 糲米 * 惡粟  # 10 * 9 * 20

# Perform the division to find the required amount of poor-quality millet
a = Fraction(實, 法)

# Output the result
a  # The required amount of poor-quality millet in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2000/81, Actual: 200/9"""
