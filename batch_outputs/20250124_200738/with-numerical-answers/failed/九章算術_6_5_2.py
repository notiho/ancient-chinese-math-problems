"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a(=36/7)斗 。菽 b(=36/35)斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is supposed to receive 2 hu of millet as a ration. 
The granary has no millet, so it is desired to substitute with 1 unit of rice and 2 units of beans to fulfill the ration.
Question: how much rice and beans should be given?

The procedure says: Place 1 unit of rice and 2 units of beans to determine their equivalent in millet. 
Add them, obtaining 3 and 8/9 (or 27/9 + 8/9 = 35/9), as the divisor.
Also place 1 unit of rice and 2 units of beans, and multiply each by the 2 hu of millet, making them the dividends.
Divide the dividends by the divisor to obtain the equivalent amounts.

Answer: *a*(=36/7) dou of rice, *b*(=36/35) hu of beans.
"""

from fractions import Fraction

# 米一、菽二
米 = 1
菽 = 2

# 并之得三、九分之八，以為法
法 = Fraction(米 + 菽, 1)  # 3
法 += Fraction(8, 9)       # 3 + 8/9 = 35/9

# 粟二斛
粟 = 2

# 以粟二斛乘之，各自為實
米實 = 粟 * 米
菽實 = 粟 * 菽

# 實如法得一斛
a = 米實 / 法  # 米 = 36/7 斗
b = 菽實 / 法  # 菽 = 36/35 斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 18/35"""
