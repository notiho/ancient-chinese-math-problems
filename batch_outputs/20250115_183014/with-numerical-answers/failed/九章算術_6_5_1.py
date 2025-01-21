"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a(=36/7)斗 。菽 b(=36/35)斛 。
"""

"""
Suppose there is a person who is owed 2 hu of millet. The granary has no millet, so it is desired to substitute with 1 part of rice and 2 parts of beans to fulfill the owed millet.
Question: how much rice and beans should be given?

The procedure says: Place 1 part of rice and 2 parts of beans to determine their equivalent in millet.
Add them, obtaining 3 and 8/9 (or 9/8 as a fraction), which becomes the divisor.
Also place 1 part of rice and 2 parts of beans, and multiply them by the 2 hu of millet, each becoming its own dividend.
Divide the dividends by the divisor to obtain the equivalent amounts.

Answer: *a*(=36/7) dou of rice, and *b*(=36/35) hu of beans.
"""

from fractions import Fraction

# 當稟粟二斛
粟 = 2  # in hu

# 米一、菽二
米 = 1
菽 = 2

# 并之得三、九分之八，以為法
法 = Fraction(米 + 菽, 9 / 8)

# 亦置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米 * 粟
菽實 = 菽 * 粟

# 實如法得一斛
a = Fraction(米實, 法)  # 36/7 dou
b = Fraction(菽實, 法)  # 36/35 hu
"""
Code error: both arguments should be Rational instances"""
