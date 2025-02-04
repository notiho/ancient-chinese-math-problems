"""
今有築牆上廣二尺下廣六尺髙二丈今已築上廣三尺六寸問已築髙㡬何
術曰置已築上廣及下廣各減牆上廣以築上廣減餘以減下廣減餘餘乗牆髙為實以牆上廣減下廣餘為法實如法而一
答曰 a丈
"""

"""
Suppose there is a wall with a top width of 2 chi, a bottom width of 6 chi, and a height of 2 zhang.
Now, the top width of the already built portion is 3 chi and 6 cun.
Question: how tall is the already built portion?

The procedure says: Place the already built top width and the bottom width.
Each subtracts the top width of the wall.
Subtract the remainder of the already built top width from the remainder of the bottom width.
Multiply the result by the height of the wall to obtain the dividend.
Subtract the bottom width from the top width of the wall to obtain the divisor.
Divide the dividend by the divisor to obtain the height of the already built portion.

The answer says: *a* zhang.
"""

# 上廣二尺
牆上廣 = 2

# 下廣六尺
牆下廣 = 6

# 高二丈
牆高 = 2

# 已築上廣三尺六寸 (convert to chi: 6 cun = 0.6 chi)
已築上廣 = 3 + Fraction(6, 10)

# 置已築上廣及下廣，各減牆上廣
已築上廣減 = 已築上廣 - 牆上廣
牆下廣減 = 牆下廣 - 牆上廣

# 以築上廣減餘，以減下廣減餘
餘 = 牆下廣減 - 已築上廣減

# 餘乘牆高，為實
實 = 餘 * 牆高

# 以牆上廣減下廣餘，為法
法 = 牆上廣 - 牆下廣

# 實如法而一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
