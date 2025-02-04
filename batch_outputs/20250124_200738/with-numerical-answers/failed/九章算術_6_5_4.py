"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a(=36/7)斗 。菽 b(=36/35)斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is supposed to receive 2 hu of millet as rations. 
The granary has no millet, so it is desired to provide rice and beans instead, in the ratio of 1 part rice to 2 parts beans, to substitute for the millet.
Question: how much rice and beans should be given?

The procedure says: Place 1 part rice and 2 parts beans to determine their equivalent in millet.
Add them, obtaining 3, and take 8/9 as the divisor.
Also place 1 part rice and 2 parts beans, and multiply them by the 2 hu of millet, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amounts.

Answer: *a*(=36/7) dou of rice, and *b*(=36/35) hu of beans.
"""

from fractions import Fraction

# 當稟粟二斛
粟 = 2

# 米一、菽二
米比例 = 1
菽比例 = 2

# 并之得三
總比例 = 米比例 + 菽比例

# 九分之八，以為法
法 = Fraction(8, 9)

# 亦置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米比例 * 粟
菽實 = 菽比例 * 粟

# 實如法得一斛
a = Fraction(米實, 總比例 * 法) * 10  # Convert to dou (1 hu = 10 dou)
b = Fraction(菽實, 總比例 * 法)  # Keep in hu

# 米 a(=36/7)斗, 菽 b(=36/35)斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 15/2
Variable 'b' has wrong value. Expected: 36/35, Actual: 3/2"""
