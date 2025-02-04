"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash. 
Question: how much is 1 zhang, 1 chi, and 1 cun worth respectively?

The procedure says: Place the value of 8 guan, and divide it by 40 chi to get the value per chi. 
Advancing the unit gives the value per zhang, and retreating the unit gives the value per cun.

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen, and 1 cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
總價值 = 8  # 貫
總長度 = 40  # 尺 (1 疋 = 40 尺)

# 每尺價值
每尺價值 = Fraction(總價值, 總長度)  # 每尺價值 in 貫

# 進位即丈價 (1 丈 = 10 尺)
每丈價值 = 每尺價值 * 10  # 每丈價值 in 貫

# 退位即寸價 (1 尺 = 10 寸)
每寸價值 = 每尺價值 / 10  # 每寸價值 in 貫

# Convert to appropriate units
a = 每丈價值  # 一丈價值 in 貫
b = 每尺價值 * 1000  # 一尺價值 in 文 (1 貫 = 1000 文)
c = 每寸價值 * 1000  # 一寸價值 in 文 (1 貫 = 1000 文)

a, b, c#----- content ends here -----

"""
"""
