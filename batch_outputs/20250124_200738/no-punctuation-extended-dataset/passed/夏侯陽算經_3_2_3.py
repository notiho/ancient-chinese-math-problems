"""
今有錦一匹直錢十八貫問丈尺寸各得幾何
術曰置錢數以四丈除之得丈價一退為尺價再退為寸價
答曰一丈 a貫 一尺 b文 一寸 c文
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 18 guan of money.
Question: how much is the value per zhang, chi, and cun?

The procedure says: Place the total money amount.
Divide it by 4 zhang to obtain the value per zhang.
Move back one place to obtain the value per chi.
Move back another place to obtain the value per cun.

Answer: 1 zhang is worth *a* guan, 1 chi is worth *b* wen, and 1 cun is worth *c* wen.
"""

# 錢數
錢數 = 18  # 貫

# 以四丈除之，得丈價一
丈價 = Fraction(錢數, 4)  # 貫 per 丈

# 退為尺價
尺價 = 丈價 / 10  # 貫 per 尺

# 再退為寸價
寸價 = 尺價 / 10  # 貫 per 寸

# Convert 尺價 and 寸價 to smaller units (文)
b = 尺價 * 1000  # 1 貫 = 1000 文
c = 寸價 * 1000  # 1 貫 = 1000 文

a = 丈價  # 丈價 remains in 貫
b = Fraction(b)  # 文 per 尺
c = Fraction(c)  # 文 per 寸#----- content ends here -----

"""
"""
