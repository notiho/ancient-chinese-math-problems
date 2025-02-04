"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose a person is owed 2 hu of millet. However, the granary has no millet and instead wants to provide rice and beans as substitutes.
The exchange rate is: 1 hu of millet = 1 hu of rice or 2 hu of beans.

Question: how much rice and beans should be given to fulfill the 2 hu of millet?

Answer: *a* dou of rice, and *b* hu of beans.
"""

from fractions import Fraction

# Millet owed: 2 hu
millet = 2

# Rice and beans are given in proportions:
# 1 hu of millet = 1 hu of rice or 2 hu of beans
# Split the millet equivalently into rice and beans

# Half of the millet is converted to rice
rice_in_hu = Fraction(millet, 2)

# The other half of the millet is converted to beans
beans_in_hu = Fraction(millet, 2) * 2

# Convert rice from hu to dou (1 hu = 10 dou)
a = rice_in_hu * 10

# Beans remain in hu
b = beans_in_hu

# Final results
a, b  # a is in dou, b is in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 10
Variable 'b' has wrong value. Expected: 36/35, Actual: 2"""
