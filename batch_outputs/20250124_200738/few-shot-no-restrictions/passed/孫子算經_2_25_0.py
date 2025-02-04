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

The procedure says: Arrange the daily weaving amounts in a decreasing sequence (1, 2, 4, 8, 16). 
Add them together, obtaining 31 as the divisor. 
Multiply the total (5 chi) by each of the sequence values, obtaining the dividend for each day. 
Divide each dividend by the divisor to get the daily weaving amounts.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. 
On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. 
On the fifth day, she weaves *e* chi.
"""

from fractions import Fraction

# Total weaving in 5 days
total_weaving = 5  # in chi

# Daily weaving ratios (1, 2, 4, 8, 16)
ratios = [1, 2, 4, 8, 16]

# Sum of the ratios (divisor)
法 = sum(ratios)

# Convert total weaving to cun (1 chi = 10 cun)
total_weaving_cun = total_weaving * 10

# Calculate daily weaving amounts
daily_weaving_cun = [Fraction(ratio * total_weaving_cun, 法) for ratio in ratios]

# Convert results to chi and cun
a = daily_weaving_cun[0]  # First day in cun
b = daily_weaving_cun[1]  # Second day in cun
c = daily_weaving_cun[2]  # Third day in cun
d = daily_weaving_cun[3] / 10  # Fourth day in chi
e = daily_weaving_cun[4] / 10  # Fifth day in chi

# Results
a寸 = a
b寸 = b
c寸 = c
d尺 = d
e尺 = e#----- content ends here -----

"""
"""
