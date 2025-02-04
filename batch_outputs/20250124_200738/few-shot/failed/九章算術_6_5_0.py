"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is supposed to receive 2 hu of millet as a ration.
The granary has no millet, so it is desired to substitute with 1 part rice and 2 parts beans to fulfill the ration.
Question: how much rice and beans should be given?

The procedure says: Place 1 part rice and 2 parts beans to determine their equivalent in millet.
Add them, obtaining 3, and take 8/9 of it as the divisor.
Also place 1 part rice and 2 parts beans, and multiply each by the 2 hu of millet, making them the dividends.
Divide the dividends by the divisor to obtain the amounts.

The answer says: *a* dou of rice, and *b* hu of beans.
"""

from fractions import Fraction

# 當稟粟二斛
粟 = 2  # in hu

# 米一、菽二
米比例 = 1
菽比例 = 2

# 并之得三、九分之八，以為法
比例和 = 米比例 + 菽比例
法 = Fraction(8, 9) * 比例和

# 置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米比例 * 粟
菽實 = 菽比例 * 粟

# 實如法得一斛
a = Fraction(米實, 法)  # 米的量 in dou
b = Fraction(菽實, 法)  # 菽的量 in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 3/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 3/2"""
