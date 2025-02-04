"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Take the base circumference of 30 chi (3 zhang = 30 chi) and square it, obtaining 900 chi².
Multiply this by the height of 4 chi, obtaining 3600 chi³.
Divide this by 36, obtaining 100 chi³.
Finally, divide this by the volume of 1 hu (1 hu = 1 chi³ 6 cun 2 fen = 1.62 chi³), obtaining the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi: 1 zhang = 10 chi)
下周 = 3 * 10  # in chi

# 高四尺
高 = 4  # in chi

# 斛法 (1 hu = 1 chi³ 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # 1.62 chi³ as a fraction

# Step 1: 下周自相乘
底積 = 下周 * 下周  # in chi²

# Step 2: 以高乘之
體積 = 底積 * 高  # in chi³

# Step 3: 以 36 除之
體積除以三十六 = Fraction(體積, 36)  # in chi³

# Step 4: 以斛法除之
粟斛數 = 體積除以三十六 / 斛法  # in hu

# Separate into integer hu and fractional fen
a = int(粟斛數)  # integer part (hu)
b = (粟斛數 - a) * 100  # fractional part (fen)

# Convert fractional fen to an integer
b = round(b)

a, b  # Output: a hu and b fen#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 73"""
