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
Add them, obtaining 3 and 8/9 (or 27/9 and 8/9), which becomes the divisor.
Also place 1 unit of rice and 2 units of beans, and multiply them by 2 hu of millet, each becoming its own dividend.
Divide the dividends by the divisor to obtain the equivalent amounts.

Answer: *a*(=36/7) dou of rice, *b*(=36/35) hu of beans.
"""

from fractions import Fraction

# 當稟粟二斛
粟 = 2  # in hu

# 置米一、菽二
米 = 1  # unit of rice
菽 = 2  # unit of beans

# 并之得三、九分之八，以為法
法 = Fraction(3) + Fraction(8, 9)

# 亦置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米 * 粟
菽實 = 菽 * 粟

# 實如法得一斛
a = Fraction(米實, 法) * 10  # Convert hu to dou (1 hu = 10 dou)
b = Fraction(菽實, 法)  # in hu

# 米 a(=36/7)斗, 菽 b(=36/35)斛#----- content ends here -----

"""
"""
