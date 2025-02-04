"""
今有鳧起南海七日至北海鴈起北海九日至南海今鳧鴈俱起問何日相逢
術曰并日數為法日數相乘為實實如法得一日
荅曰 a日 
"""

"""
Suppose a duck starts flying from the South Sea and takes 7 days to reach the North Sea.
A wild goose starts flying from the North Sea and takes 9 days to reach the South Sea.
If both start flying at the same time, question: after how many days will they meet?

The procedure says: Add the days of both as the divisor.
Multiply the days of both as the dividend.
Divide the dividend by the divisor to find the number of days.

Answer: *a* days.
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
