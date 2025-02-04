"""
今有惡粟一斛五㪷舂之得糲米七㪷今有惡粟二斛問為粺米幾何
術曰置糲米之數求為粺米所得之數以乘今有惡粟為實以本粟為法實如法得一
答曰 a㪷
"""

"""
Suppose there is 1 hu and 5 dou of poor-quality millet. After pounding, it produces 7 dou of roughly husked millet.
Now, suppose there are 2 hu of poor-quality millet.
Question: how much polished millet does it produce?

The procedure says: Place the amount of roughly husked millet obtained from the first case.
Use it to find the amount of polished millet, which is the number obtained.
Multiply this by the amount of poor-quality millet in the second case, making it the dividend.
Take the original amount of poor-quality millet in the first case as the divisor.
Divide the dividend by the divisor, obtaining the result.

Answer: *a* dou.
"""

# 惡粟一斛五㪷
本粟 = 1 * 10 + 5  # Convert 1 hu and 5 dou to dou

# 舂之得糲米七㪷
糲米 = 7

# 今有惡粟二斛
今粟 = 2 * 10  # Convert 2 hu to dou

# 以糲米之數求為粺米所得之數
所得之數 = 糲米

# 以乘今有惡粟為實
實 = 所得之數 * 今粟

# 以本粟為法
法 = 本粟

# 實如法得一
a = Fraction(實, 法)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 42/5, Actual: 28/3"""
