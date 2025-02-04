"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一求田一畝問從幾何
術曰下有六分以一為一百二十半為六十三分之一為四十四分之一為三十五分之一為二十四六分之一為二十并之得二百九十四以為法置田二百四十步亦以一為一百二十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, and 1/6 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/6. Take 1 as 120, 1/2 as 60, 1/3 as 40, 1/4 as 30, 1/5 as 24, and 1/6 as 20.
Add these, obtaining 294 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 120, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一六分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6)

# 以一為一百二十
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

# 并之得二百九十四，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一

# 置田二百四十步
田 = 240

# 亦以一為一百二十，乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
