"""
今有田廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一。求田一畝，問︰從幾何？
術曰：下有一十分，以一為二千五百二十，半為一千二百六十，三分之一為八百四十，四分之一為六百三十，五分之一為五百四，六分之一為四百二十，七分之一為三百六十，八分之一為三百一十五，九分之一為二百八十，十分之一為二百五十二，并之得七千三百八十一，以為法。置田二百四十步，亦以一為二千五百二十乘之，為實。實如法得從步。
荅曰： a(=604800/7381)步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 bu and 1/2 bu, 1/3 bu, 1/4 bu, 1/5 bu, 1/6 bu, 1/7 bu, 1/8 bu, 1/9 bu, and 1/10 bu.
A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is 1/10. 
Take 1 as 2520, 1/2 as 1260, 1/3 as 840, 1/4 as 630, 1/5 as 504, 1/6 as 420, 1/7 as 360, 1/8 as 315, 1/9 as 280, and 1/10 as 252.
Add these, obtaining 7381 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 2520, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a*(=604800/7381) bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一、五分步之一、六分步之一、七分步之一、八分步之一、九分步之一、十分步之一
廣 = [
    1,  # 1 bu
    Fraction(1, 2),  # 1/2 bu
    Fraction(1, 3),  # 1/3 bu
    Fraction(1, 4),  # 1/4 bu
    Fraction(1, 5),  # 1/5 bu
    Fraction(1, 6),  # 1/6 bu
    Fraction(1, 7),  # 1/7 bu
    Fraction(1, 8),  # 1/8 bu
    Fraction(1, 9),  # 1/9 bu
    Fraction(1, 10),  # 1/10 bu
]

# 以一為二千五百二十
基準 = 2520

# 計算每個部分的值
廣值 = [基準 * g for g in 廣]

# 并之得七千三百八十一，以為法
法 = sum(廣值)

# 置田二百四十步
田 = 240

# 亦以一為二千五百二十乘之，為實
實 = 田 * 基準

# 實如法得從步
a = Fraction(實, 法)  # 604800/7381

a  # Output the result#----- content ends here -----

"""
"""
