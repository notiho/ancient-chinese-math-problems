"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一。求田一畝，問︰從幾何？
術曰：下有七分，以一為四百二十，半為二百一十，三分之一為一百四十，四分之一為一百五，五分之一為八十四，六分之一為七十，七分之一為六十，并之得一千八十九，以為法。置田二百四十步，亦以一為四百二十乘之，為實。實如法得從步。
荅曰： a(=11200/121)步 。
"""

"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, and 1/7 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is a denominator of 7. Take 1 as 420, 1/2 as 210, 1/3 as 140, 1/4 as 105, 1/5 as 84, 1/6 as 70, and 1/7 as 60. Add these, obtaining 1089 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 420, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a*(=11200/121) bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7)

# 下有七分，以一為四百二十
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

# 亦以一為四百二十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法) # 11200/121
"""
"""
