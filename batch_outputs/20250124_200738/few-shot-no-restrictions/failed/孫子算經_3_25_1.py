"""
今有獸，六首四足；禽，二首二足，上有七十六首，下有四十六足。問：禽、獸各幾何？
術曰：倍足以減首，餘半之，即獸；以四乘獸，減足，餘半之，即禽。
答曰： a 獸 b 禽。
"""

#----- content starts here -----
"""
Suppose there are beasts with 6 heads and 4 legs each, and birds with 2 heads and 2 legs each.
There are a total of 76 heads and 46 legs.
Question: how many beasts and birds are there?

The procedure says:
Double the number of legs and subtract the number of heads. Halve the remainder to obtain the number of beasts.
Multiply the number of beasts by 4, subtract the total number of legs, and halve the remainder to obtain the number of birds.

Answer: *a* beasts and *b* birds.
"""

# Total heads and legs
總首 = 76
總足 = 46

# Step 1: Double the legs and subtract the heads
倍足減首 = 2 * 總足 - 總首

# Step 2: Halve the result to get the number of beasts
獸 = 倍足減首 // 2

# Step 3: Multiply the number of beasts by 4, subtract the total legs, and halve the result to get the number of birds
禽 = (總首 - 6 * 獸)#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
