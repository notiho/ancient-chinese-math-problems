"""
今有惡粟一斛五㪷舂之得糲米七㪷今有惡粟二斛問為粺米幾何
術曰置糲米之數求為粺米所得之數以乘今有惡粟為實以本粟為法實如法得一
答曰 a㪷
"""

"""
Suppose there is 1 hu and 5 dou of poor millet. After pounding it, 7 dou of roughly husked millet is obtained.
Now suppose there are 2 hu of poor millet.
Question: how much finely husked millet is obtained?

The procedure says: Place the amount of roughly husked millet obtained.
Use it to find the amount of finely husked millet.
Multiply this by the current amount of poor millet, making it the dividend.
Use the original amount of poor millet as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a* dou.
"""

from fractions import Fraction

# 惡粟 1斛5㪷 (convert to dou, as 1 hu = 10 dou)
本粟 = 1 * 10 + 5

# 舂之得糲米 7㪷
糲米 = 7

# 今有惡粟 2斛 (convert to dou)
今粟 = 2 * 10

# 置糲米之數，求為粺米所得之數
所得粺米 = 糲米

# 以乘今有惡粟，為實
實 = 所得粺米 * 今粟

# 以本粟為法
法 = 本粟

# 實如法得一
a = Fraction(實, 法)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 42/5, Actual: 28/3"""
