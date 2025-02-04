"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一。求田一畝，問︰從幾何？
術曰：下有八分，以一為八百四十，半為四百二十，三分之一為二百八十，四分之一為二百一十，五分之一為一百六十八，六分之一為一百四十，七分之一為一百二十，八分之一為一百五，并之得二千二百八十三，以為法。置田二百四十步，亦以一為八百四十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, and 1/8 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/8. Take 1 as 840, 1/2 as 420, 1/3 as 280, 1/4 as 210, 1/5 as 168, 1/6 as 140, 1/7 as 120, and 1/8 as 105.
Add these, obtaining 2283 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 840, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8)

# 以一為八百四十
一 = 840

# 半為四百二十
半 = 420

# 三分之一為二百八十
三分之一 = 280

# 四分之一為二百一十
四分之一 = 210

# 五分之一為一百六十八
五分之一 = 168

# 六分之一為一百四十
六分之一 = 140

# 七分之一為一百二十
七分之一 = 120

# 八分之一為一百五
八分之一 = 105

# 并之得二千二百八十三，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一

# 置田二百四十步
田 = 240

# 亦以一為八百四十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
