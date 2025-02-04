"""
今有七百人造浮橋九日成今增五百人問日㡬何
術曰置本人數以日數乗之為實以本人數今増人數併之為法實如法而一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there are 700 people building a floating bridge, and it is completed in 9 days.
Now, if 500 more people are added, how many days will it take?

The procedure says: Place the original number of people and multiply it by the number of days, obtaining the dividend.
Add the original number of people and the increased number of people, obtaining the divisor.
Divide the dividend by the divisor, obtaining the number of days.

Answer: *a* days.
"""

# 本人數
本人數 = 700

# 日數
日數 = 9

# 今增人數
增人數 = 500

# 置本人數以日數乗之，為實
實 = 本人數 * 日數

# 以本人數今増人數併之，為法
法 = 本人數 + 增人數

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
