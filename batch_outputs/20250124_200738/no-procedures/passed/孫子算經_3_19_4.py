"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of brocade (1 pi), worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

Answer: each zhang is worth *a* qian, each chi is worth *b* qian, and each cun is worth *c* qian.
"""

# Total value of the brocade
total_value = 18000

# Length of one bolt of brocade in chi (1 pi = 4 zhang = 40 chi)
total_length_in_chi = 40

# Value per chi
b = Fraction(total_value, total_length_in_chi)

# Value per zhang (1 zhang = 10 chi)
a = 10 * b

# Value per cun (1 chi = 10 cun)
c = Fraction(b, 10)

# Output results
a, b, c#----- content ends here -----

"""
"""
