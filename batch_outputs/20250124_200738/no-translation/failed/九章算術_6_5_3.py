"""
今有人當稟粟二斛。倉無粟，欲與米一、菽二，以當所稟粟。問︰各幾何？
術曰：置米一、菽二求為粟之數。并之得三、九分之八，以為法。亦置米一、菽二，而以粟二斛乘之，各自為實。實如法得一斛。
荅曰：米 a斗 。菽 b斛 。
"""

#----- content starts here -----

# 當稟粟二斛
粟 = 2

# 置米一、菽二求為粟之數
米率 = 1
菽率 = 2

# 并之得三、九分之八，以為法
法 = Fraction(8, 9)

# 亦置米一、菽二，而以粟二斛乘之，各自為實
米實 = 米率 * 粟
菽實 = 菽率 * 粟

# 實如法得一斛
a = Fraction(米實, 法)
b = Fraction(菽實, 法) / 10  # Convert to 斛 (1斛 = 10斗)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36/7, Actual: 9/4
Variable 'b' has wrong value. Expected: 36/35, Actual: 9/20"""
