#今有田廣一步半。求田一畝，問︰從幾何？
#術曰：下有半，是二分之一。以一為二，半為一，并之得三，為法。置田二百四十步，亦以一為二乘之，為實。實如法得從步。
#荅曰： a(=160)步 。

"""
Suppose there is a field with a width of one bu and a half. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is a half, that is, 1/2. 
Take 1 as 2, and a half as 1.
Add these, obtaining 3 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a*(=160) bu.
"""

# 廣一步半
廣 = 1 + Fraction(1, 2)

# 田一畝
田 = 1

# 以一為二
一 = 2
# 半為一
半 = 1
# 并之得三，為法
法 = 一 + 半

# 置田二百四十步
田 = 240

# 亦以一為二乘之，為實
實 = 2 * 田

# 實如法得從步
a = Fraction(實, 法) # 160
