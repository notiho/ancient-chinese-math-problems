"""
今有鳧起南海，七日至北海；鴈起北海，九日至南海。今鳧鴈俱起。問︰何日相逢？
術曰：并日數為法，日數相乘為實，實如法得一日。
荅曰： a(=63/16)日 。
"""

#----- content starts here -----
"""
Suppose there is a duck starting from the South Sea, taking 7 days to reach the North Sea; and a goose starting from the North Sea, taking 9 days to reach the South Sea.
Now, both the duck and the goose start at the same time.
Question: after how many days will they meet?

The procedure says: Add the days together to form the divisor.
Multiply the days together to form the dividend.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a*(=63/16) days.
"""

# 鳧起南海，七日至北海
鳧日數 = 7

# 鴈起北海，九日至南海
鴈日數 = 9

# 并日數為法
法 = 鳧日數 + 鴈日數

# 日數相乘為實
實 = 鳧日數 * 鴈日數

# 實如法得一日
a = Fraction(實, 法) # 63/16#----- content ends here -----

"""
"""
