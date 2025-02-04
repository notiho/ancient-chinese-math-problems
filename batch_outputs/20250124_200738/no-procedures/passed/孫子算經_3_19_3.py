"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

#----- content starts here -----
"""
Suppose there is a piece of brocade (silk fabric) that is 1 pi in length and worth 18,000 qian.
Question: how much is each zhang, chi, and cun worth?

Answer: each zhang is worth *a* qian, each chi is worth *b* qian, and each cun is worth *c* qian.
"""

# Total value of the brocade
total_value = 18000

# Length of 1 pi in terms of chi (1 pi = 4 zhang = 40 chi = 400 cun)
total_chi = 40
total_cun = 400

# Value per zhang (1 zhang = 10 chi)
a = Fraction(total_value, 4)

# Value per chi
b = Fraction(total_value, total_chi)

# Value per cun
c = Fraction(total_value, total_cun)

a, b, c#----- content ends here -----

"""
"""
