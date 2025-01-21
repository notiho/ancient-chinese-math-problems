"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
術曰：先置周五丈四尺相乘，得二千九百一十六尺，以深一丈八尺乘之，得五萬二千四百八十八尺；以一十二除之，得四千三百七十四尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
Suppose there is a circular pit with a circumference of 5 zhang and 4 chi, and a depth of 1 zhang and 8 chi.
Question: how much millet can it hold?

The procedure says: First, take the circumference of 5 zhang and 4 chi, multiply it by itself, obtaining 2916 chi.
Multiply this by the depth of 1 zhang and 8 chi, obtaining 52488 chi.
Divide this by 12, obtaining 4374 chi.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a* hu.
"""

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang to chi

# 先置周五丈四尺相乘，得二千九百一十六尺
積1 = 周 * 周

# 以深一丈八尺乘之，得五萬二千四百八十八尺
積2 = 積1 * 深

# 以一十二除之，得四千三百七十四尺
積3 = Fraction(積2, 12)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi

# 以斛法除之，即得
a = Fraction(積3, 斛法)  # Result in hu
"""
"""
