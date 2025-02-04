"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

"""
Suppose there is one bolt of brocade (1 pi) worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

Answer: *a* qian per zhang, *b* qian per chi, and *c* qian per cun.
"""

# Total value of the brocade in qian
total_value = 18000

# 1 pi = 4 zhang = 40 chi = 400 cun
pi_to_zhang = 4
pi_to_chi = 40
pi_to_cun = 400

# Calculate the value of each unit
a = Fraction(total_value, pi_to_zhang)  # Value per zhang
b = Fraction(total_value, pi_to_chi)   # Value per chi
c = Fraction(total_value, pi_to_cun)   # Value per cun
"""
"""
