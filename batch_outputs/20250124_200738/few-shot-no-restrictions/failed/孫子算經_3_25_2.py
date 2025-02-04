"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

#----- content starts here -----
"""
Suppose there are beasts, each with 6 heads and 4 legs, and birds, each with 2 heads and 2 legs.
In total, there are 76 heads and 46 legs.
Question: how many beasts and birds are there?

The procedure says: Double the number of legs and subtract the number of heads. Halve the remainder to find the number of beasts.
Multiply the number of beasts by 4, subtract the total number of legs, and halve the remainder to find the number of birds.

Answer: *a* beasts and *b* birds.
"""

# Total heads and legs
總首 = 76
總足 = 46

# Beasts: 6 heads, 4 legs
獸首 = 6
獸足 = 4

# Birds: 2 heads, 2 legs
禽首 = 2
禽足 = 2

# Step 1: Double the legs and subtract the heads, then halve the result to find the number of beasts
獸 = (2 * 總足 - 總首) // 2

# Step 2: Multiply the number of beasts by 4, subtract the total legs, and halve the result to find the number of birds
禽 = (總首 - 獸 * 獸首) // 禽首

# Final answer
a = 獸
b = 禽#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 7, Actual: 14"""
