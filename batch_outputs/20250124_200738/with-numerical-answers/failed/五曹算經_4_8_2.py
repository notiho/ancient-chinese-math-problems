"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a(=1543/25)斛 奇 b(=34/25)分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground with a base circumference of 3 zhang and a height of 4 chi.
Question: how much millet is there?

The procedure says: Place the base circumference of 30 chi, square it, obtaining 900 chi².
Multiply it by the height of 4 chi, obtaining 3600 chi³.
Divide it by 36, obtaining 100 chi³.
Divide it by the dou-measure of 1 chi 6 cun 2 fen (1.62 chi), obtaining the result.

The answer says: *a*(=1543/25) dou and *b*(=34/25) fen.
"""

from fractions import Fraction

# 下周三丈 (convert to chi)
下周 = 3 * 10  # 1 丈 = 10 尺

# 高四尺
高 = 4

# 列下周三十尺自相乘得九百尺
積 = 下周 * 下周  # Square the base circumference

# 以高四尺乘之得三千六百尺
體積 = 積 * 高  # Multiply by the height

# 以三十六除之得一百尺
體積 = Fraction(體積, 36)

# 以斛法一尺六寸二分除之即得 (convert 1 chi 6 cun 2 fen to chi)
斛法 = Fraction(1) + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen = 1.62 chi

# Divide the volume by the dou-measure
粟 = Fraction(體積, 斛法)

# Separate into dou and fen
a = 粟  # 1543/25 dou
b = 粟 - int(粟)  # Fractional part (34/25 fen)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 5000/81
Variable 'b' has wrong value. Expected: 34/25, Actual: 59/81"""
