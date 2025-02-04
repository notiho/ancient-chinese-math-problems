"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一求田一畝問從幾何
術曰下有七分以一為四百二十半為二百一十三分之一為一百四十四分之一為一百五五分之一為八十四六分之一為七十七分之一為六十并之得一千八十九以為法置田二百四十步亦以一為四百二十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, and 1/7 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are sevenths. Take 1 as 420, 1/2 as 210, 1/3 as 140, 1/4 as 105, 1/5 as 84, 1/6 as 70, and 1/7 as 60.
Add these, obtaining 1089 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 420, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7)

# 以一為四百二十
一 = 420

# 半為二百一十
半 = 210

# 三分之一為一百四十
三分之一 = 140

# 四分之一為一百五
四分之一 = 105

# 五分之一為八十四
五分之一 = 84

# 六分之一為七十
六分之一 = 70

# 七分之一為六十
七分之一 = 60

# 并之得一千八十九，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一

# 置田二百四十步
田 = 240

# 亦以一為四百二十，乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
