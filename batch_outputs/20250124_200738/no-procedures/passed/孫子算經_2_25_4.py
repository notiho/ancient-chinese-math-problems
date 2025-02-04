"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, the amount she weaves doubles compared to the previous day. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

Answer: on the first day, she weaves *a* cun; on the second day, she weaves *b* cun; on the third day, she weaves *c* cun; on the fourth day, she weaves *d* chi; on the fifth day, she weaves *e* chi.
"""

# Total woven in five days
total_woven = 5 * 10  # Convert 5 chi to cun (1 chi = 10 cun)

# Let the first day's weaving be x cun
a = Fraction(1, 31) * total_woven  # First day (x)
b = 2 * a  # Second day (2x)
c = 4 * a  # Third day (4x)
d = Fraction(8 * a, 10)  # Fourth day (8x, converted to chi)
e = Fraction(16 * a, 10)  # Fifth day (16x, converted to chi)

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
