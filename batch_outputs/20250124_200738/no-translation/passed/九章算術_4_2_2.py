"""
今有田廣一步半、三分步之一、四分步之一。求田一畝，問︰從幾何？
術曰：下有四分，以一為一十二，半為六，三分之一為四，四分之一為三，并之得二十五，以為法。置田二百四十步，亦以一為一十二乘之，為實。實如法而一，得從步。
荅曰： a步 。
"""

#----- content starts here -----

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
實 = 田 * 12

# 實如法而一，得從步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
