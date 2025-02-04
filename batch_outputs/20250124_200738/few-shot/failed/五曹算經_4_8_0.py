"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground, with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 30 chi (3 zhang = 30 chi), square it to get 900 chi².
Multiply this by the height of 4 chi, obtaining 3600 chi³.
Divide by 36, obtaining 100 chi³.
Finally, divide by the dou-measurement of 1 chi 6 cun 2 fen (1.62 chi³), obtaining the result.

Answer: *a* dou and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1 zhang = 10 chi

# 高四尺
高 = 4

# 列下周三十尺自相乘得九百尺
下周平方 = 下周 * 下周

# 以高四尺乘之得三千六百尺
體積 = 下周平方 * 高

# 以三十六除之得一百尺
體積除以三十六 = Fraction(體積, 36)

# 以斛法一尺六寸二分除之即得
斛法 = Fraction(162, 100)  # 1 chi 6 cun 2 fen = 1.62 chi³
粟量 = Fraction(體積除以三十六, 斛法)

# 分離整數部分和分數部分
a = 粟量.numerator // 粟量.denominator  # 整數部分 (a斛)
b = 粟量 - a  # 剩餘部分 (b分)
b = b * 100  # 轉換為百分制 (b分)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 5900/81"""
