"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years.
Each year, 3 sheng per hu is lost due to wastage.
Question: how much is lost in one year and in nine years?

Answer: in one year, *a* hu is lost, and in nine years, *b* hu is lost.
"""

from fractions import Fraction

# 粟總量：三十六萬九千九百八十斛七斗
total_millet_hu = 369980  # Total hu
total_millet_dou = 7      # Additional dou

# Convert total millet to hu (1 hu = 10 dou)
total_millet = total_millet_hu + Fraction(total_millet_dou, 10)

# 每年每斛耗三升 (1 hu = 10 dou = 100 sheng, so 3 sheng = 3/100 hu)
annual_loss_per_hu = Fraction(3, 100)

# 一年耗損總量
a = total_millet * annual_loss_per_hu

# 九年耗損總量
b = a * 9

# Results
a, b
"""
"""
