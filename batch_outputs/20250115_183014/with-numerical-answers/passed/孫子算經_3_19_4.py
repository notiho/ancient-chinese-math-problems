"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a(=4500)錢 ，尺 b(=450)錢 ，寸 c(=45)錢 。
"""

"""
Suppose there is one bolt of brocade worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

The procedure says: Place the 18,000 qian and divide it by 4, obtaining the value of one zhang.
Step back once and again, obtaining the values of chi and cun.

Answer: one zhang is *a*(=4500) qian, one chi is *b*(=450) qian, and one cun is *c*(=45) qian.
"""

# 置錢一萬八千
錢 = 18000

# 以四除之，得一丈之直
丈 = 錢 / 4

# 一退再退，得尺寸之直
尺 = 丈 / 10
寸 = 尺 / 10

a = 丈  # 4500
b = 尺  # 450
c = 寸  # 45
"""
"""
