"""
今有錦一匹直錢十八貫問丈尺寸各得幾何
術曰置錢數以四丈除之得丈價一退為尺價再退為寸價
答曰一丈 a貫 一尺 b文 一寸 c文
"""

"""
Suppose there is a piece of brocade, one pi, worth 18 guan.
Question: how much is the value per zhang, chi, and cun?

The procedure says: Place the total amount of money.
Divide it by 4 zhang to obtain the value per zhang.
Move one decimal place back to get the value per chi.
Move another decimal place back to get the value per cun.

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

# Convert to appropriate units
a = 丈價  # 貫
b = 尺價 * 1000  # 文 (1 貫 = 1000 文)
c = 寸價 * 1000  # 文 (1 貫 = 1000 文)
"""
"""
