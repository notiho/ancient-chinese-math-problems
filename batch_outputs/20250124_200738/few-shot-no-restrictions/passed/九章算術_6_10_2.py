"""
今有惡粟二十斗，舂之，得糲米九斗。今欲求粺米十斗，問︰惡粟幾何？
術曰：置糲米九斗，以九乘之，為法。亦置粺米十斗，以十乘之，又以惡粟二十斗乘之，為實。實如法得一斗。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 20 dou of coarse millet. After pounding, it produces 9 dou of roughly husked millet.
Now, it is desired to obtain 10 dou of finely husked millet.
Question: how much coarse millet is required?

The procedure says: Place the 9 dou of roughly husked millet, multiply it by 9, obtaining the divisor.
Also place the 10 dou of finely husked millet, multiply it by 10, and then multiply it by the 20 dou of coarse millet, obtaining the dividend.
Perform the division, obtaining the number of dou.

Answer: *a* dou.
"""

from fractions import Fraction

# Given values
惡粟 = 20  # coarse millet in dou
糲米 = 9  # roughly husked millet in dou
粺米 = 10  # desired finely husked millet in dou

# Procedure
# 法 = 置糲米九斗，以九乘之
法 = 9 * 糲米

# 實 = 置粺米十斗，以十乘之，又以惡粟二十斗乘之
實 = 10 * 粺米 * 惡粟

# 實如法得一斗
a = Fraction(實, 法)

a  # Output the result in dou#----- content ends here -----

"""
"""
