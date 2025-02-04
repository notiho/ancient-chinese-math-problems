"""
今有泥方一尺欲為彈丸令徑一寸問得㡬何
術曰置泥方寸數再自乗以十六乗之為實以九為法實如法得一
答曰 a枚
"""

#----- content starts here -----
"""
Suppose there is a cube of clay with a side length of 1 chi. It is desired to make pellets with a diameter of 1 cun.
Question: how many pellets can be made?

The procedure says: Place the number of cubic cun in the clay. Square it, then multiply by 16, obtaining the dividend.
Take 9 as the divisor. Divide the dividend by the divisor to obtain the number of pellets.

Answer: *a* pellets.
"""

from fractions import Fraction

# 泥方一尺
泥方邊長 = 1  # in chi

# 1 chi = 10 cun
泥方邊長寸 = 10 * 泥方邊長  # convert to cun

# 泥方寸數
泥方體積寸數 = 泥方邊長寸 ** 3  # cubic cun

# 再自乘
平方 = 泥方體積寸數 ** 2

# 以十六乘之，為實
實 = 16 * 平方

# 以九為法
法 = 9

# 實如法得一
a = Fraction(實, 法)  # number of pellets#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 16000/9, Actual: 16000000/9"""
