"""
今有田廣一步半三分步之一四分步之一五分步之一六分步之一七分步之一八分步之一九分步之一十分步之一十一分步之一求田一畝問從幾何
術曰下有一十一分以一為二萬七千七百二十半為一萬三千八百六十三分之一為九千二百四十四分之一為六千九百三十五分之一為五千五百四十四六分之一為四千六百二十七分之一為三千九百六十八分之一為三千四百六十五九分之一為三千八十一十分之一為二千七百七十二一十一分之一為二千五百二十并之得八萬三千七百一十一以為法置田二百四十步亦以一為二萬七千七百二十乘之為實實如法得從步
荅曰 a步 
"""

"""
Suppose there is a field with a width of 1 bu, plus 1/2 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu, plus 1/10 bu, plus 1/11 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/11. Take 1 as 27720, 1/2 as 13860, 1/3 as 9240, 1/4 as 6930, 1/5 as 5544, 1/6 as 4620, 1/7 as 3960, 1/8 as 3465, 1/9 as 3080, 1/10 as 2772, and 1/11 as 2520.
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

# 將廣轉換為分數的共同分母
分母 = 27720  # 1 的分母為 27720
分子 = (
    27720
    + 13860
    + 9240
    + 6930
    + 5544
    + 4620
    + 3960
    + 3465
    + 3080
    + 2772
    + 2520
)

# 廣的分數表示
廣分數 = Fraction(分子, 分母)

# 以廣為法
法 = 廣分數

# 置田二百四十步
田 = 240

# 亦以一為二萬七千七百二十乘之，為實
實 = 田 * 分母

# 實如法得從步
a = Fraction(實, 分子)  # 分子來自法的分數表示

a
"""
"""
