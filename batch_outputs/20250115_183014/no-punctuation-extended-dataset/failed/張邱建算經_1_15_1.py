"""
今有女善織日益功疾初日織五尺今一月日織九疋三丈問日益㡬何
術曰置今織尺數以一月日而一所得倍之又倍初日尺數減之餘為實以一月日數初一日減之餘為法實如法得一
答曰 a寸
"""

"""
Suppose there is a woman skilled in weaving, whose daily weaving increases in speed. On the first day, she weaves 5 chi. By the end of one month, she weaves a total of 9 pi and 3 zhang.
Question: by how much does her daily weaving increase?

The procedure says: Place the total number of chi woven in one month. Multiply it by twice the number of days in one month, and then also double the number of chi woven on the first day. Subtract the latter from the former, and the remainder is the dividend.
Take the number of days in one month, subtract the first day, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the daily increase.

Answer: *a* cun.
"""

# 初日織五尺
初日織 = 5

# 一月日數
一月日數 = 30

# 今一月日織九疋三丈
# 1 疋 = 4 丈, 1 丈 = 10 尺
一月織 = 9 * 4 * 10 + 3 * 10  # Convert to chi

# 置今織尺數，以一月日而一所得倍之
實 = 2 * 一月日數 * 一月織

# 又倍初日尺數，減之
實 -= 2 * 初日織

# 餘為實，以一月日數初一日減之
法 = 一月日數 - 1

# 餘為法，實如法得一
a = Fraction(實, 法) / 10  # Convert chi to cun (1 chi = 10 cun)
"""
Variable 'a' has wrong value. Expected: 160/29, Actual: 2339/29"""
