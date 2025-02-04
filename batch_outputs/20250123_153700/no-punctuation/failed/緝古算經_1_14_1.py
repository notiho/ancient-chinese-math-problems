"""
假令有句股相乘冪七百六十五分之一弦多於句三十六十分之九問三事各多少
術曰冪自乘倍多數而一為實半多數為廉法從開立方除之即句以弦多句加之即弦以句除冪即股
答曰句 a 股 b 弦 c 
"""

"""
Suppose there is a right triangle where the product of the base (ju) and height (gu) is 1/765 of the square of the hypotenuse (xian).
The hypotenuse exceeds the base by 9/36 (or 1/4).
Question: What are the lengths of the base (ju), height (gu), and hypotenuse (xian)?

The procedure says:
1. Multiply the square of the hypotenuse by itself, then double the excess amount, and add 1 to obtain the dividend.
2. Take half of the excess amount as the divisor.
3. Perform cube root extraction to find the base (ju).
4. Add the excess amount to the base to find the hypotenuse (xian).
5. Divide the product of the base and height by the base to find the height (gu).

Answer: The base is *a*, the height is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪 (hypotenuse squared) is 1/765 of the product of the base and height
冪率 = Fraction(1, 765)

# 弦多於句 36分之9
弦多句 = Fraction(9, 36)

# 1. 冪自乘倍多數而一為實
倍多數 = 2 * 弦多句
實 = 冪率 * 冪率 + 倍多數 + 1

# 2. 半多數為廉法
廉法 = 弦多句 / 2

# 3. 從開立方除之即句
句 = 實 ** (1 / 3) / 廉法

# 4. 以弦多句加之即弦
弦 = 句 + 弦多句

# 5. 以句除冪即股
股 = 冪率 / 句

a = 句
b = 股
c = 弦
"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 9.15771741780163
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.0001427418518006051
Variable 'c' has wrong value. Expected: 205/4, Actual: 9.40771741780163"""
