"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, the amount she weaves doubles compared to the previous day. In five days, she weaves a total of 5 chi (or 50 cun).  
Question: how much does she weave each day?

Answer: On the first day, she weaves *a* cun, on the second day *b* cun, on the third day *c* cun, on the fourth day *d* chi, and on the fifth day *e* chi.
"""

# Total woven in 5 days
total_cun = 50  # 5 chi = 50 cun

# Let the amount woven on the first day be x (in cun)
# Each subsequent day doubles the previous day's amount:
# Day 1: x
# Day 2: 2x
# Day 3: 4x
# Day 4: 8x
# Day 5: 16x
# Total: x + 2x + 4x + 8x + 16x = 31x = 50 cun

# Solve for x
x = Fraction(total_cun, 31)

# Calculate the amount woven each day
a = x  # First day (in cun)
b = 2 * x  # Second day (in cun)
c = 4 * x  # Third day (in cun)
d = Fraction(8 * x, 10)  # Fourth day (convert cun to chi: 10 cun = 1 chi)
e = Fraction(16 * x, 10)  # Fifth day (convert cun to chi: 10 cun = 1 chi)

# Results
a, b, c, d, e
"""
"""
