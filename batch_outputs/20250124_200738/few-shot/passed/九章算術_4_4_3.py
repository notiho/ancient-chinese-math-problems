"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一。求田一畝，問︰從幾何？
術曰：下有六分，以一為一百二十，半為六十，三分之一為四十，四分之一為三十，五分之一為二十四，六分之一為二十，并之得二百九十四以為法。置田二百四十步，亦以一為一百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, and 1/6 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are sixths. Take 1 as 120, 1/2 as 60, 1/3 as 40, 1/4 as 30, 1/5 as 24, and 1/6 as 20. 
Add these, obtaining 294 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 120, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6)

# 下有六分，以一為一百二十
一 = 120

# 半為六十
半 = 60

# 三分之一為四十
三分之一 = 40

# 四分之一為三十
四分之一 = 30

# 五分之一為二十四
五分之一 = 24

# 六分之一為二十
六分之一 = 20

# 并之得二百九十四以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一

# 置田二百四十步
田 = 240

# 亦以一為一百二十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
