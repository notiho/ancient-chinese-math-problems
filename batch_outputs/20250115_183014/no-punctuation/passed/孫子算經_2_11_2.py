"""
今有圓窖周五丈四尺深一丈八尺問受粟幾何
術曰先置周五丈四尺相乘得二千九百一十六尺以深一丈八尺乘之得五萬二千四百八十八尺以一十二除之得四千三百七十四尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a circular pit with a circumference of 5 zhang 4 chi and a depth of 1 zhang 8 chi.
Question: how much millet can it hold?

The procedure says: First, place the circumference of 5 zhang 4 chi.
Multiply it by itself, obtaining 2916 chi².
Multiply this by the depth of 1 zhang 8 chi, obtaining 52488 chi³.
Divide this by 12, obtaining 4374 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen, and the result is the number of hu.

The answer says: *a* hu.
"""

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang to chi

# 相乘得二千九百一十六尺
周積 = 周 * 周

# 以深一丈八尺乘之
體積 = 周積 * 深

# 以一十二除之
體積 = Fraction(體積, 12)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to a single unit in chi

# 以斛法除之即得
a = Fraction(體積, 斛法)
"""
"""
