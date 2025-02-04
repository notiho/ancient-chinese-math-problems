"""
今有獸六首四足禽二首二足上有七十六首下有四十六足問禽獸各幾何
術曰倍足以減首餘半之即獸以四乘獸減足餘半之即禽
答曰 a 獸 b 禽
"""

#----- content starts here -----
"""
Suppose there are 6-headed, 4-legged beasts and 2-headed, 2-legged birds.
The total number of heads is 76, and the total number of legs is 46.
Question: how many beasts and birds are there?

The procedure says: Double the number of legs and subtract the number of heads. Halve the remainder; this gives the number of beasts.
Multiply the number of beasts by 4, subtract the total number of legs, and halve the remainder; this gives the number of birds.

Answer: *a* beasts and *b* birds.
"""

# 上有七十六首
總首 = 76

# 下有四十六足
總足 = 46

# 倍足以減首
倍足減首 = 2 * 總足 - 總首

# 餘半之，即獸
a = Fraction(倍足減首, 2)

# 以四乘獸
獸足 = 4 * a

# 減足
減足 = 總足 - 獸足

# 餘半之，即禽
b = Fraction(減足, 2)#----- content ends here -----

"""
"""
