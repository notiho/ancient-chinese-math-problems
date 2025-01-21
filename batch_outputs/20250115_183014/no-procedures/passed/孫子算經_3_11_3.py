"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, every hu loses 3 sheng.
Question: how much is lost in one year, and how much is lost in nine years?

Answer: in *a* year, it loses *b* hu; in *c* years, it loses *d* hu.
"""

# Total millet in hu and dou
total_hu = 369980
total_dou = 7

# Convert dou to hu (1 hu = 10 dou)
total_hu += Fraction(total_dou, 10)

# Loss per hu per year in sheng
loss_per_hu_per_year = 3  # in sheng

# Convert loss per hu per year to hu (1 hu = 10 dou = 100 sheng)
loss_per_hu_per_year_in_hu = Fraction(loss_per_hu_per_year, 100)

# Total loss in one year
b = total_hu * loss_per_hu_per_year_in_hu

# Total loss in nine years
d = b * 9

# Assign year values
a = 1
c = 9

# Results
a, b, c, d
"""
"""
