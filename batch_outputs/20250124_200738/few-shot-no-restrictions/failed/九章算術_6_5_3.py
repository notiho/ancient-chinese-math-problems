"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is supposed to receive 2 hu of millet as a ration. 
The granary has no millet, so it is desired to substitute with 1 unit of rice and 2 units of beans to fulfill the ration.
Question: how much rice and beans should be given?

The procedure says: Place 1 unit of rice and 2 units of beans to determine their equivalent in millet.
Add them together, obtaining 3, and take 8/9 as the divisor.
Also place 1 unit of rice and 2 units of beans, and multiply each by the 2 hu of millet, obtaining the dividend.
Divide the dividend by the divisor to obtain the equivalent amount.

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
a = Fraction(米實, 法)  # 米 in dou
b = Fraction(菽實, 法)  # 菽 in hu

# Output results
a斗 = a  # 米 in dou
b斛 = b  # 菽 in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 9/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 9/2"""
