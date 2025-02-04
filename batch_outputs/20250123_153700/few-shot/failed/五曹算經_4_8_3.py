"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a pile of millet on flat ground with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 30 chi, multiply it by itself, obtaining 900 chi².
Multiply this by the height of 4 chi, obtaining 3600 chi³.
Divide this by 36, obtaining 100 chi³.
Divide this by the hu-divisor, which is 1 chi 6 cun 2 fen (1.62 chi), and the result is obtained.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi: 1丈 = 10尺)
下周 = 3 * 10  # in chi

# 高四尺
高 = 4  # in chi

# 斛法一尺六寸二分 (convert to chi: 1尺 = 10寸, 1寸 = 10分)
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # in chi

# 列下周三十尺自相乘得九百尺
底積 = 下周 * 下周  # in chi²

# 以高四尺乘之得三千六百尺
體積 = 底積 * 高  # in chi³

# 以三十六除之得一百尺
體積簡化 = Fraction(體積, 36)  # in chi³

# 以斛法一尺六寸二分除之即得
粟量 = Fraction(體積簡化, 斛法)  # in hu

# 分解為整斛和分
a = int(粟量)  # 整斛
b = (粟量 - a) * 100  # 分 (convert fractional part to fen)

a, b  # Answer in hu and fen
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 5900/81"""
