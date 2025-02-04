"""
今有錦一匹直錢十八貫問丈尺寸各得幾何
術曰置錢數以四丈除之得丈價一退為尺價再退為寸價
答曰一丈 a貫 一尺 b文 一寸 c文
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 18 guan of money.
Question: how much is the value of one zhang, one chi, and one cun respectively?

The procedure says: Place the total money amount.
Divide it by 4 zhang to obtain the value of one zhang.
Move one decimal place back to get the value of one chi.
Move another decimal place back to get the value of one cun.

Answer: one zhang is worth *a* guan, one chi is worth *b* wen, and one cun is worth *c* wen.
"""

# 錢數
錢數 = 18  # in 貫

# 以四丈除之，得丈價一
丈價 = 錢數 / 4  # in 貫

# 退為尺價
尺價 = 丈價 / 10  # in 貫 (1 丈 = 10 尺)

# 再退為寸價
寸價 = 尺價 / 10  # in 貫 (1 尺 = 10 寸)

# Convert to appropriate units
a = 丈價  # in 貫
b = 尺價 * 1000  # in 文 (1 貫 = 1000 文)
c = 寸價 * 1000  # in 文 (1 貫 = 1000 文)#----- content ends here -----

"""
"""
