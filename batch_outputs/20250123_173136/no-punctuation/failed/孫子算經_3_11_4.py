"""
今有粟三十六萬九千九百八十斛七斗在倉九年年斛耗三升問一年九年各耗幾何
術曰置三十六萬九千九百八十斛七斗以三升乘之得一年之耗又以九乘之即九年之耗
答曰一年耗 a斛 九年耗 b斛 
"""

"""
Suppose there are 369,980 hu and 7 dou of millet in a granary for 9 years.
Each year, 3 sheng per hu is lost.
Question: how much is lost in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou.
Multiply it by 3 sheng to obtain the loss for one year.
Then multiply it by 9 to obtain the loss for nine years.

Answer: the loss for one year is *a* hu, and the loss for nine years is *b* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟 = 369980 + Fraction(7, 10)  # Convert 7 dou to hu (1 hu = 10 dou)

# 年斛耗三升
年耗率 = Fraction(3, 10)  # Convert 3 sheng to hu (1 hu = 10 dou = 100 sheng)

# 以三升乘之，得一年之耗
一年耗 = 粟 * 年耗率

# 又以九乘之，即九年之耗
九年耗 = 一年耗 * 9

a = 一年耗
b = 九年耗
"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
