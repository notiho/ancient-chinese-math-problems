"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, her output doubles.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange 1, 2, 4, 8, and 16 as a decreasing sequence.
Add them together to obtain the divisor.
Multiply the total 5 chi by each of the individual terms (before summing), obtaining the dividends.
Divide each dividend by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in five days
總織 = 5  # chi

# Arrange 1, 2, 4, 8, 16 as a sequence
列衰 = [1, 2, 4, 8, 16]

# Add them together to obtain the divisor
法 = sum(列衰)

# Multiply the total 5 chi by each term in the sequence
實 = [總織 * i for i in 列衰]

# Divide each dividend by the divisor
a = Fraction(實[0], 法) * 10  # Convert chi to cun
b = Fraction(實[1], 法) * 10  # Convert chi to cun
c = Fraction(實[2], 法) * 10  # Convert chi to cun
d = Fraction(實[3], 法)       # chi remains as is
e = Fraction(實[4], 法)       # chi remains as is
"""
"""
