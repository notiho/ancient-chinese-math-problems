"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a pile of millet on flat ground with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 30 chi (3 zhang = 30 chi), square it to get 900 chi².
Multiply this by the height of 4 chi to get 3600 chi³.
Divide this by 36 to get 100 chi³.
Finally, divide by the dou/hu divisor of 1 chi 6 cun 2 fen (1.62 chi) to obtain the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺
高 = 4

# 列下周三十尺自相乘得九百尺
積 = 下周 * 下周

# 以高四尺乘之得三千六百尺
體積 = 積 * 高

# 以三十六除之得一百尺
體積 = Fraction(體積, 36)

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)

# 以斛法除之即得
粟 = Fraction(體積, 斛法)

# 分解為斛和分
a = 粟.numerator // 粟.denominator  # 整斛部分
b = 粟 - a  # 剩餘分部分
b = b * 斛法.denominator  # 轉換為分

a, b = int(a), int(b)

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 36"""
