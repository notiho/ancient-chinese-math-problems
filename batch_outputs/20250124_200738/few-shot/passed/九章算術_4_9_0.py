"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一。求田一畝，問︰從幾何？
術曰：下有一十一分，以一為二萬七千七百二十，半為一萬三千八百六十，三分之一為九千二百四十，四分之一為六千九百三十，五分之一為五千五百四十四，六分之一為四千六百二十，七分之一為三千九百六十，八分之一為三千四百六十五，九分之一為三千八十，一十分之一為二千七百七十二，一十一分之一為二千五百二十，并之得八萬三千七百一十一，以為法。置田二百四十步，亦以一為二萬七千七百二十乘之，為實。實如法得從步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu and a half, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu, plus 1/10 bu, plus 1/11 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/11. Take 1 as 27720, 1/2 as 13860, 1/3 as 9240, 1/4 as 6930, 1/5 as 5544, 1/6 as 4620, 1/7 as 3960, 1/8 as 3465, 1/9 as 3080, 1/10 as 2772, and 1/11 as 2520. Add these, obtaining 83711 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 27720, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9) + Fraction(1, 10) + Fraction(1, 11)

# 以一為二萬七千七百二十
一 = 27720

# 半為一萬三千八百六十，三分之一為九千二百四十，四分之一為六千九百三十，五分之一為五千五百四十四，六分之一為四千六百二十，七分之一為三千九百六十，八分之一為三千四百六十五，九分之一為三千八十，一十分之一為二千七百七十二，一十一分之一為二千五百二十
半 = 一 // 2
三分之一 = 一 // 3
四分之一 = 一 // 4
五分之一 = 一 // 5
六分之一 = 一 // 6
七分之一 = 一 // 7
八分之一 = 一 // 8
九分之一 = 一 // 9
十分之一 = 一 // 10
十一分之一 = 一 // 11

# 并之得八萬三千七百一十一，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一 + 九分之一 + 十分之一 + 十一分之一

# 置田二百四十步
田 = 240

# 亦以一為二萬七千七百二十乘之，為實
實 = 一 * 田

# 實如法得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
