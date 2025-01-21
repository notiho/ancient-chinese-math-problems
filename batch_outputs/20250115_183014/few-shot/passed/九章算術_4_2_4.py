"""
今有田廣一步半、三分步之一、四分步之一。求田一畝，問︰從幾何？
術曰：下有四分，以一為一十二，半為六，三分之一為四，四分之一為三，并之得二十五，以為法。置田二百四十步，亦以一為一十二乘之，為實。實如法而一，得從步。
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 1 bu, 1/2 bu, 1/3 bu, and 1/4 bu. A field of 1 mu is sought.
Question: how large is the length?

The procedure says: Below, there is a denominator of 4. Take 1 as 12, 1/2 as 6, 1/3 as 4, and 1/4 as 3.
Add these, obtaining 25 as the divisor.
Place the field of 240 bu, and also multiply it by taking 1 as 12, giving the dividend.
Do the division, obtaining the number of steps of the length.

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣一步半、三分步之一、四分步之一
廣 = 1 + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 4)

# 下有四分，以一為一十二
一 = 12

# 半為六
半 = 6

# 三分之一為四
三分之一 = 4

# 四分之一為三
四分之一 = 3

# 并之得二十五，以為法
法 = 一 + 半 + 三分之一 + 四分之一

# 置田二百四十步
田 = 240

# 亦以一為一十二乘之，為實
實 = 12 * 田

# 實如法而一，得從步
a = Fraction(實, 法)
"""
"""
