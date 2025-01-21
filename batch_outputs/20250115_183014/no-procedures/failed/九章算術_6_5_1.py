"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
荅曰：米 a斗 。菽 b斛 。
"""

"""
Suppose a person is owed 2 hu of millet. However, the granary has no millet and instead wants to pay with rice and beans.
The exchange rate is 1 hu of millet = 1 hu of rice or 2 hu of beans.

Question: how much rice and beans should be given?

Answer: *a* dou of rice and *b* hu of beans.
"""

# 粟二斛
粟 = 2  # in hu

# 米一 (1 hu of millet = 1 hu of rice)
米 = 粟 * 1  # in hu

# 菽二 (1 hu of millet = 2 hu of beans)
菽 = 粟 * 2  # in hu

# Convert 米 from hu to dou (1 hu = 10 dou)
a = 米 * 10  # 米 in dou
b = 菽  # 菽 in hu

# Final results
a, b  # 米 in dou, 菽 in hu
"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 20
Variable 'b' has wrong value. Expected: 36/35, Actual: 4"""
