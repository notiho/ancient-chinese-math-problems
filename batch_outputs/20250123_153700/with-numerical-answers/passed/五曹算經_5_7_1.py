"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a(=2)貫文 ，一尺 b(=200)文 ，一寸 c(=20)文 。
"""

"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the value of 8 guan, and divide it by 40 chi to obtain the value per chi.
Advancing one place gives the value per zhang.
Retreating one place gives the value per cun.

Answer: 1 zhang is *a*(=2) guan, 1 chi is *b*(=200) wen, and 1 cun is *c*(=20) wen.
"""

from fractions import Fraction

# 錦一疋直錢八貫
錢 = 8  # 8 貫

# 一疋為四十尺
疋長度 = 40  # 40 尺

# 以四十尺除之即尺價
尺價 = Fraction(錢, 疋長度)  # 每尺價值

# 進位即丈價 (1 丈 = 10 尺)
丈價 = 10 * 尺價  # 每丈價值

# 退位即寸價 (1 尺 = 10 寸)
寸價 = Fraction(尺價, 10)  # 每寸價值

a = 丈價  # 2 貫
b = 尺價 * 1000  # 200 文
c = 寸價 * 1000  # 20 文
"""
"""
