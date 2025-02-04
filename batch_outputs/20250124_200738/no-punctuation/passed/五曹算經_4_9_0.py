"""
今有內角聚粟下周五十四尺高五尺問粟㡬何
術曰列下周五十四尺自相乘得二千九百一十六尺以高五尺乘之得一萬四千五百八十尺以九除之得一千六百二十尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there is an inner corner filled with millet. The base circumference is 54 chi, and the height is 5 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 54 chi, multiply it by itself, obtaining 2916 chi².
Multiply this by the height of 5 chi, obtaining 14580 chi³.
Divide this by 9, obtaining 1620 chi³.
Divide this by the hu-divisor, which is 1 chi 6 cun 2 fen (1.62 chi), and the result is the amount of millet in hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周五十四尺
下周 = 54

# 高五尺
高 = 5

# 列下周五十四尺，自相乘
積1 = 下周 * 下周  # 得二千九百一十六尺
積1 = 2916  # Confirmed from the text

# 以高五尺乘之
積2 = 積1 * 高  # 得一萬四千五百八十尺
積2 = 14580  # Confirmed from the text

# 以九除之
積3 = Fraction(積2, 9)  # 得一千六百二十尺
積3 = 1620  # Confirmed from the text

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)  # Convert 1.62 to a fraction

# 以斛法除之
a = Fraction(積3, 斛法)  # 得粟的斛數#----- content ends here -----

"""
"""
