"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, the amount she weaves doubles compared to the previous day. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in 5 days
total_woven = 5  # in chi

# Let the amount woven on the first day be x (in cun)
# Each day doubles, so:
# Day 1: x cun
# Day 2: 2x cun
# Day 3: 4x cun
# Day 4: 8x cun
# Day 5: 16x cun

# Total woven in cun:
# 1 chi = 10 cun
total_woven_in_cun = total_woven * 10

# Sum of woven amounts in cun:
# x + 2x + 4x + 8x + 16x = 31x
total_cun = 31

# Solve for x:
x = Fraction(total_woven_in_cun, total_cun)

# Calculate the amount woven each day:
a = x  # First day in cun
b = 2 * x  # Second day in cun
c = 4 * x  # Third day in cun
d = Fraction(8 * x, 10)  # Fourth day in chi
e = Fraction(16 * x, 10)  # Fifth day in chi

# Results:
a, b, c, d, e#----- content ends here -----

"""
"""
