"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
術曰：置周二百八十六尺，自相乘得八萬一千七百九十六尺，以深三丈六尺乘之，得二百九十四萬四千六百五十六；以一十二除之，得二十四萬五千三百八十八尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular silo with a circumference of 286 chi and a depth of 3 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 286 chi, square it to get 81796 chi².
Multiply this by the depth of 3 zhang 6 chi to get 2944656 chi³.
Divide this by 12 to get 245388 chi³.
Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen) to get the number of hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周二百八十六尺
周 = 286  # chi

# 深三丈六尺
深 = 3 * 10 + 6  # Convert zhang and chi to chi (1 zhang = 10 chi)

# 置周二百八十六尺，自相乘得八萬一千七百九十六尺
周平方 = 周 ** 2  # chi²

# 以深三丈六尺乘之，得二百九十四萬四千六百五十六
體積 = 周平方 * 深  # chi³

# 以一十二除之
體積除以十二 = Fraction(體積, 12)  # chi³

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # chi³ per hu

# 即得
a = Fraction(體積除以十二, 斛法)  # hu

a#----- content ends here -----

"""
"""
