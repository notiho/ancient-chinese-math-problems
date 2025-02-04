"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Arrange the cash value as 8 guan.
Divide it by 40 chi to obtain the value per chi.
Advancing the unit gives the value per zhang.
Retreating the unit gives the value per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
錢 = 8  # 貫
疋長度 = 40  # 一疋為四十尺

# 以四十尺除之即尺價
尺價 = Fraction(錢, 疋長度)  # 每尺價值

# 進位即丈價 (1丈 = 10尺)
丈價 = 10 * 尺價

# 退位即寸價 (1尺 = 10寸)
寸價 = Fraction(尺價, 10)

# 答案
a = 丈價  # 一丈價值
b = 尺價  # 一尺價值
c = 寸價  # 一寸價值#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 200, Actual: 1/5
Variable 'c' has wrong value. Expected: 20, Actual: 1/50"""
