"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a person who is owed 2 hu of millet. The granary has no millet, so it is desired to substitute rice and beans (1 part rice, 2 parts beans) to fulfill the owed millet.
Question: how much rice and beans should be given?

The procedure says: Place 1 part rice and 2 parts beans to determine the equivalent amount of millet. 
Add them together, obtaining 3, and take 8/9 of it as the divisor.
Also place 1 part rice and 2 parts beans, and multiply each by the 2 hu of millet, making each its own dividend.
Divide the dividends by the divisor to obtain the equivalent amounts.

Answer: *a* dou of rice, and *b* hu of beans.
"""

# 當稟粟二斛
粟 = 2  # in hu

# 米一、菽二
米比例 = 1
菽比例 = 2

# 并之得三、九分之八，以為法
比例和 = 米比例 + 菽比例
法 = Fraction(8, 9) * 比例和

# 置米一、菽二，而以粟二斛乘之，各自為實
米實 = 粟 * 米比例
菽實 = 粟 * 菽比例

# 實如法得一斛
a = Fraction(米實, 法)  # 米 in dou
b = Fraction(菽實, 法)  # 菽 in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 3/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 3/2"""
