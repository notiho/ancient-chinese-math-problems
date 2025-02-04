"""
今有女善織日益功疾初日織五尺今一月日織九疋三丈問日益㡬何
術曰置今織尺數以一月日而一所得倍之又倍初日尺數減之餘為實以一月日數初一日減之餘為法實如法得一
答曰 a寸
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving, and her daily weaving output increases day by day. 
On the first day, she weaves 5 chi. By the end of one month (30 days), she weaves 9 pi and 3 zhang in total.
Question: how much does her daily weaving output increase?

The procedure says: Place the total number of chi woven in the month. 
Multiply it by twice the number of days in the month, then subtract twice the chi woven on the first day. 
The remainder is the dividend.
Take the number of days in the month, subtract 1, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the daily increase.

Answer: *a* cun.
"""

# 初日織五尺
初日尺數 = 5

# 一月日數
一月日數 = 30

# 今一月織九疋三丈
# 1 疋 = 4 丈, 1 丈 = 10 尺
一月總織尺數 = 9 * 4 * 10 + 3 * 10

# 置今織尺數，以一月日而一所得倍之
實 = 2 * 一月總織尺數

# 又倍初日尺數，減之
實 -= 2 * 初日尺數

# 餘為實
實 = 實

# 以一月日數，初一日減之，餘為法
法 = 一月日數 - 1

# 實如法得一
a = Fraction(實, 法)

# Convert to cun (1 chi = 10 cun)
a寸 = a * 10
a寸#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 160/29, Actual: 770/29"""
