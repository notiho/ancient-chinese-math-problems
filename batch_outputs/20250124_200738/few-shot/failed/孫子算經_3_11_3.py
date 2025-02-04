"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. 
Each year, 3 sheng per hu are consumed. 
Question: how much is consumed in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou. Multiply it by 3 sheng, obtaining the consumption for one year. 
Then multiply it by 9, obtaining the consumption for nine years.

Answer: one year consumes *a* hu, and nine years consume *b* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟 = 369980 + Fraction(7, 10)  # Convert 7 dou to hu (1 dou = 1/10 hu)

# 年斛耗三升
年耗升 = 3

# 置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗
一年耗 = 粟 * Fraction(年耗升, 10)  # Convert 3 sheng to hu (1 hu = 10 sheng)

# 又以九乘之，即九年之耗
九年耗 = 一年耗 * 9

# 答案
a = 一年耗
b = 九年耗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
