"""
今有綿九萬一千一百三十五觔給與三萬六千四百五十四戶問戶得幾何
術曰置九萬一千一百三十五觔為實以三萬六千四百五十四戶為法除之得二觔不盡一萬八千二百二十七觔以一十六乘之得二十九萬一千六百三十二兩以戶除之即得
答曰 a觔 
"""

#----- content starts here -----
"""
Suppose there are 91,135 jin of cotton to be distributed among 36,454 households.
Question: how much does each household receive?

The procedure says: Place 91,135 jin as the dividend.
Use 36,454 households as the divisor and divide, obtaining 2 jin with a remainder of 18,227 jin.
Multiply the remainder by 16, obtaining 291,632 liang.
Divide this by the number of households, obtaining the result.

Answer: each household receives *a* jin.
"""

from fractions import Fraction

# 置九萬一千一百三十五觔為實
實 = 91135

# 以三萬六千四百五十四戶為法
法 = 36454

# 除之得二觔不盡一萬八千二百二十七觔
整觔 = 實 // 法
餘觔 = 實 % 法

# 以一十六乘之，得二十九萬一千六百三十二兩
餘兩 = 16 * 餘觔

# 以戶除之，即得
每戶兩 = Fraction(餘兩, 法)

# 合併成每戶所得
a = 整觔 + Fraction(每戶兩, 16)  # 每戶所得以觔為單位#----- content ends here -----

"""
"""
