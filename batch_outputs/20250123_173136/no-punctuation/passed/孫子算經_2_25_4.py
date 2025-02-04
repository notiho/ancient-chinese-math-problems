"""
今有女子善織日自倍五日織通五尺問日織幾何
術曰各置列衰副并得三十一為法以五尺乘并者各自為實實如法而一即得
答曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

"""
Suppose there is a woman skilled in weaving. Each day, she doubles her output.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the outputs of each day in a sequence, each day doubling the previous one.
Add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by each of the individual outputs (before summing), obtaining the dividends.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 五日織通五尺
總織 = 5  # chi

# 各置列衰 (日自倍)
日織 = [1, 2, 4, 8, 16]

# 副并得三十一，為法
法 = sum(日織)

# 以五尺乘并者，各自為實
實 = [總織 * i for i in 日織]

# 實如法而一，即得
a = Fraction(實[0], 法) * 10  # Convert chi to cun
b = Fraction(實[1], 法) * 10  # Convert chi to cun
c = Fraction(實[2], 法) * 10  # Convert chi to cun
d = Fraction(實[3], 法)       # Remains in chi
e = Fraction(實[4], 法)       # Remains in chi
"""
"""
