"""
假令有句股相乘冪七百六十五分之一弦多於句三十六十分之九問三事各多少
術曰冪自乘倍多數而一為實半多數為廉法從開立方除之即句以弦多句加之即弦以句除冪即股
答曰句 a 股 b 弦 c 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (ju) and height (gu) equals 1/765 of the square of the hypotenuse (xian).
The hypotenuse exceeds the base by 9/36 (or 1/4).
Question: What are the lengths of the base (ju), height (gu), and hypotenuse (xian)?

The procedure says:
1. Take the square of the hypotenuse (xian) and multiply it by itself.
2. Double the excess (difference between the hypotenuse and the base) and add 1 to form the dividend.
3. Take half of the excess as the divisor.
4. Divide the dividend by the divisor and then take the cube root to find the base (ju).
5. Add the excess to the base to find the hypotenuse (xian).
6. Divide the product of the base and height by the base to find the height (gu).

Answer: The base is *a*, the height is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪 (product of base and height) is 1/765 of the square of the hypotenuse
冪 = Fraction(1, 765)

# 弦多於句 (hypotenuse exceeds the base) by 36分之9 (1/4)
多數 = Fraction(9, 36)

# 冪自乘倍多數而一為實
實 = 冪 * 冪 * (2 * 多數 + 1)

# 半多數為廉法
廉法 = 多數 / 2

# 從開立方除之即句 (cube root of 实 divided by 廉法 gives the base)
句 = (實 / 廉法) ** Fraction(1, 3)

# 以弦多句加之即弦 (add the excess to the base to find the hypotenuse)
弦 = 句 + 多數

# 以句除冪即股 (divide the product of base and height by the base to find the height)
股 = 冪 / 句

# Final results
a = 句
b = 股
c = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.027370713909446624
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.04775869371943936
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.2773707139094466"""
