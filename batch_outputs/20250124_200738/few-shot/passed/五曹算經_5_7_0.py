"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash. 
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Arrange the cash as 8 guan. Divide it by 40 chi to get the price per chi.
Advancing the unit gives the price per zhang.
Retreating the unit gives the price per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

from fractions import Fraction

# 錢八貫
錢 = 8  # in 貫

# 一疋為四十尺
疋長度 = 40  # in 尺

# 以四十尺除之即尺價
尺價 = Fraction(錢, 疋長度)  # in 貫 per 尺

# 進位即丈價 (1 丈 = 10 尺)
丈價 = 10 * 尺價  # in 貫 per 丈

# 退位即寸價 (1 尺 = 10 寸)
寸價 = Fraction(尺價, 10)  # in 貫 per 寸

# Convert to appropriate units
a = 丈價  # in 貫
b = 尺價 * 1000  # convert 貫 to 文 (1 貫 = 1000 文)
c = 寸價 * 1000  # convert 貫 to 文 (1 貫 = 1000 文)#----- content ends here -----

"""
"""
