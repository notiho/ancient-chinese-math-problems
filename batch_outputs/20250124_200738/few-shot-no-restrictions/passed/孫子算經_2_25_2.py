"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles compared to the previous day.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the sequence of daily outputs in a line, each doubling the previous one.
Add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by each term in the sequence, giving the dividend for each day.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

from fractions import Fraction

# Total woven in 5 days
total_woven = 5  # in chi

# Sequence of daily outputs (doubling each day)
daily_outputs = [1, 2, 4, 8, 16]  # relative proportions

# Add the sequence to get the divisor
法 = sum(daily_outputs)  # 法 = 31

# Multiply total woven by each term in the sequence to get the dividend
實 = [total_woven * i for i in daily_outputs]

# Divide each dividend by the divisor to get the daily outputs
daily_woven = [Fraction(i, 法) for i in 實]

# Convert results to chi and cun
a = daily_woven[0] * 10  # First day in cun
b = daily_woven[1] * 10  # Second day in cun
c = daily_woven[2] * 10  # Third day in cun
d = daily_woven[3]       # Fourth day in chi
e = daily_woven[4]       # Fifth day in chi

# Results
a寸 = a
b寸 = b
c寸 = c
d尺 = d
e尺 = e#----- content ends here -----

"""
"""
