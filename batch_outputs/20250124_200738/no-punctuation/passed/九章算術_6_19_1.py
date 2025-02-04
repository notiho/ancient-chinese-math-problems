"""
今有鳧起南海七日至北海鴈起北海九日至南海今鳧鴈俱起問何日相逢
術曰并日數為法日數相乘為實實如法得一日
荅曰 a日 
"""

#----- content starts here -----
"""
Suppose there is a duck that takes 7 days to travel from the South Sea to the North Sea, and a goose that takes 9 days to travel from the North Sea to the South Sea.
If the duck and the goose start traveling toward each other at the same time, 
Question: how many days will it take for them to meet?

The procedure says: Add the days of travel for both as the divisor.
Multiply the days of travel for both as the dividend.
Divide the dividend by the divisor to obtain the number of days.

The answer says: *a* days.
"""

# 鳧起南海七日
鳧日數 = 7

# 鴈起北海九日
鴈日數 = 9

# 并日數為法
法 = 鳧日數 + 鴈日數

# 日數相乘為實
實 = 鳧日數 * 鴈日數

# 實如法得一日
a = Fraction(實, 法)#----- content ends here -----

"""
"""
