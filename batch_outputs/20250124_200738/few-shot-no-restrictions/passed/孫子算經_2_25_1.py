"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles compared to the previous day. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the sequence of daily outputs in decreasing order and add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by each of the terms in the sequence, obtaining the dividends.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

from fractions import Fraction

# Total weaving in 5 days
total_weaving = 5  # in chi

# Daily weaving sequence (doubles each day)
daily_sequence = [1, 2, 4, 8, 16]  # relative proportions

# Add the sequence to get the divisor
法 = sum(daily_sequence)  # 1 + 2 + 4 + 8 + 16 = 31

# Multiply total weaving by each term in the sequence to get the dividends
實 = [Fraction(total_weaving * term, 法) for term in daily_sequence]

# Convert results to appropriate units (1 chi = 10 cun)
a = 實[0] * 10  # First day in cun
b = 實[1] * 10  # Second day in cun
c = 實[2] * 10  # Third day in cun
d = 實[3]       # Fourth day in chi
e = 實[4]       # Fifth day in chi

# Results
a寸 = a
b寸 = b
c寸 = c
d尺 = d
e尺 = e#----- content ends here -----

"""
"""
