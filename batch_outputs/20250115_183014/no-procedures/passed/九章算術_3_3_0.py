"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, the amount she weaves doubles compared to the previous day.
In 5 days, she weaves a total of 5 chi (尺).
Question: how much does she weave each day?

Answer: on the first day, she weaves *a* cun (寸); on the second day, she weaves *b* cun; on the third day, she weaves *c* cun; on the fourth day, she weaves *d* chi (尺); on the fifth day, she weaves *e* chi (尺).
"""

# Total weaving in 5 days
total_weaving = 5  # in chi

# Conversion: 1 chi = 10 cun
total_weaving_in_cun = total_weaving * 10  # convert to cun

# Let the first day's weaving be x (in cun)
# Each subsequent day doubles the previous day's weaving:
# Day 1: x
# Day 2: 2x
# Day 3: 4x
# Day 4: 8x
# Day 5: 16x
# Total weaving: x + 2x + 4x + 8x + 16x = 31x = total_weaving_in_cun

x = Fraction(total_weaving_in_cun, 31)  # First day's weaving in cun

# Calculate weaving for each day
a = x  # First day in cun
b = 2 * x  # Second day in cun
c = 4 * x  # Third day in cun
d = Fraction(8 * x, 10)  # Fourth day in chi
e = Fraction(16 * x, 10)  # Fifth day in chi

# Results
a, b, c, d, e
"""
"""
