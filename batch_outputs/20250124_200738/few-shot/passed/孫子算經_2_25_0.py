"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her weaving output doubles.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the daily outputs in a decreasing sequence and sum them, obtaining 31 as the divisor.
Multiply the total of 5 chi by each of the individual terms in the sequence, each becoming a dividend.
Divide each dividend by the divisor to obtain the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in five days
總織 = 5  # chi

# Daily weaving outputs in a geometric progression (1, 2, 4, 8, 16)
列衰 = [1, 2, 4, 8, 16]

# Sum of the sequence (法)
法 = sum(列衰)

# Multiply the total woven (5 chi) by each term in the sequence
實 = [總織 * i for i in 列衰]

# Divide each result by the divisor (法) to get daily outputs
a = Fraction(實[0], 法) * 10  # Convert to cun (1 chi = 10 cun)
b = Fraction(實[1], 法) * 10  # Convert to cun
c = Fraction(實[2], 法) * 10  # Convert to cun
d = Fraction(實[3], 法)       # Already in chi
e = Fraction(實[4], 法)       # Already in chi#----- content ends here -----

"""
"""
