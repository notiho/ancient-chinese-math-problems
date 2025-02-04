"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, 3 sheng per hu is lost due to wastage.
Question: how much is wasted in one year and in nine years?

Answer: in one year, *a* hu is wasted, and in nine years, *b* hu is wasted.
"""

from fractions import Fraction

# Total millet in hu and dou
total_hu = 369980
total_dou = 7

# Convert dou to hu (1 hu = 10 dou)
total_hu += Fraction(total_dou, 10)

# Wastage per hu per year in sheng (1 hu = 10 dou = 100 sheng)
wastage_per_hu_per_year = Fraction(3, 100)

# Wastage in one year
a = total_hu * wastage_per_hu_per_year

# Wastage in nine years
b = a * 9

# Results
a, b
"""
"""
