"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

#----- content starts here -----
"""
Suppose there is a piece of brocade (silk fabric) that is worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the value of 18,000 qian and divide it by 4 to obtain the value of one zhang.
Then, divide by 10 to obtain the value of one chi.
Finally, divide by 10 again to obtain the value of one cun.

Answer: one zhang is worth *a* qian, one chi is worth *b* qian, and one cun is worth *c* qian.
"""

# 錦一匹，直錢一萬八千
總價 = 18000

# 以四除之，得一丈之直
丈價 = Fraction(總價, 4)

# 一退 (divide by 10), 得一尺之直
尺價 = Fraction(丈價, 10)

# 再退 (divide by 10), 得一寸之直
寸價 = Fraction(尺價, 10)

# 答案
a = 丈價
b = 尺價
c = 寸價#----- content ends here -----

"""
"""
