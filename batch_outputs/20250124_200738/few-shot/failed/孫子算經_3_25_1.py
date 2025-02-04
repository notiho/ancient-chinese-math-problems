"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

#----- content starts here -----
"""
Suppose there are beasts with six heads and four legs, and birds with two heads and two legs.
There are 76 heads in total and 46 legs in total.
Question: how many beasts and birds are there respectively?

The procedure says: Double the number of legs and subtract the number of heads. Halve the remainder to get the number of beasts.
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
b = 禽#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 7, Actual: -7"""
