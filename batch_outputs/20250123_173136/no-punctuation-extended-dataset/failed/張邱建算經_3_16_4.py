"""
今有惡粟一斛五㪷舂之得糲米七㪷今有惡粟二斛問為粺米幾何
術曰置糲米之數求為粺米所得之數以乘今有惡粟為實以本粟為法實如法得一
答曰 a㪷
"""

"""
Suppose there is 1 hu and 5 dou of poor-quality millet. After pounding it, 7 dou of roughly husked millet is obtained.
Now, suppose there are 2 hu of poor-quality millet.
Question: how much finely husked millet is obtained?

The procedure says: Place the amount of roughly husked millet obtained from the first case.
Use it to find the amount of finely husked millet.
Multiply this by the current amount of poor-quality millet, making it the dividend.
Use the original amount of poor-quality millet as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* dou.
"""

from fractions import Fraction

# Initial poor-quality millet: 1 hu 5 dou
# Convert to dou (1 hu = 10 dou)
本粟 = 1 * 10 + 5  # 1 hu and 5 dou

# Roughly husked millet obtained: 7 dou
糲米 = 7

# Current poor-quality millet: 2 hu
# Convert to dou
今有惡粟 = 2 * 10  # 2 hu

# Procedure:
# Use roughly husked millet to find finely husked millet
# Multiply by the current poor-quality millet (實)
實 = 糲米 * 今有惡粟

# Use the original poor-quality millet as the divisor (法)
法 = 本粟

# Divide 实 by 法 to get the result
a = Fraction(實, 法)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 42/5, Actual: 28/3"""
