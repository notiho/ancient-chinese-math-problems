"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles, and in five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the sequence of daily outputs in decreasing order, and sum them to obtain 31 as the divisor.
Multiply the total 5 chi by each of the sequence elements, obtaining the dividends.
Divide each dividend by the divisor to obtain the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in five days
總織 = 5  # chi

# Daily output sequence (倍增): 1, 2, 4, 8, 16
日織序列 = [1, 2, 4, 8, 16]

# Sum of the sequence as the divisor
法 = sum(日織序列)

# Multiply the total woven by each sequence element to get the dividends
實 = [總織 * i for i in 日織序列]

# Divide each dividend by the divisor to get the daily outputs
a = Fraction(實[0], 法) * 10  # Convert chi to cun for the first three days
b = Fraction(實[1], 法) * 10  # Convert chi to cun for the first three days
c = Fraction(實[2], 法) * 10  # Convert chi to cun for the first three days
d = Fraction(實[3], 法)       # chi for the fourth day
e = Fraction(實[4], 法)       # chi for the fifth day#----- content ends here -----

"""
"""
