"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
術曰：置周二百八十六尺，自相乘得八萬一千七百九十六尺，以深三丈六尺乘之，得二百九十四萬四千六百五十六；以一十二除之，得二十四萬五千三百八十八尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular pit with a circumference of 286 chi and a depth of 3 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 286 chi, square it to get 81796 chi².
Multiply this by the depth of 3 zhang 6 chi (which is 36 chi), obtaining 2944656 chi³.
Divide this by 12, obtaining 245388 chi³.
Finally, divide by the volume of 1 hu, which is 1 chi 6 cun 2 fen (1.62 chi³), to get the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周二百八十六尺
周 = 286

# 深三丈六尺 (1 丈 = 10 尺)
深 = 3 * 10 + 6  # Convert to chi

# 置周二百八十六尺，自相乘得八萬一千七百九十六尺
周平方 = 周 ** 2

# 以深三丈六尺乘之，得二百九十四萬四千六百五十六
體積 = 周平方 * 深

# 以一十二除之
體積除以十二 = Fraction(體積, 12)

# 斛法一尺六寸二分 (1 尺 6 寸 2 分 = 1.62 尺³)
斛法 = Fraction(162, 100)  # Convert to fractional form

# 以斛法除之，即得
a = Fraction(體積除以十二, 斛法)

# Final result
a#----- content ends here -----

"""
"""
