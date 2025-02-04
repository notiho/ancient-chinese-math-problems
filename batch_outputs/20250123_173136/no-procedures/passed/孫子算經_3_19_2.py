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

# One pi of brocade is 4 zhang (1 pi = 4 zhang)
pi_to_zhang = 4

# One zhang is 10 chi
zhang_to_chi = 10

# One chi is 10 cun
chi_to_cun = 10

# Calculate the value of one zhang
a = Fraction(total_value, pi_to_zhang)

# Calculate the value of one chi
b = Fraction(a, zhang_to_chi)

# Calculate the value of one cun
c = Fraction(b, chi_to_cun)

# Results
a, b, c
"""
"""
