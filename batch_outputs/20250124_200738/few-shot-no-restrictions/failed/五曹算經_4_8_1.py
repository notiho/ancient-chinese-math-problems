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
Multiply it by the height of 4 chi to get 3600 chi³.
Divide it by 36 to account for the shape of the pile, obtaining 100 chi³.
Finally, divide it by the volume of 1 hu, which is 1 chi³ 6 cun 2 fen (1 chi³ = 10 cun³, so 1 chi³ 6 cun 2 fen = 1.62 chi³).
This gives the amount of millet in hu.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1 zhang = 10 chi

# 高四尺
高 = 4  # chi

# 斛法 1 chi³ 6 cun 2 fen = 1.62 chi³
斛法 = Fraction(162, 100)  # Representing 1.62 as a fraction

# Step 1: Square the base circumference
下周平方 = 下周 ** 2  # chi²

# Step 2: Multiply by the height
體積 = 下周平方 * 高  # chi³

# Step 3: Divide by 36 for the shape of the pile
有效體積 = Fraction(體積, 36)  # chi³

# Step 4: Divide by the volume of 1 hu
粟 = 有效體積 / 斛法  # hu

# Extract the integer part (a hu) and fractional remainder (b fen)
a = 粟.numerator // 粟.denominator  # Integer part (hu)
b = (粟 - a) * 100  # Remaining fraction in fen (1 hu = 100 fen)

# Final answer
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 5900/81"""
