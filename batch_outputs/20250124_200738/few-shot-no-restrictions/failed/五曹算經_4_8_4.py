"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground, with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says:
- Convert the base circumference to chi (30 chi).
- Multiply the base circumference by itself to get the area of the base (900 square chi).
- Multiply the base area by the height (4 chi) to get the volume (3600 cubic chi).
- Divide the volume by 36 to account for the shape of the pile (since it's a cone-like shape).
- Finally, divide the result by the volume of 1 hu (1 hu = 1 chi 6 cun 2 fen = 1.62 chi³).

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1 zhang = 10 chi

# 高四尺
高 = 4  # in chi

# Step 1: 下周自相乘得九百尺 (base area)
底面積 = 下周 * 下周  # in square chi

# Step 2: 以高四尺乘之得三千六百尺 (volume)
體積 = 底面積 * 高  # in cubic chi

# Step 3: 以三十六除之 (adjust for cone-like shape)
調整後體積 = Fraction(體積, 36)  # in cubic chi

# Step 4: 以斛法一尺六寸二分除之 (convert to hu)
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen = 1.62 chi³
粟量 = 調整後體積 / 斛法  # in hu

# Extract integer part (a) and fractional part (b)
a = int(粟量)  # integer part in hu
b = (粟量 - a) * 100  # fractional part in fen

# Final answer
a, round(b)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 61
Variable 'b' has wrong value. Expected: 34/25, Actual: 5900/81"""
