"""
今有車運麥輸太倉去三十七里十六分里之十一重車日行四十五里七日五返問空車日行㡬何
術曰置麥去太倉里數以返數乗之以重車日行里數而一所得為重行日數以減凡日數餘為空行日數以為法以返數乗麥去太倉里數為實實如法而一
答曰日行 a里
"""

#----- content starts here -----
"""
Suppose there is a cart transporting wheat to the Grand Granary, which is 37 li and 11/16 of a li away.
A loaded cart travels 45 li per day, completing 7 days and 5 round trips.
Question: how many li does the empty cart travel per day?

The procedure says:
1. Place the distance to the Grand Granary in li and multiply it by the number of round trips.
2. Divide this by the distance a loaded cart travels per day to obtain the number of days spent traveling loaded.
3. Subtract this from the total number of days to find the number of days spent traveling empty.
4. Use this as the divisor.
5. Multiply the distance to the Grand Granary by the number of round trips to obtain the dividend.
6. Divide the dividend by the divisor to find the distance the empty cart travels per day.

Answer: the empty cart travels *a* li per day.
"""

from fractions import Fraction

# 麥輸太倉去三十七里十六分里之十一
去太倉里數 = 37 + Fraction(11, 16)

# 重車日行四十五里
重車日行里數 = 45

# 七日五返
凡日數 = 7
返數 = 5

# 置麥去太倉里數，以返數乗之
總里數 = 去太倉里數 * 返數

# 以重車日行里數而一，所得為重行日數
重行日數 = Fraction(總里數, 重車日行里數)

# 以減凡日數，餘為空行日數
空行日數 = 凡日數 - 重行日數

# 以返數乗麥去太倉里數為實
實 = 去太倉里數 * 返數

# 實如法而一
a = Fraction(實, 空行日數)#----- content ends here -----

"""
"""
