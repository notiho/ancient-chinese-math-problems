"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a(=8) 獸 b(=7) 禽。
"""

#----- content starts here -----
"""
Suppose there are beasts, each with 6 heads and 4 legs, and birds, each with 2 heads and 2 legs.
Altogether, there are 76 heads above and 46 legs below.
Question: how many beasts and birds are there respectively?

The procedure says: Double the number of legs and subtract the number of heads. Halve the remainder, and that gives the number of beasts.
Multiply the number of beasts by 4, subtract the number of legs, and halve the remainder, and that gives the number of birds.

Answer: *a*(=8) beasts and *b*(=7) birds.
"""

# 上有七十六首
總首 = 76

# 下有四十六足
總足 = 46

# 倍足以減首
倍足減首 = 2 * 總足 - 総首

# 餘半之，即獸
獸 = Fraction(倍足減首, 2)

# 以四乘獸
四乘獸 = 4 * 獸

# 減足
減足 = 四乘獸 - 總足

# 餘半之，即禽
禽 = Fraction(減足, 2)

a = 獸  # 8
b = 禽  # 7#----- content ends here -----

"""
Code error: name '総首' is not defined"""
