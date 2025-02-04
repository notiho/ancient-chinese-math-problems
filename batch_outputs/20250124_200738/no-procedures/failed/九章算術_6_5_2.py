"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose a person is owed 2 hu of millet. However, the granary has no millet and instead wants to substitute with rice and beans.
The substitution is to use 1 part rice and 2 parts beans to replace the millet.

Question: how much rice and beans should be given?

Answer: *a* dou of rice, and *b* hu of beans.
"""

from fractions import Fraction

# 粟二斛
粟 = 2  # in hu

# Ratio of rice to beans is 1:2
rice_ratio = 1
bean_ratio = 2
total_ratio = rice_ratio + bean_ratio

# 米 a斗
# Rice is 1 part of the total ratio, converted to dou (1 hu = 10 dou)
a = Fraction(rice_ratio, total_ratio) * 粟 * 10  # in dou

# 菽 b斛
# Beans are 2 parts of the total ratio, in hu
b = Fraction(bean_ratio, total_ratio) * 粟  # in hu

a, b  # Output rice in dou and beans in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 20/3
Variable 'b' has wrong value. Expected: 36/35, Actual: 4/3"""
