"""
今有平地聚粟下周三丈高四尺問粟㡬何
術曰列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

"""
Suppose there is a flat ground with a pile of millet. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

The procedure says: Place the base circumference as 30 chi. Multiply it by itself, obtaining 900 chi².
Multiply this by the height of 4 chi, obtaining 3600 chi³.
Divide this by 36, obtaining 100 chi³.
Divide this by the hu-divisor, which is 1 chi 6 cun 2 fen (1.62 chi), and the result is the amount of millet.

The answer says: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1丈 = 10尺

# 高四尺
高 = 4

# 列下周三十尺，自相乘得九百尺
積 = 下周 * 下周

# 以高四尺乘之，得三千六百尺
體積 = 積 * 高

# 以三十六除之，得一百尺
體積 = Fraction(體積, 36)

# 斛法一尺六寸二分 (convert to chi: 1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)

# 以斛法除之，即得
粟 = Fraction(體積, 斛法)

# 分解為斛和分
a = 粟.numerator // 粟.denominator  # 整斛數
b = 粟.numerator % 粟.denominator  # 剩餘分數部分

a斛 = a
b分 = Fraction(b, 粟.denominator)  # 剩餘部分以分數表示
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 59"""
