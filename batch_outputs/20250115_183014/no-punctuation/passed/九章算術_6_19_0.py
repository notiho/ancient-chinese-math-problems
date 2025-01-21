"""
今有鳧起南海七日至北海鴈起北海九日至南海今鳧鴈俱起問何日相逢
術曰并日數為法日數相乘為實實如法得一日
荅曰 a日 
"""

"""
Suppose a duck starts flying from the South Sea and takes 7 days to reach the North Sea.
A wild goose starts flying from the North Sea and takes 9 days to reach the South Sea.
Question: on which day will they meet if they start at the same time?

The procedure says: Add the number of days together to form the divisor.
Multiply the number of days together to form the dividend.
Divide the dividend by the divisor to obtain the number of days.

Answer: they meet on *a* day.
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
a = Fraction(實, 法)
"""
"""
