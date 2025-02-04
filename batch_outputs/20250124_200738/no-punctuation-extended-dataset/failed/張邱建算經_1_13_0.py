"""
今有泥方一尺欲為彈丸令徑一寸問得㡬何
術曰置泥方寸數再自乗以十六乗之為實以九為法實如法得一
答曰 a枚
"""

#----- content starts here -----
"""
Suppose there is a cube of mud with a side length of 1 chi. It is desired to make pellets with a diameter of 1 cun.
Question: how many pellets can be made?

The procedure says: Place the number of cubic cun of the mud. Square it, then multiply it by 16, obtaining the dividend.
Take 9 as the divisor. Divide the dividend by the divisor, obtaining the number of pellets.

Answer: *a* pellets.
"""

from fractions import Fraction

# 泥方一尺
泥方 = 1  # in chi

# Convert to cubic cun (1 chi = 10 cun)
泥方寸數 = (泥方 * 10) ** 3

# 再自乘 (square it)
平方 = 泥方寸數 ** 2

# 以十六乘之，為實
實 = 16 * 平方

# 以九為法
法 = 9

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 16000/9, Actual: 16000000/9"""
