"""
假令有句股相乘冪七百六十五分之一弦多於句三十六十分之九問三事各多少
術曰冪自乘倍多數而一為實半多數為廉法從開立方除之即句以弦多句加之即弦以句除冪即股
答曰句 a 股 b 弦 c 
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the base (ju) and height (gu) is 1/765 of the square of the hypotenuse (xian).
The hypotenuse exceeds the base by 9/36 (or 1/4).
Question: What are the lengths of the base (ju), height (gu), and hypotenuse (xian)?

The procedure says: 
1. Take the square of the hypotenuse, multiply it by itself, and double the excess amount (the difference between the hypotenuse and the base), then add 1 to form the dividend.
2. Take half of the excess amount as the divisor.
3. Perform cube root extraction on the result to obtain the base (ju).
4. Add the excess amount to the base to obtain the hypotenuse (xian).
5. Divide the square of the hypotenuse by the base to obtain the height (gu).

Answer: The base is *a*, the height is *b*, and the hypotenuse is *c*.
"""

from fractions import Fraction

# 冪 (hypotenuse squared) is given as 1/765
冪 = Fraction(1, 765)

# 弦多於句 (hypotenuse exceeds base) by 36分之9 (or 1/4)
多數 = Fraction(9, 36)

# 冪自乘倍多數而一為實
實 = 冪 * 冪 * (2 * 多數 + 1)

# 半多數為廉法
廉法 = 多數 / 2

# 從開立方除之即句
句 = 實 ** (1 / 3) / 廉法

# 以弦多句加之即弦
弦 = 句 + 多數

# 以句除冪即股
股 = 冪 / 句

a = 句
b = 股
c = 弦#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 287/20, Actual: 0.1094828556377865
Variable 'b' has wrong value. Expected: 246/5, Actual: 0.01193967342985984
Variable 'c' has wrong value. Expected: 205/4, Actual: 0.3594828556377865"""
