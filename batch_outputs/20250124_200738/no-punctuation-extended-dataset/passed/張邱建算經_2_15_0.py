"""
今有車運麥輸太倉去三十七里十六分里之十一重車日行四十五里七日五返問空車日行㡬何
術曰置麥去太倉里數以返數乗之以重車日行里數而一所得為重行日數以減凡日數餘為空行日數以為法以返數乗麥去太倉里數為實實如法而一
答曰日行 a里
"""

#----- content starts here -----
"""
Suppose there is a cart transporting wheat to the Grand Granary, which is 37 li and 11/16 of a li away. 
A loaded cart travels 45 li per day, completing 7 days and 5 round trips. 
Question: how far does the empty cart travel per day?

The procedure says: Place the distance to the Grand Granary multiplied by the number of round trips.
Multiply this by the distance a loaded cart travels per day, and divide by 1, obtaining the number of days for loaded travel.
Subtract this from the total number of days, leaving the number of days for empty travel.
Take this as the divisor.
Multiply the distance to the Grand Granary by the number of round trips, obtaining the dividend.
Divide the dividend by the divisor.

Answer: the empty cart travels *a* li per day.
"""

from fractions import Fraction

# 麥輸太倉去三十七里十六分里之十一
太倉距離 = 37 + Fraction(11, 16)

# 重車日行四十五里
重車日行 = 45

# 七日五返
總日數 = 7
返數 = 5

# 置麥去太倉里數以返數乗之
總距離 = 太倉距離 * 返數

# 以重車日行里數而一所得為重行日數
重行日數 = Fraction(總距離, 重車日行)

# 以減凡日數餘為空行日數
空行日數 = 總日數 - 重行日數

# 以為法
法 = 空行日數

# 以返數乗麥去太倉里數為實
實 = 太倉距離 * 返數

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
