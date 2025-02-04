"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is supposed to receive 2 hu of millet. However, the granary has no millet, so it is desired to substitute with 1 part rice and 2 parts beans to fulfill the amount of millet owed.
Question: how much rice and beans should be given?

Answer: *a* dou of rice, and *b* hu of beans.
"""

# 粟二斛
粟 = 2  # in hu

# 米一 (1 part rice) and 菽二 (2 parts beans) means the ratio is 1:2
# Total ratio parts = 1 + 2 = 3

# Rice (米) share
a = Fraction(1, 3) * 粟 * 10  # Convert hu to dou (1 hu = 10 dou)

# Beans (菽) share
b = Fraction(2, 3) * 粟  # Keep in hu

# Final result
a, b  # 米 a斗, 菽 b斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 20/3
Variable 'b' has wrong value. Expected: 36/35, Actual: 4/3"""
