"""
今有獸六首四足禽二首二足上有七十六首下有四十六足問禽獸各幾何
術曰倍足以減首餘半之即獸以四乘獸減足餘半之即禽
答曰 a 獸 b 禽
"""

"""
Suppose there are 6-headed, 4-legged beasts and 2-headed, 2-legged birds.
Above, there are 76 heads, and below, there are 46 legs.
Question: how many beasts and birds are there respectively?

The procedure says: Double the number of legs and subtract the number of heads. Halve the remainder, and that gives the number of beasts.
Multiply the number of beasts by 4, subtract the number of legs, and halve the remainder, and that gives the number of birds.

Answer: *a* beasts and *b* birds.
"""

# 上有七十六首
總首 = 76

# 下有四十六足
總足 = 46

# 倍足以減首
餘數 = 2 * 總足 - 總首

# 餘半之，即獸
a = 餘數 // 2

# 以四乘獸減足
餘數_禽 = 4 * a - 總足

# 餘半之，即禽
b = 餘數_禽 // 2
"""
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
