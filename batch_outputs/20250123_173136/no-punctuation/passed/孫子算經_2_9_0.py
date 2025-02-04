"""
今有圓窖下周二百八十六尺深三丈六尺問受粟幾何
術曰置周二百八十六尺自相乘得八萬一千七百九十六尺以深三丈六尺乘之得二百九十四萬四千六百五十六以一十二除之得二十四萬五千三百八十八尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a circular pit with a circumference of 286 chi and a depth of 3 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of 286 chi, square it, obtaining 81796 chi.
Multiply it by the depth of 3 zhang 6 chi, obtaining 2944656.
Divide it by 12, obtaining 245388 chi.
Divide it by the dou-measure of 1 chi 6 cun 2 fen, and the result is the number of dou.

Answer: *a* dou.
"""

from fractions import Fraction

# 下周二百八十六尺
周 = 286

# 深三丈六尺
深 = 3 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 置周二百八十六尺，自相乘
周平方 = 周 * 周

# 以深三丈六尺乘之
積 = 周平方 * 深

# 以一十二除之
積除十二 = Fraction(積, 12)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 1 chi 6 cun 2 fen to chi

# 以斛法除之，即得
a = Fraction(積除十二, 斛法)  # Result in dou
"""
"""
