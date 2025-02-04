"""
今有錦一疋直錢八貫問一丈一尺一寸各直㡬何
術曰列錢八貫以四十尺除之即尺價進位即丈價退位即寸價
答曰:一丈 a貫文 一尺 b文 一寸 c文 
"""

"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Arrange the cash value of 8 guan. Divide it by 40 chi to obtain the value per chi.
Advancing one place gives the value per zhang.
Retreating one place gives the value per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
錦價 = 8  # 貫

# 一疋為四十尺
疋長 = 40  # 尺

# 以四十尺除之，即尺價
尺價 = Fraction(錦價 * 1000, 疋長)  # 1 貫 = 1000 文

# 進位，即丈價 (1 丈 = 10 尺)
丈價 = 10 * 尺價 / 1000  # Convert back to 貫

# 退位，即寸價 (1 尺 = 10 寸)
寸價 = 尺價 / 10  # 文

a = 丈價
b = 尺價
c = 寸價
"""
"""
