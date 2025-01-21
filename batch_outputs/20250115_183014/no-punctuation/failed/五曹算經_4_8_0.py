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
Divide this by the dou-measure of 1 chi 6 cun 2 fen (1.62 chi), obtaining the result.

Answer: *a* dou and *b* fen.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺
高 = 4

# 列下周三十尺，自相乘得九百尺
積基 = 下周 * 下周

# 以高四尺乘之，得三千六百尺
積體積 = 積基 * 高

# 以三十六除之，得一百尺
積體積 = Fraction(積體積, 36)

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)

# 以斛法除之，即得
總斛 = 積體積 / 斛法

# 整數部分為斛
a = int(總斛)

# 餘數部分為分
b = (總斛 - a) * 100  # Convert fractional part to fen

a = Fraction(a)
b = Fraction(int(b))  # Ensure b is an integer fraction
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 72"""
