"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一。求田一畝，問︰從幾何？
術曰：下有九分，以一為二千五百二十，半為一千二百六十，三分之一為八百四十，四分之一為六百三十，五分之一為五百四，六分之一為四百二十，七分之一為三百六十，八分之一為三百一十五，九分之一為二百八十，并之得七千一百二十九，以為法。置田二百四十步，亦以一為二千五百二十乘之，為實。實如法得從步。
荅曰： a(=604800/7129)步 。
"""

"""
Suppose there is a field with a width of 1 bu and 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, 1/8 bu, and 1/9 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there are ninths.
Take 1 as 2520, 1/2 as 1260, 1/3 as 840, 1/4 as 630, 1/5 as 504, 1/6 as 420, 1/7 as 360, 1/8 as 315, and 1/9 as 280.
Add these, obtaining 7129 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a*(=604800/7129) bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4) + Fraction(1, 5) + Fraction(1, 6) + Fraction(1, 7) + Fraction(1, 8) + Fraction(1, 9)

# 以一為二千五百二十
一 = 2520

# 半為一千二百六十
半 = 一 // 2

# 三分之一為八百四十
三分之一 = 一 // 3

# 四分之一為六百三十
四分之一 = 一 // 4

# 五分之一為五百四
五分之一 = 一 // 5

# 六分之一為四百二十
六分之一 = 一 // 6

# 七分之一為三百六十
七分之一 = 一 // 7

# 八分之一為三百一十五
八分之一 = 一 // 8

# 九分之一為二百八十
九分之一 = 一 // 9

# 并之得七千一百二十九，以為法
法 = 一 + 半 + 三分之一 + 四分之一 + 五分之一 + 六分之一 + 七分之一 + 八分之一 + 九分之一

# 置田二百四十步
田 = 240

# 亦以一為二千五百二十乘之，為實
實 = 田 * 一

# 實如法得從步
a = Fraction(實, 法) # 604800/7129
"""
"""
