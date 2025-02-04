"""
今有圓窖周五丈四尺深一丈八尺問受粟幾何
術曰先置周五丈四尺相乘得二千九百一十六尺以深一丈八尺乘之得五萬二千四百八十八尺以一十二除之得四千三百七十四尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a circular pit with a circumference of 5 zhang and 4 chi, and a depth of 1 zhang and 8 chi.
Question: how much millet can it hold?

The procedure says: First, place the circumference of 5 zhang and 4 chi, and square it, obtaining 2916 chi.
Multiply it by the depth of 1 zhang and 8 chi, obtaining 52488 chi.
Divide it by 12, obtaining 4374 chi.
Divide it by the hu-divisor of 1 chi 6 cun 2 fen, and the result is the number of hu.

The answer says: *a* hu.
"""

from fractions import Fraction

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang to chi

# 先置周五丈四尺相乘，得二千九百一十六尺
周積 = 周 * 周

# 以深一丈八尺乘之，得五萬二千四百八十八尺
體積 = 周積 * 深

# 以一十二除之，得四千三百七十四尺
體積 = Fraction(體積, 12)

# 以斛法一尺六寸二分除之，即得
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi
a = Fraction(體積, 斛法)  # Result in hu
"""
"""
