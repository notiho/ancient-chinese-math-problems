"""
今有窖上方五尺下方八尺深九尺問受粟幾何
術曰上下方相乘又各自相乘併以深乘之三而一所得為實實如斛法而一得斛數
答曰 a斛
"""

"""
Suppose there is a pit with an upper square side of 5 chi, a lower square side of 8 chi, and a depth of 9 chi.
Question: how much millet can it hold?

The procedure says: Multiply the upper and lower square sides with each other, then multiply each of them with itself.
Add these results together, and multiply by the depth.
Divide by 3, obtaining the volume.
Divide the volume by the hu-divisor (10), obtaining the number of hu.

Answer: *a* hu.
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
上方自乘 = 上方 * 上方
下方自乘 = 下方 * 下方

# 並以深乘之
實 = (上下相乘 + 上方自乘 + 下方自乘) * 深

# 三而一所得為實
實 = Fraction(實, 3)

# 實如斛法而一，斛法為10
斛法 = 10
a = Fraction(實, 斛法)
"""
Variable 'a' has wrong value. Expected: 2150/9, Actual: 387/10"""
