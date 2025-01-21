"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, her output doubles compared to the previous day.
In five days, she weaves a total of 5 chi. 

Question: how much does she weave each day?

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. 
On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in five days
total_woven = 5  # in chi

# Conversion: 1 chi = 10 cun
total_woven_cun = total_woven * 10  # in cun

# Let the first day's weaving be x cun
# Each subsequent day doubles the previous day's output:
# First day: x cun
# Second day: 2x cun
# Third day: 4x cun
# Fourth day: 8x cun
# Fifth day: 16x cun
# Total: x + 2x + 4x + 8x + 16x = 31x = total_woven_cun

# Solve for x
x = Fraction(total_woven_cun, 31)  # First day's weaving in cun

# Calculate each day's weaving
a = x  # First day in cun
b = 2 * x  # Second day in cun
c = 4 * x  # Third day in cun
d = Fraction(8 * x, 10)  # Fourth day in chi (convert from cun to chi)
e = Fraction(16 * x, 10)  # Fifth day in chi (convert from cun to chi)

# Results
a, b, c, d, e  # Outputs for each day
"""
"""
