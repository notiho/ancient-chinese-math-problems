"""
今有錦一匹直錢一萬八千問丈尺寸各直幾何
術曰置錢一萬八千以四除之得一丈之直一退再退得尺寸之直
答曰丈 a錢 尺 b錢 寸 c錢 
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the 18,000 qian and divide it by 4, obtaining the value of one zhang.
Step back once, and step back again to obtain the value of one chi and one cun, respectively.

Answer: one zhang is worth *a* qian, one chi is worth *b* qian, and one cun is worth *c* qian.
"""

# 錢一萬八千
錢 = 18000

# 以四除之，得一丈之直
丈直 = 錢 / 4

# 退一步，得一尺之直
尺直 = 丈直 / 10

# 再退一步，得一寸之直
寸直 = 尺直 / 10

a = 丈直
b = 尺直
c = 寸直#----- content ends here -----

"""
"""
