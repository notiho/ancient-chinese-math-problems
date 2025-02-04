"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""
Suppose there is 369,980 hu and 7 dou of millet in a granary for 9 years. Each year, 3 sheng per hu is lost due to spoilage.
Question: how much is lost in one year, and how much is lost in nine years?

Answer: in one year, *a* hu is lost, and in nine years, *b* hu is lost.
"""

from fractions import Fraction

# 粟總量：三十六萬九千九百八十斛七斗
total_millet_hu = 369980
total_millet_dou = 7

# Convert dou to hu (1 hu = 10 dou)
total_millet_hu += Fraction(total_millet_dou, 10)

# 每年每斛耗三升
loss_per_hu_per_year = Fraction(3, 10)  # 3 sheng = 3/10 hu

# 一年耗
a = total_millet_hu * loss_per_hu_per_year

# 九年耗
b = a * 9

a, b  # Output the results for one year and nine years.
"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
