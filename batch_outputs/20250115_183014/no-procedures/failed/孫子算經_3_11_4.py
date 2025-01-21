"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, 3 sheng per hu is lost due to spoilage.
Question: how much is lost in one year, and how much is lost in nine years?

Answer: in *a* year, *b* hu are lost; in *c* years, *d* hu are lost.
"""

# Total millet in hu and dou
total_hu = 369980 + Fraction(7, 10)  # 1 dou = 1/10 hu

# Loss per hu per year in sheng
loss_per_hu_per_year = Fraction(3, 10)  # 3 sheng = 3/10 hu

# Loss in one year
a = 1
b = total_hu * loss_per_hu_per_year

# Loss in nine years
c = 9
d = b * c  # Multiply one year's loss by 9 years

# Results
a, b, c, d
"""
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'd' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
