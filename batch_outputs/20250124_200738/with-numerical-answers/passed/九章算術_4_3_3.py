"""
今有田廣一步半、三分步之一、四分步之一、五分步之一。求田一畝，問︰從幾何？
術曰：下有五分，以一為六十，半為三十，三分之一為二十，四分之一為一十五，五分之一為一十二，并之得一百三十七，以為法。置田二百四十步，亦以一為六十乘之，為實。實如法得從步。
荅曰： a(=14400/137)步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of one bu, a half bu, one-third bu, one-fourth bu, and one-fifth bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is one-fifth. Take 1 as 60, a half as 30, one-third as 20, one-fourth as 15, and one-fifth as 12.
Add these, obtaining 137 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 60, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a*(=14400/137) bu.
"""

# 廣一步半、三分步之一、四分步之一、五分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5)

# 以一為六十
一 = 60
# 半為三十
半 = 30
# 三分之一為二十
三分之一 = 20
# 四分之一為十五
四分之一 = 15
# 五分之一為十二
五分之一 = 12

# 并之得一百三十七，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一

# 置田二百四十步
田 = 240

# 亦以一為六十乘之，為實
實 = 田 * 60

# 實如法得從步
a = Fraction(實, 法) # 14400/137#----- content ends here -----

"""
"""
