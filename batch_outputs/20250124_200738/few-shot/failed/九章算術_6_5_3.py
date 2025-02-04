"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is owed 2 hu of millet. The granary has no millet, so it is desired to provide rice and beans (1 part rice and 2 parts beans) to substitute for the millet.
Question: how much rice and beans should be given?

The procedure says: Place 1 part rice and 2 parts beans to determine the equivalent amount of millet.
Add these, obtaining 3, and take 8/9 as the divisor.
Also place 1 part rice and 2 parts beans, and multiply them by the 2 hu of millet, each becoming its own dividend.
Do the division, obtaining the amount of 1 hu.

The answer says: *a* dou of rice, and *b* hu of beans.
"""

# 當稟粟二斛
粟 = 2  # in hu

# 米一、菽二
米率 = 1
菽率 = 2

# 并之得三、九分之八，以為法
法 = Fraction(8, 9)

# 亦置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米率 * 粟
菽實 = 菽率 * 粟

# 實如法得一斛
a = 米實 / 法  # 米 in dou
b = 菽實 / 法  # 菽 in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 9/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 9/2"""
