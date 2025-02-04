"""
今有田廣一步半、三分步之一。求田一畝，問︰從幾何？
術曰：下有三分，以一為六，半為三，三分之一為二，并之得一十一為法。置田二百四十步，亦以一為六乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of one bu, a half bu, and one-third of a bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are thirds. Take 1 as 6, a half as 3, and one-third as 2.
Add these, obtaining 11 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 6, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半、三分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3)

# 以一為六
一 = 6
# 半為三
半 = 3
# 三分之一為二
三分之一 = 2

# 并之得十一為法
法 = 一 + 半 + 三分之一

# 置田二百四十步
田 = 240

# 亦以一為六乘之，為實
實 = 6 * 田

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
