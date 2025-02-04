"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

"""
Suppose there is a person who is supposed to receive 2 hu of millet. 
The granary has no millet, so it is desired to substitute with 1 part rice and 2 parts beans to fulfill the amount of millet owed.
Question: how much rice and beans should be given?

The procedure says: Place 1 part rice and 2 parts beans to determine their equivalent in millet.
Add them, obtaining 3, and take 8/9 as the divisor.
Also place 1 part rice and 2 parts beans, and multiply each by 2 hu of millet, making each a dividend.
Divide each dividend by the divisor, obtaining the amount of 1 hu.

Answer: *a* dou of rice, and *b* hu of beans.
"""

from fractions import Fraction

# 當稟粟二斛
粟 = 2  # in hu

# 置米一、菽二
米 = 1
菽 = 2

# 并之得三、九分之八，以為法
法 = Fraction(8, 9)

# 亦置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米 * 粟
菽實 = 菽 * 粟

# 實如法得一斛
a = 米實 / 法  # 米 in dou
b = 菽實 / 法  # 菽 in hu
"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 9/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 9/2"""
