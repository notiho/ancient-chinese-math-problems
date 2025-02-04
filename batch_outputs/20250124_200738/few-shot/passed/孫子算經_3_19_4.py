"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the 18,000 qian and divide it by 4, obtaining the value of one zhang.
Each step back (divide by 10) gives the value of one chi and one cun.

Answer: one zhang is worth *a* qian, one chi is worth *b* qian, and one cun is worth *c* qian.
"""

# 錢一萬八千
錢 = 18000

# 以四除之，得一丈之直
丈 = Fraction(錢, 4)

# 一退再退，得尺寸之直
尺 = Fraction(丈, 10)
寸 = Fraction(尺, 10)

a = 丈
b = 尺
c = 寸#----- content ends here -----

"""
"""
