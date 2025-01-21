"""
今有平地聚粟下周三丈高四尺問粟㡬何
術曰列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

"""
Suppose there is a flat ground with a pile of millet. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference, 30 chi, and multiply it by itself, obtaining 900 chi².
Multiply this by the height, 4 chi, obtaining 3600 chi³.
Divide this by 36, obtaining 100 chi³.
Divide this by the hu-divisor, 1 chi 6 cun 2 fen (1.62 chi), to obtain the result.

Answer: *a* hu and *b* fen.
"""

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1 丈 = 10 尺

# 高四尺
高 = 4

# 列下周三十尺，自相乘，得九百尺
底積 = 下周 * 下周

# 以高四尺乘之，得三千六百尺
體積 = 底積 * 高

# 以三十六除之，得一百尺
體積 = Fraction(體積, 36)

# 斛法一尺六寸二分 (convert to chi: 1 chi + 6 cun + 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)  # 1.62 chi

# 以斛法除之，即得
總斛 = Fraction(體積, 斛法)

# 分離整斛與餘分
a = 總斛.numerator // 總斛.denominator  # 整斛
b = 總斛.numerator % 總斛.denominator  # 餘分
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 59"""
