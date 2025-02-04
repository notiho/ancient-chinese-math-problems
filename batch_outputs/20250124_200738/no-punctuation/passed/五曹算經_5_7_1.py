"""
今有錦一疋直錢八貫問一丈一尺一寸各直㡬何
術曰列錢八貫以四十尺除之即尺價進位即丈價退位即寸價
答曰:一丈 a貫文 一尺 b文 一寸 c文 
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is one zhang, one chi, and one cun worth respectively?

The procedure says: Arrange the cash value of 8 guan.
Divide it by 40 chi, obtaining the value per chi.
Advancing the unit gives the value per zhang.
Retreating the unit gives the value per cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

# 錦一疋直錢八貫
錢 = 8  # 貫

# 一疋為四十尺
疋長度 = 40  # 尺

# 以四十尺除之，即尺價
尺價 = Fraction(錢 * 1000, 疋長度)  # 1 貫 = 1000 文

# 進位，即丈價 (1 丈 = 10 尺)
丈價 = 10 * 尺價

# 退位，即寸價 (1 尺 = 10 寸)
寸價 = Fraction(尺價, 10)

# Convert results to appropriate units
a = Fraction(丈價, 1000)  # 丈價 in 貫
b = 尺價  # 尺價 in 文
c = 寸價  # 寸價 in 文#----- content ends here -----

"""
"""
