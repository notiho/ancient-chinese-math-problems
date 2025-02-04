"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a貫文 ，一尺 b文 ，一寸 c文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash. 
Question: how much is 1 zhang, 1 chi, and 1 cun worth respectively?

The procedure says: Place the 8 guan of cash, divide it by 40 chi to get the price per chi.
Advancing the unit gives the price per zhang.
Retreating the unit gives the price per cun.

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen, and 1 cun is worth *c* wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
總價 = 8  # 貫
每貫文 = 1000  # 1 貫 = 1000 文
總價文 = 總價 * 每貫文  # 總價轉換為文

# 一疋長四十尺
疋長 = 40  # 尺

# 每尺價
每尺價 = Fraction(總價文, 疋長)

# 每丈價 (1 丈 = 10 尺)
每丈價 = 每尺價 * 10

# 每寸價 (1 尺 = 10 寸)
每寸價 = Fraction(每尺價, 10)

# 答案
a = Fraction(每丈價, 每貫文)  # 轉換回貫
b = 每尺價  # 文
c = 每寸價  # 文

a, b, c#----- content ends here -----

"""
"""
