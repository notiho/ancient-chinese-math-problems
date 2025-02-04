"""
今有田廣一步半三分步之一四分步之一五分步之一求田一畝問從幾何
術曰下有五分以一為六十半為三十三分之一為二十四分之一為一十五五分之一為一十二并之得一百三十七以為法置田二百四十步亦以一為六十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, and 1/5 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/5. Take 1 as 60, 1/2 as 30, 1/3 as 20, 1/4 as 15, and 1/5 as 12.
Add these, obtaining 137 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 60, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5)

# 以一為六十
一 = 60
半 = 30  # 1/2 as 30
三分之一 = 20  # 1/3 as 20
四分之一 = 15  # 1/4 as 15
五分之一 = 12  # 1/5 as 12

# 并之得一百三十七，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一

# 置田二百四十步
田 = 240

# 亦以一為六十乘之，為實
實 = 田 * 60

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
