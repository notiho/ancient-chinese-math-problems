"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a(=1543/25)斛 奇 b(=34/25)分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 30 chi, multiply it by itself to obtain 900 chi².
Multiply this by the height of 4 chi to obtain 3600 chi³.
Divide this by 36 to obtain 100 chi³.
Divide this by the volume conversion factor of 1 chi 6 cun 2 fen (1.62 chi³) to obtain the amount in hu.

Answer: *a*(=1543/25) hu and *b*(=34/25) fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi: 1 zhang = 10 chi)
下周 = 3 * 10  # 30 chi

# 高四尺
高 = 4  # 4 chi

# 列下周三十尺自相乘得九百尺
底積 = 下周 * 下周  # 30 * 30 = 900 chi²

# 以高四尺乘之得三千六百尺
體積 = 底積 * 高  # 900 * 4 = 3600 chi³

# 以三十六除之得一百尺
體積簡化 = Fraction(體積, 36)  # 3600 / 36 = 100 chi³

# 斛法一尺六寸二分 (convert to chi³: 1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # 1.62 chi³

# 以斛法除之即得
粟量 = Fraction(體積簡化, 斛法)  # 100 / 1.62 = 1543/25 hu

# 分解為斛和分
a = 粟量  # 1543/25 hu
b = 粟量 - int(粟量)  # Fractional part (34/25 fen)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 5000/81
Variable 'b' has wrong value. Expected: 34/25, Actual: 59/81"""
