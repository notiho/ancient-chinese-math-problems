"""
假令有句股相乘冪七百六十五分之一弦多於句三十六十分之九問三事各多少
術曰冪自乘倍多數而一為實半多數為廉法從開立方除之即句以弦多句加之即弦以句除冪即股
答曰句 a 股 b 弦 c 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (ju) and height (gu) is 1/765 of the square of the hypotenuse (xian).
The hypotenuse exceeds the base by 9/36 (or 1/4).
Question: What are the three sides (ju, gu, xian)?

The procedure says:
1. Take the square of the hypotenuse (mian), multiply it by itself, and double the excess number (1/4), adding 1 to form the dividend (shi).
2. Take half of the excess number (1/4) as the divisor (lianfa).
3. Extract the cube root of the division result to obtain the base (ju).
4. Add the excess (1/4) to the base to obtain the hypotenuse (xian).
5. Divide the square of the hypotenuse by the base to obtain the height (gu).

Answer: The base is *a*, the height is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪 (square of the hypotenuse) is 1/765
冪 = Fraction(1, 765)

# 弦多於句 36分之9 (or 1/4)
多數 = Fraction(9, 36)

# 冪自乘
冪自乘 = 冪 * 冪

# 倍多數而一為實
實 = 冪自乘 * (2 * 多數 + 1)

# 半多數為廉法
廉法 = 多數 / 2

# 從開立方除之即句
句 = (實 / 廉法) ** Fraction(1, 3)

# 以弦多句加之即弦
弦 = 句 + 多數

# 以句除冪即股
股 = 冪 / 句

# Final results
a = 句
b = 股
c = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.027370713909446624
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.04775869371943936
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.2773707139094466"""
