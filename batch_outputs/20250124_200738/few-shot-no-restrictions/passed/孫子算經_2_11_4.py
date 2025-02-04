"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
術曰：先置周五丈四尺相乘，得二千九百一十六尺，以深一丈八尺乘之，得五萬二千四百八十八尺；以一十二除之，得四千三百七十四尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular granary with a circumference of 5 zhang and 4 chi, and a depth of 1 zhang and 8 chi.
Question: how much millet can it hold?

The procedure says: First, take the circumference (5 zhang and 4 chi) and square it, obtaining 2916 chi².
Then, multiply it by the depth (1 zhang and 8 chi), obtaining 52488 chi³.
Divide this by 12, obtaining 4374 chi³.
Finally, divide it by the volume of 1 hu (1 chi 6 cun 2 fen), obtaining the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 周五丈四尺
周 = 5 * 10 + 4  # Convert zhang to chi (1 zhang = 10 chi)

# 深一丈八尺
深 = 1 * 10 + 8  # Convert zhang to chi

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to a single unit in chi

# 先置周五丈四尺相乘，得二千九百一十六尺
周平方 = 周 ** 2

# 以深一丈八尺乘之，得五萬二千四百八十八尺
體積 = 周平方 * 深

# 以一十二除之，得四千三百七十四尺
體積 = Fraction(體積, 12)

# 以斛法一尺六寸二分除之，即得
a = Fraction(體積, 斛法)

# Output the result
a#----- content ends here -----

"""
"""
