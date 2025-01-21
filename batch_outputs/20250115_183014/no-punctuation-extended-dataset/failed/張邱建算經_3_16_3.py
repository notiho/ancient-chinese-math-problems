"""
今有惡粟一斛五㪷舂之得糲米七㪷今有惡粟二斛問為粺米幾何
術曰置糲米之數求為粺米所得之數以乘今有惡粟為實以本粟為法實如法得一
答曰 a㪷
"""

"""
Suppose there is 1 hu and 5 dou of poor-quality millet. After hulling, 7 dou of roughly husked millet is obtained.
Now suppose there are 2 hu of poor-quality millet.
Question: how much finely husked millet is obtained?

The procedure says: Place the amount of roughly husked millet obtained and use it to calculate the amount of finely husked millet.
Multiply the obtained amount by the current amount of poor-quality millet, making it the dividend.
Use the original amount of poor-quality millet as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* dou.
"""

# 惡粟一斛五㪷
本粟 = 1 * 10 + 5  # Convert 1 hu and 5 dou to dou

# 舂之得糲米七㪷
糲米 = 7

# 今有惡粟二斛
今粟 = 2 * 10  # Convert 2 hu to dou

# 置糲米之數求為粺米所得之數
所得之數 = 糲米

# 以乘今有惡粟為實
實 = 所得之數 * 今粟

# 以本粟為法
法 = 本粟

# 實如法得一
a = Fraction(實, 法)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 42/5, Actual: 28/3"""
