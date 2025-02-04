"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Arrange the cash value of 8 guan.
Divide it by 40 chi to obtain the value per chi.
Advancing a position gives the value per zhang.
Retreating a position gives the value per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
總價 = 8  # 貫
每貫文 = 1000  # 一貫等於1000文
總價文 = 總價 * 每貫文  # 總價轉換為文

# 一疋長四十尺
總長度 = 40  # 尺

# 以四十尺除之即尺價
尺價 = Fraction(總價文, 總長度)

# 進位即丈價 (1丈 = 10尺)
丈價 = 10 * 尺價

# 退位即寸價 (1尺 = 10寸)
寸價 = Fraction(尺價, 10)

# 答案
a = Fraction(丈價, 每貫文)  # 丈價轉換為貫
b = 尺價  # 尺價以文表示
c = 寸價  # 寸價以文表示#----- content ends here -----

"""
"""
