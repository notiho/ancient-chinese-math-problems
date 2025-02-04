"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose a person is owed 2 hu of millet. However, the granary has no millet, so it is desired to substitute rice and beans in the ratio of 1:2 (1 part rice, 2 parts beans) to fulfill the owed millet.
Question: how much rice and beans should be given?

Answer: *a* dou of rice, and *b* hu of beans.
"""

# 粟二斛
粟 = 2  # in hu

# Ratio of rice to beans is 1:2
rice_ratio = 1
bean_ratio = 2
total_ratio = rice_ratio + bean_ratio

# Convert millet into rice and beans
# Rice is 1/3 of the total millet (in dou, since 1 hu = 10 dou)
a = Fraction(rice_ratio, total_ratio) * 粟 * 10  # 米 a斗

# Beans are 2/3 of the total millet (in hu)
b = Fraction(bean_ratio, total_ratio) * 粟  # 菽 b斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 20/3
Variable 'b' has wrong value. Expected: 36/35, Actual: 4/3"""
