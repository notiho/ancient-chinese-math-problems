"""
今有錦一匹直錢一萬八千問丈尺寸各直幾何
術曰置錢一萬八千以四除之得一丈之直一退再退得尺寸之直
答曰丈 a錢 尺 b錢 寸 c錢 
"""

"""
Suppose there is a piece of brocade, 1 pi, worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the 18,000 qian and divide it by 4, obtaining the value of 1 zhang.
Step back once, obtaining the value of 1 chi.
Step back again, obtaining the value of 1 cun.

Answer: 1 zhang is worth *a* qian, 1 chi is worth *b* qian, and 1 cun is worth *c* qian.
"""

# 錢一萬八千
總錢 = 18000

# 以四除之，得一丈之直
丈直 = 總錢 / 4

# 退，得尺寸之直
尺直 = 丈直 / 10  # 1 丈 = 10 尺
寸直 = 尺直 / 10  # 1 尺 = 10 寸

a = 丈直
b = 尺直
c = 寸直
"""
"""
