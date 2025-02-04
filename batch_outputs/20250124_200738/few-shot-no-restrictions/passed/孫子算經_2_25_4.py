"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her weaving output doubles compared to the previous day. 
In five days, she weaves a total of 5 chi. 
Question: how much does she weave each day?

The procedure says: Place the sequence of outputs for each day in decreasing order. 
Add them together, obtaining 31 as the divisor. 
Multiply the total 5 chi by the individual outputs, obtaining the dividends. 
Divide each dividend by the divisor to obtain the daily weaving amounts.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. 
On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. 
On the fifth day, she weaves *e* chi.
"""

from fractions import Fraction

# Total weaving in 5 days
total_weaving = 5  # in chi

# Daily weaving outputs in terms of ratios (doubling each day)
daily_ratios = [1, 2, 4, 8, 16]  # First day: 1, Second day: 2, ..., Fifth day: 16

# Add the ratios to get the divisor
法 = sum(daily_ratios)  # 法 = 31

# Multiply total weaving by each ratio to get the dividends
實 = [total_weaving * ratio for ratio in daily_ratios]

# Divide each dividend by the divisor to get the daily weaving amounts
daily_weaving = [Fraction(實[i], 法) for i in range(len(實))]

# Convert results to chi and cun
a = daily_weaving[0] * 10  # First day in cun
b = daily_weaving[1] * 10  # Second day in cun
c = daily_weaving[2] * 10  # Third day in cun
d = daily_weaving[3]       # Fourth day in chi
e = daily_weaving[4]       # Fifth day in chi

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
