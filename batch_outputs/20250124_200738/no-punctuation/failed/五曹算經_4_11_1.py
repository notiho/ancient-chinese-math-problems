"""
今有外角聚粟下周四十八尺高六尺問粟㡬何
術曰列下周四十八尺自相乘得二千三百四尺以高六尺乘之得一萬三千八百二十四尺以二十七除之得五百一十二尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

#----- content starts here -----
"""
Suppose there is an external granary filled with millet. Its base circumference is 48 chi, and its height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 48 chi, multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen (which is 1.62 chi), obtaining the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘
積 = 下周 * 下周  # 得二千三百四尺
積 = 2304  # Confirmed value

# 以高六尺乘之
體積 = 積 * 高  # 得一萬三千八百二十四尺
體積 = 13824  # Confirmed value

# 以二十七除之
體積_斛單位 = Fraction(體積, 27)  # 得五百一十二尺
體積_斛單位 = 512  # Confirmed value

# 以斛法一尺六寸二分除之
斛法 = Fraction(162, 100)  # 1 chi 6 cun 2 fen = 1.62 chi
粟量 = Fraction(體積_斛單位, 斛法)

# 分解為整斛與分
a = int(粟量)  # 整斛
b = (粟量 - a) * 100  # 剩餘部分轉為分 (百分制)

a = a  # Final value for hu
b = round(b)  # Final value for fen#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 5"""
