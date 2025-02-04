"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is owed 2 hu of millet. However, the granary has no millet, so it is desired to give 1 unit of rice and 2 units of beans as a substitute for the millet owed.
Question: how much rice and beans should be given?

The procedure says: Place 1 unit of rice and 2 units of beans to determine their equivalent in millet. Add them, obtaining 3, and take 8/9 as the divisor. 
Also place 1 unit of rice and 2 units of beans, and multiply each by the 2 hu of millet owed, obtaining the dividend for each. 
Divide the dividend by the divisor to obtain the equivalent amounts.

Answer: *a* dou of rice, and *b* hu of beans.
"""

from fractions import Fraction

# 粟二斛
粟 = 2  # in hu

# 米一、菽二
米 = 1
菽 = 2

# 并之得三、九分之八，以為法
法 = Fraction(8, 9)

# 置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米 * 粟
菽實 = 菽 * 粟

# 實如法得一斛
a = 米實 / 法  # 米的量 in dou
b = 菽實 / 法  # 菽的量 in hu

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 9/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 9/2"""
