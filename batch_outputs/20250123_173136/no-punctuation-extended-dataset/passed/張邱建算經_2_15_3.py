"""
今有車運麥輸太倉去三十七里十六分里之十一重車日行四十五里七日五返問空車日行㡬何
術曰置麥去太倉里數以返數乗之以重車日行里數而一所得為重行日數以減凡日數餘為空行日數以為法以返數乗麥去太倉里數為實實如法而一
答曰日行 a里
"""

"""
Suppose a cart is transporting wheat to the granary, which is 37 li and 11/16 of a li away.
A loaded cart travels 45 li per day. The trip takes 7 days in total, including 5 round trips.
Question: how far does the empty cart travel per day?

The procedure says: Place the distance to the granary and multiply it by the number of round trips.
Divide this by the distance a loaded cart travels per day to obtain the number of days spent traveling loaded.
Subtract this from the total number of days to get the number of days spent traveling empty.
Use this as the divisor.
Multiply the distance to the granary by the number of round trips to get the dividend.
Divide the dividend by the divisor to obtain the daily distance traveled by the empty cart.

Answer: the empty cart travels *a* li per day.
"""

# 麥輸太倉去三十七里十六分里之十一
去太倉里數 = 37 + Fraction(11, 16)

# 重車日行四十五里
重車日行里數 = 45

# 七日
凡日數 = 7

# 五返
返數 = 5

# 置麥去太倉里數，以返數乗之
重行總里數 = 去太倉里數 * 返數

# 以重車日行里數而一，所得為重行日數
重行日數 = Fraction(重行總里數, 重車日行里數)

# 以減凡日數，餘為空行日數
空行日數 = 凡日數 - 重行日數

# 以返數乗麥去太倉里數，為實
空行總里數 = 去太倉里數 * 返數

# 實如法而一
a = Fraction(空行總里數, 空行日數)
"""
"""
