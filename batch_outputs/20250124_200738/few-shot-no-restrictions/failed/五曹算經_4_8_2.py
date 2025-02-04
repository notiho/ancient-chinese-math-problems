"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 30 chi (3 zhang = 30 chi), square it to get 900 chi².
Multiply this by the height of 4 chi to get 3600 chi³.
Divide this by 36 to get 100 chi³.
Finally, divide by the volume of 1 hu (1 hu = 1 chi³ 6 cun 2 fen = 1.62 chi³) to obtain the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1 zhang = 10 chi

# 高四尺
高 = 4  # in chi

# 斛法：1斛 = 1尺6寸2分 = 1.62尺³
斛法 = Fraction(162, 100)  # 1.62 as a fraction

# 列下周三十尺自相乘得九百尺
基面積 = 下周 ** 2  # in chi²

# 以高四尺乘之得三千六百尺
體積 = 基面積 * 高  # in chi³

# 以三十六除之得一百尺
體積_錐形 = Fraction(體積, 36)  # Divide by 36 for the cone formula

# 以斛法除之即得
粟量 = 體積_錐形 / 斛法  # Divide by the volume of 1 hu

# Separate into hu and fen
a = int(粟量)  # Whole hu
b = (粟量 - a) * 100  # Remaining fraction in fen

# Final result
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 5900/81"""
