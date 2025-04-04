"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a觔 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 綿九萬一千一百三十五觔
綿 = 91135

# 三萬六千四百五十四戶
戶 = 36454

# 置九萬一千一百三十五觔，為實
實 = 綿

# 以三萬六千四百五十四戶，為法
法 = 戶

# 除之，得二觔，不盡一萬八千二百二十七觔
整觔 = 實 // 法
餘觔 = 實 % 法

# 以一十六乘之，得二十九萬一千六百三十二兩
餘兩 = 餘觔 * 16

# 以戶除之，即得
每戶兩 = Fraction(餘兩, 戶)

# 合併結果
a = Fraction(整觔) + Fraction(每戶兩, 16)
#----- content ends here -----


"""

"""


"""
"""
