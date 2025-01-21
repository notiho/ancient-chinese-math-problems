"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, every hu loses 3 sheng.
Question: how much is lost in one year, and how much is lost in nine years?

Answer: in *a* year, *b* hu are lost; in *c* years, *d* hu are lost.
"""

# Total millet in hu and dou
total_hu = 369980
total_dou = 7

# Convert dou to hu (1 hu = 10 dou)
total_hu += Fraction(total_dou, 10)

# Loss per hu per year in sheng (1 hu = 10 dou = 100 sheng)
loss_per_hu_per_year = Fraction(3, 100)

# Total loss in one year
loss_one_year = total_hu * loss_per_hu_per_year

# Total loss in nine years
loss_nine_years = 9 * loss_one_year

# Convert losses back to hu and dou
a = 1  # for one year
b = loss_one_year  # loss in hu for one year

c = 9  # for nine years
d = loss_nine_years  # loss in hu for nine years

# Final results
a, b, c, d
"""
"""
