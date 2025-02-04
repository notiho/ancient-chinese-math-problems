"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一求田一畝問從幾何
術曰下有一十分以一為二千五百二十半為一千二百六十三分之一為八百四十四分之一為六百三十五分之一為五百四六分之一為四百二十七分之一為三百六十八分之一為三百一十五九分之一為二百八十十分之一為二百五十二并之得七千三百八十一以為法置田二百四十步亦以一為二千五百二十乘之為實實如法得從步
荅曰 a步 
"""

"""
Suppose there is a field with a width of 1 bu, plus 1/2 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu, plus 1/10 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/10. Take 1 as 2520, 1/2 as 1260, 1/3 as 840, 1/4 as 630, 1/5 as 504, 1/6 as 420, 1/7 as 360, 1/8 as 315, 1/9 as 280, and 1/10 as 252.
Add these, obtaining 7381 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一
廣 = (
    1
    + Fraction(1, 2)
    + Fraction(1, 3)
    + Fraction(1, 4)
    + Fraction(1, 5)
    + Fraction(1, 6)
    + Fraction(1, 7)
    + Fraction(1, 8)
    + Fraction(1, 9)
    + Fraction(1, 10)
)

# 以一為二千五百二十
一 = 2520

# 半為一千二百六十
半 = 1260

# 三分之一為八百四十四
三分之一 = 840

# 四分之一為六百三十
四分之一 = 630

# 五分之一為五百零四
五分之一 = 504

# 六分之一為四百二十
六分之一 = 420

# 七分之一為三百六十
七分之一 = 360

# 八分之一為三百一十五
八分之一 = 315

# 九分之一為二百八十
九分之一 = 280

# 十分之一為二百五十二
十分之一 = 252

# 并之得七千三百八十一，以為法
法 = (
    一
    + 半
    + 三分之一
    + 四分之一
    + 五分之一
    + 六分之一
    + 七分之一
    + 八分之一
    + 九分之一
    + 十分之一
)

# 置田二百四十步
田 = 240

# 亦以一為二千五百二十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)
"""
"""
