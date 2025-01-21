"""
今有窖上方五尺下方八尺深九尺問受粟幾何
術曰上下方相乘又各自相乘併以深乘之三而一所得為實實如斛法而一得斛數
答曰 a斛
"""

"""
Suppose there is a pit with an upper square side of 5 chi, a lower square side of 8 chi, and a depth of 9 chi.
Question: how much millet can it hold?

The procedure says: Multiply the upper and lower sides with each other. Then, multiply each of them with itself.
Add these together, and multiply by the depth.
Divide by 3, obtaining the volume.
Divide the result by the dou-to-hu conversion factor (10 dou = 1 hu), obtaining the number of hu.

Answer: it holds *a* hu.
"""

# 上方五尺
上方 = 5

# 下方八尺
下方 = 8

# 深九尺
深 = 9

# 上下方相乘
上下相乘 = 上方 * 下方

# 又各自相乘
上平方 = 上方 * 上方
下平方 = 下方 * 下方

# 併以深乘之
實 = (上下相乘 + 上平方 + 下平方) * 深

# 三而一所得為實
實 = Fraction(實, 3)

# 斛法：10斗 = 1斛
斛法 = 10

# 實如斛法而一得斛數
a = Fraction(實, 斛法)
"""
Variable 'a' has wrong value. Expected: 2150/9, Actual: 387/10"""
