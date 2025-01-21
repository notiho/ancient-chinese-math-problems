"""
今有泥方一尺欲為彈丸令徑一寸問得㡬何
術曰置泥方寸數再自乗以十六乗之為實以九為法實如法得一
答曰 a枚
"""

"""
Suppose there is a cubic chi of clay. It is desired to make pellets with a diameter of 1 cun.
Question: how many pellets can be made?

The procedure says: Place the number of cubic cun in the clay. Square it, then multiply by 16 to obtain the dividend.
Take 9 as the divisor. Divide the dividend by the divisor to obtain the result.

The answer says: *a* pellets.
"""

from fractions import Fraction

# 泥方一尺 (1 cubic chi = 1000 cubic cun)
泥方寸數 = 1000

# 再自乘 (square the number of cubic cun)
平方 = 泥方寸數 ** 2

# 以十六乘之，為實 (multiply by 16 to get the dividend)
實 = 16 * 平方

# 以九為法 (take 9 as the divisor)
法 = 9

# 實如法得一 (divide the dividend by the divisor to get the result)
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 16000/9, Actual: 16000000/9"""
