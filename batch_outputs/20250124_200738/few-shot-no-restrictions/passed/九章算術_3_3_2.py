"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the sequence 1, 2, 4, 8, 16 as a decreasing sequence.
Add them together to form the divisor.
Multiply the total 5 chi by each of the sequence terms (before summing), forming the dividends.
Divide each dividend by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

from fractions import Fraction

# Total woven in five days
total_woven = 5  # chi

# Sequence of daily weaving multipliers
sequence = [1, 2, 4, 8, 16]

# Add the sequence to form the divisor
divisor = sum(sequence)

# Multiply total woven by each sequence term to form the dividends
dividends = [total_woven * term for term in sequence]

# Divide each dividend by the divisor to get the daily weaving amounts
daily_woven = [Fraction(dividend, divisor) for dividend in dividends]

# Convert the results into chi and cun
a = daily_woven[0] * 10  # First day in cun
b = daily_woven[1] * 10  # Second day in cun
c = daily_woven[2] * 10  # Third day in cun
d = daily_woven[3]       # Fourth day in chi
e = daily_woven[4]       # Fifth day in chi

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
