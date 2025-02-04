"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day she weaves double the amount of the previous day. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in 5 days
total_woven = 5  # in chi

# Convert total to cun (1 chi = 10 cun)
total_woven_cun = total_woven * 10  # in cun

# Let the first day's weaving be x cun
a = Fraction(1)  # First day weaving in cun

# Each subsequent day doubles the previous day's weaving
b = 2 * a  # Second day weaving in cun
c = 2 * b  # Third day weaving in cun
d = 2 * c / 10  # Fourth day weaving in chi
e = 2 * d  # Fifth day weaving in chi

# Total weaving equation: a + b + c + d*10 + e*10 = total_woven_cun
# Solve for a
a = Fraction(total_woven_cun, 1 + 2 + 4 + 8 + 16)  # First day weaving in cun

# Calculate the rest
b = 2 * a  # Second day weaving in cun
c = 2 * b  # Third day weaving in cun
d = 2 * c / 10  # Fourth day weaving in chi
e = 2 * d  # Fifth day weaving in chi

a, b, c, d, e  # Results for each day
"""
"""
