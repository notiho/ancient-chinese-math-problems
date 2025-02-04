"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一求田一畝問從幾何
術曰下有一十一分以一為二萬七千七百二十半為一萬三千八百六十三分之一為九千二百四十四分之一為六千九百三十五分之一為五千五百四十四六分之一為四千六百二十七分之一為三千九百六十八分之一為三千四百六十五九分之一為三千八十一十分之一為二千七百七十二一十一分之一為二千五百二十并之得八萬三千七百一十一以為法置田二百四十步亦以一為二萬七千七百二十乘之為實實如法得從步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu, plus 1/2 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu, plus 1/10 bu, plus 1/11 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/11. Take 1 as 27720, and 1/2 as 13860, 1/3 as 9240, 1/4 as 6930, 1/5 as 5544, 1/6 as 4620, 1/7 as 3960, 1/8 as 3465, 1/9 as 3080, 1/10 as 2772, and 1/11 as 2520.
Add these, obtaining 83711 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 27720, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一
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
    + Fraction(1, 11)
)

# 以一為二萬七千七百二十
一 = 27720

# 半為一萬三千八百六十
半 = 13860

# 三分之一為九千二百四十四
三分之一 = 9240

# 四分之一為六千九百三十
四分之一 = 6930

# 五分之一為五千五百四十四
五分之一 = 5544

# 六分之一為四千六百二十
六分之一 = 4620

# 七分之一為三千九百六十
七分之一 = 3960

# 八分之一為三千四百六十五
八分之一 = 3465

# 九分之一為三千零八十
九分之一 = 3080

# 十分之一為二千七百七十二
十分之一 = 2772

# 十一分之一為二千五百二十
十一分之一 = 2520

# 并之得八萬三千七百一十一，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一 + 九分之一 + 十分之一 + 十一分之一

# 置田二百四十步
田 = 240

# 亦以一為二萬七千七百二十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
