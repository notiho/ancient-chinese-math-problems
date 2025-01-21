"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一、十二分步之一。求田一畝，問︰從幾何？
術曰：下有一十二分，以一為八萬三千一百六十，半為四萬一千五百八十，三分之一為二萬七千七百二十，四分之一為二萬七百九十，五分之一為一萬六千六百三十二，六分之一為一萬三千八百六十，七分之一為一萬一千八百八十，八分之一為一萬三百九十五，九分之一為九千二百四十，一十分之一為八千三百一十六十一分之一為七千五百六十，十二分之一為六千九百三十，并之得二十五萬八千六十三，以為法。置田二百四十步，亦以一為八萬三千一百六十乘之，為實。實如法得從步。
荅曰： a(=6652800/86021)步 。
"""

"""
Suppose there is a field with a width of 1 bu, plus 1/2 bu, plus 1/3 bu, plus 1/4 bu, plus 1/5 bu, plus 1/6 bu, plus 1/7 bu, plus 1/8 bu, plus 1/9 bu, plus 1/10 bu, plus 1/11 bu, plus 1/12 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is a denominator of 12. Take 1 as 83160, 1/2 as 41580, 1/3 as 27720, 1/4 as 20790, 1/5 as 16632, 1/6 as 13860, 1/7 as 11880, 1/8 as 10395, 1/9 as 9240, 1/10 as 8316, 1/11 as 7560, and 1/12 as 6930. Add these, obtaining 258063 as the divisor. Place the field of 240 bu, and also multiply it by taking 1 as 83160, giving the dividend. Do the division, obtaining the number of steps of the length.

The answer says: *a*(=6652800/86021) bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一、十一分步之一、十二分步之一
廣 = Fraction(1, 1) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9) + Fraction(1, 10) + Fraction(1, 11) + Fraction(1, 12)

# 以一為八萬三千一百六十
一 = 83160

# 半為四萬一千五百八十
半 = 41580

# 三分之一為二萬七千七百二十
三分之一 = 27720

# 四分之一為二萬七百九十
四分之一 = 20790

# 五分之一為一萬六千六百三十二
五分之一 = 16632

# 六分之一為一萬三千八百六十
六分之一 = 13860

# 七分之一為一萬一千八百八十
七分之一 = 11880

# 八分之一為一萬三百九十五
八分之一 = 10395

# 九分之一為九千二百四十
九分之一 = 9240

# 一十分之一為八千三百一十六
一十分之一 = 8316

# 十一分之一為七千五百六十
十一分之一 = 7560

# 十二分之一為六千九百三十
十二分之一 = 6930

# 并之得二十五萬八千六十三，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一 + 九分之一 + 一十分之一 + 十一分之一 + 十二分之一

# 置田二百四十步
田 = 240

# 亦以一為八萬三千一百六十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法) # 6652800/86021
"""
"""
