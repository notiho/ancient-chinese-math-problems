"""
今有鳧起南海，七日至北海；鴈起北海，九日至南海。今鳧鴈俱起。問︰何日相逢？
術曰：并日數為法，日數相乘為實，實如法得一日。
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose a duck starts flying from the South Sea and takes 7 days to reach the North Sea.
A goose starts flying from the North Sea and takes 9 days to reach the South Sea.
Now, both the duck and the goose start flying at the same time.
Question: after how many days will they meet?

The procedure says: Add the number of days for both as the divisor.
Multiply the number of days for both as the dividend.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
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
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
