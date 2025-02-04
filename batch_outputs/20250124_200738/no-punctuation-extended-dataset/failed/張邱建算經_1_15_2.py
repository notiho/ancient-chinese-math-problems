"""
今有女善織日益功疾初日織五尺今一月日織九疋三丈問日益㡬何
術曰置今織尺數以一月日而一所得倍之又倍初日尺數減之餘為實以一月日數初一日減之餘為法實如法得一
答曰 a寸
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving, and her daily weaving increases in speed. On the first day, she weaves 5 chi. By the end of one month (30 days), she weaves a total of 9 pi and 3 zhang.
Question: by how much does her daily weaving increase?

The procedure says: Place the total number of chi woven now, and divide it by the number of days in one month. Double the result, and also double the number of chi woven on the first day. Subtract the latter from the former, and the remainder is the dividend. Subtract the first day from the number of days in one month, and the remainder is the divisor. Divide the dividend by the divisor to obtain the daily increase.

Answer: *a* cun.
"""

# 初日織五尺
初日織 = 5

# 一月日數
一月日數 = 30

# 今一月織九疋三丈
# 1 疋 = 40 尺, 1 丈 = 10 尺
今織 = 9 * 40 + 3 * 10  # Convert to chi

# 置今織尺數，以一月日而一，所得倍之
倍今織 = 2 * (今織 / 一月日數)

# 又倍初日尺數
倍初日 = 2 * 初日織

# 減之，餘為實
實 = 倍今織 - 倍初日

# 以一月日數，初一日減之，餘為法
法 = 一月日數 - 1

# 實如法得一
a = Fraction(實, 法)  # Convert to cun (1 chi = 10 cun)
a_cun = a * 10  # Convert the result to cun

a = a_cun  # Final result in cun#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
