"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan in money. 
Question: how much is the value of 1 zhang, 1 chi, and 1 cun respectively?

The procedure says: Place the value of 8 guan, divide it by 40 chi (the length of the bolt), obtaining the value per chi.
Advancing the unit gives the value per zhang.
Retreating the unit gives the value per cun.

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen, and 1 cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
錦價 = 8  # 貫
一疋長度 = 40  # 尺

# 以四十尺除之即尺價
尺價 = Fraction(錦價, 一疋長度)  # 每尺的價值 (貫)

# 進位即丈價 (1丈 = 10尺)
丈價 = 10 * 尺價  # 每丈的價值 (貫)

# 退位即寸價 (1尺 = 10寸)
寸價 = Fraction(尺價, 10)  # 每寸的價值 (文)

# 答案
a = 丈價  # 一丈的價值 (貫)
b = 尺價 * 1000  # 一尺的價值 (文, 1貫 = 1000文)
c = 寸價 * 1000  # 一寸的價值 (文, 1貫 = 1000文)

a, b, c#----- content ends here -----

"""
"""
