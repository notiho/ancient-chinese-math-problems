"""
今有女善織日益功疾初日織五尺今一月日織九疋三丈問日益㡬何
術曰置今織尺數以一月日而一所得倍之又倍初日尺數減之餘為實以一月日數初一日減之餘為法實如法得一
答曰 a寸
"""

"""
Suppose there is a woman skilled in weaving, and her daily weaving output increases day by day.
On the first day, she weaves 5 chi. By the end of one month (30 days), she has woven 9 pi and 3 zhang.
Question: by how much does her daily weaving output increase?

The procedure says: Place the total number of chi woven now.
Multiply it by twice the number of days in one month, and also double the number of chi woven on the first day.
Subtract the latter from the former, and the remainder is the dividend.
Subtract the first day from the number of days in one month, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the daily increase.

Answer: *a* cun.
"""

# 初日織五尺
初日尺數 = 5

# 一月日數
一月日數 = 30

# 今織九疋三丈
# 1 疋 = 4 丈, 1 丈 = 10 尺
今織尺數 = 9 * 4 * 10 + 3 * 10

# 所得倍之
所得 = 2 * 一月日數 * 今織尺數

# 又倍初日尺數
倍初日尺數 = 2 * 初日尺數 * 一月日數

# 減之，餘為實
實 = 所得 - 倍初日尺數

# 以一月日數初一日減之，餘為法
法 = 一月日數 - 1

# 實如法得一
a = Fraction(實, 法) / 10  # Convert to cun (1 chi = 10 cun)
"""
Variable 'a' has wrong value. Expected: 160/29, Actual: 2310/29"""
