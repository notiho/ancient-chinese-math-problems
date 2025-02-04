"""
今有獸六首四足禽二首二足上有七十六首下有四十六足問禽獸各幾何
術曰倍足以減首餘半之即獸以四乘獸減足餘半之即禽
答曰 a 獸 b 禽
"""

"""
Suppose there are 6-headed, 4-legged beasts and 2-headed, 2-legged birds.
There are 76 heads in total and 46 legs in total.
Question: how many beasts and birds are there respectively?

The procedure says: Double the number of legs, subtract the number of heads, and halve the remainder to get the number of beasts.
Multiply the number of beasts by 4, subtract the number of legs, and halve the remainder to get the number of birds.

Answer: *a* beasts and *b* birds.
"""

# 上有七十六首
總首 = 76

# 下有四十六足
總足 = 46

# 倍足以減首
倍足減首 = 2 * 總足 - 總首

# 餘半之，即獸
獸 = Fraction(倍足減首, 2)

# 以四乘獸
四乘獸 = 4 * 獸

# 減足
減足 = 四乘獸 - 總足

# 餘半之，即禽
禽 = Fraction(減足, 2)

a = 獸
b = 禽
"""
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
