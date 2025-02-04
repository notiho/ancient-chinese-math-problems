"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of coins. 
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Place the value of 8 guan, and divide it by 40 chi to get the value per chi.
Advancing the unit gives the value per zhang.
Retreating the unit gives the value per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
錦價 = 8  # 貫
總尺數 = 40  # 一疋有四十尺

# 每尺價
每尺價 = Fraction(錦價 * 1000, 總尺數)  # 1 貫 = 1000 文

# 一丈價 (進位，1 丈 = 10 尺)
一丈價 = 每尺價 * 10 / 1000  # 換算回貫

# 一寸價 (退位，1 尺 = 10 寸)
一寸價 = 每尺價 / 10  # 文

# 答案
a = 一丈價  # 一丈價 (貫)
b = 每尺價  # 一尺價 (文)
c = 一寸價  # 一寸價 (文)

a, b, c#----- content ends here -----

"""
"""
