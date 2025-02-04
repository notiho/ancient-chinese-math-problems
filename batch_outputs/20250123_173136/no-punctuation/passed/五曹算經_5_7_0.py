"""
今有錦一疋直錢八貫問一丈一尺一寸各直㡬何
術曰列錢八貫以四十尺除之即尺價進位即丈價退位即寸價
答曰:一丈 a貫文 一尺 b文 一寸 c文 
"""

"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Arrange the cash value of 8 guan, and divide it by 40 chi, obtaining the value per chi.
Advancing the unit gives the value per zhang.
Retreating the unit gives the value per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# 錢八貫
錢 = 8  # in guan

# 一疋為四十尺
疋長度 = 40  # in chi

# 以四十尺除之，即尺價
尺價 = Fraction(錢, 疋長度)  # value per chi in guan

# 進位，即丈價 (1丈 = 10尺)
丈價 = 10 * 尺價  # value per zhang in guan

# 退位，即寸價 (1尺 = 10寸)
寸價 = Fraction(尺價, 10)  # value per cun in guan

# Convert to appropriate units
a = 丈價  # value per zhang in guan
b = 尺價 * 1000  # value per chi in wen (1 guan = 1000 wen)
c = 寸價 * 1000  # value per cun in wen (1 guan = 1000 wen)
"""
"""
