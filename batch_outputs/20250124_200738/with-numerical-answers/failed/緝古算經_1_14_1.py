"""
假令有句股相乘冪七百六十五分之一，弦多於句三十六十分之九。問：三事各多少？
術曰：冪自乘，倍多數而一，為實。半多數，為廉法，從。開立方除之，即句。以弦多句加之，即弦。以句除冪，即股。
答曰：句 a(=287/20) ，股 b(=246/5) ，弦 c(=205/4) 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (ju) and height (gu) equals 1/765. 
The hypotenuse (xian) is greater than the base by 9/36 (or 1/4). 
Question: what are the values of the three sides?

The procedure says: Square the product (mi), double the excess value (duoshu), and add 1 to obtain the dividend (shi). 
Take half of the excess value as the divisor (lianfa). 
Divide the cube root of the dividend by the divisor to obtain the base (ju). 
Add the excess value to the base to obtain the hypotenuse (xian). 
Divide the product (mi) by the base to obtain the height (gu).

Answer: The base (ju) is *a*(=287/20), the height (gu) is *b*(=246/5), and the hypotenuse (xian) is *c*(=205/4).
"""

from fractions import Fraction

# 冪七百六十五分之一
冪 = Fraction(1, 765)

# 弦多於句三十六十分之九
多數 = Fraction(9, 36)

# 冪自乘
冪平方 = 冪 ** 2

# 倍多數而一，為實
實 = 2 * 多數 + 1

# 半多數，為廉法
廉法 = 多數 / 2

# 從。開立方除之，即句
句 = (冪平方 / 實) ** Fraction(1, 3) / 廉法

# 以弦多句加之，即弦
弦 = 句 + 多數

# 以句除冪，即股
股 = 冪 / 句

# 答案
a = 句  # 287/20
b = 股  # 246/5
c = 弦  # 205/4#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.08355105610932304
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.015645398195484897
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.333551056109323"""
