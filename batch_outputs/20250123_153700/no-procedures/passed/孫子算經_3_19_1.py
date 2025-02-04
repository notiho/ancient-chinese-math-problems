"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

"""
Suppose there is one bolt of brocade (1 pi), worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

Answer: each zhang is worth *a* qian, each chi is worth *b* qian, and each cun is worth *c* qian.
"""

# Total value of the brocade
total_value = 18000

# Length of one pi in chi (1 pi = 4 zhang = 40 chi = 400 cun)
total_length_in_chi = 40
total_length_in_cun = 400

# Value of one zhang (1 zhang = 10 chi)
a = Fraction(total_value, 4)

# Value of one chi
b = Fraction(total_value, total_length_in_chi)

# Value of one cun
c = Fraction(total_value, total_length_in_cun)
"""
"""
