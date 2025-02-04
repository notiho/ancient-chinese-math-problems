"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles, and in five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the sequence 1, 2, 4, 8, 16 as a decreasing sequence.
Add them together to obtain the divisor.
Multiply the total 5 chi by each of the sequence elements (before summing), obtaining the dividend for each day.
Divide each dividend by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

from fractions import Fraction

# Total woven in 5 days
total_woven = 5  # in chi

# Sequence of daily weaving multipliers
sequence = [1, 2, 4, 8, 16]

# Add the sequence to get the divisor
divisor = sum(sequence)

# Multiply total woven by each sequence element to get the dividend
dividends = [total_woven * x for x in sequence]

# Divide each dividend by the divisor to get the daily weaving amounts
daily_weaving = [Fraction(dividend, divisor) for dividend in dividends]

# Convert to appropriate units (1 chi = 10 cun)
a = daily_weaving[0] * 10  # First day in cun
b = daily_weaving[1] * 10  # Second day in cun
c = daily_weaving[2] * 10  # Third day in cun
d = daily_weaving[3]       # Fourth day in chi
e = daily_weaving[4]       # Fifth day in chi

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
