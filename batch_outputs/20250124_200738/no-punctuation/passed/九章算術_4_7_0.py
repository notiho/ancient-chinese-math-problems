"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一求田一畝問從幾何
術曰下有九分以一為二千五百二十半為一千二百六十三分之一為八百四十四分之一為六百三十五分之一為五百四六分之一為四百二十七分之一為三百六十八分之一為三百一十五九分之一為二百八十并之得七千一百二十九以為法置田二百四十步亦以一為二千五百二十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, 1/8 bu, and 1/9 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are ninths.
Take 1 as 2520, half as 1260, thirds as 840, fourths as 630, fifths as 504, sixths as 420, sevenths as 360, eighths as 315, and ninths as 280.
Add these, obtaining 7129 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9)

# 以一為2520
一 = 2520

# 半為1260
半 = 1260

# 三分之一為840
三分之一 = 840

# 四分之一為630
四分之一 = 630

# 五分之一為504
五分之一 = 504

# 六分之一為420
六分之一 = 420

# 七分之一為360
七分之一 = 360

# 八分之一為315
八分之一 = 315

# 九分之一為280
九分之一 = 280

# 并之得7129，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一 + 九分之一

# 置田二百四十步
田 = 240

# 亦以一為2520乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
