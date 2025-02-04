"""
今有錦一疋直錢八貫。問：一丈一尺一寸各直㡬何？
術曰：列錢八貫，以四十尺除之即尺價；進位即丈價；退位即寸價。
答曰:一丈 a(=2)貫文 ，一尺 b(=200)文 ，一寸 c(=20)文 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 8 guan of cash.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the 8 guan of cash, and divide it by 40 chi to obtain the price per chi.
Advancing the unit gives the price per zhang.
Retreating the unit gives the price per cun.

Answer: 1 zhang is *a*(=2) guan, 1 chi is *b*(=200) wen, and 1 cun is *c*(=20) wen.
"""

# 錦一疋直錢八貫
錢 = 8  # 貫

# 一疋為四十尺
疋長 = 40  # 尺

# 以四十尺除之即尺價
尺價 = Fraction(錢, 疋長)  # 貫/尺

# 進位即丈價 (1丈 = 10尺)
丈價 = 10 * 尺價  # 貫/丈

# 退位即寸價 (1尺 = 10寸)
寸價 = 尺價 / 10  # 貫/寸

# Convert 貫 to 文 (1貫 = 1000文)
a = 丈價  # 2 貫
b = 尺價 * 1000  # 200 文
c = 寸價 * 1000  # 20 文#----- content ends here -----

"""
"""
