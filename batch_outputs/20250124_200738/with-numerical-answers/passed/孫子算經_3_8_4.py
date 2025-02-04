"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a(=5/2)觔 。
"""

#----- content starts here -----
"""
Suppose there are 91,135 jin of cotton, to be distributed among 36,454 households.
Question: how much does each household receive?

The procedure says: Place 91,135 jin as the dividend; take 36,454 households as the divisor.
Divide them, obtaining 2 jin, with a remainder of 18,227 jin.
Multiply the remainder by 16, obtaining 291,632 liang.
Divide this by the number of households, obtaining the result.

Answer: *a*(=5/2) jin.
"""

from fractions import Fraction

# 置九萬一千一百三十五觔，為實
實 = 91135

# 以三萬六千四百五十四戶，為法
法 = 36454

# 除之，得二觔，不盡一萬八千二百二十七觔
商 = 實 // 法  # 2
餘 = 實 % 法  # 18227

# 以一十六乘之，得二十九萬一千六百三十二兩
餘兩 = 16 * 餘  # 291632

# 以戶除之，即得
每戶兩 = Fraction(餘兩, 法)  # 8/5 jin (in liang)

# 合併結果為觔
a = 商 + 每戶兩 / 16  # 5/2 jin#----- content ends here -----

"""
"""
