"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a(=50/31)寸 ，次日織 b(=100/31)寸 ，次日織 c(=200/31)寸 ，次日織 d(=40/31)尺 ，次日織 e(=80/31)尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the sequence of outputs (doubled each day) in a line.
Add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by each of the sequence elements, obtaining the dividends.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a*(=50/31) cun. On the second day, she weaves *b*(=100/31) cun. On the third day, she weaves *c*(=200/31) cun. On the fourth day, she weaves *d*(=40/31) chi. On the fifth day, she weaves *e*(=80/31) chi.
"""

# 日自倍
日織 = [1, 2, 4, 8, 16]  # Daily weaving sequence (doubled each day)

# 各置列衰副，并得三十一為法
法 = sum(日織)  # 31

# 以五尺乘并者
總織 = 5  # Total weaving in chi
實 = [總織 * i for i in 日織]

# 各自為實，實如法而一，即得
a, b, c, d, e = [Fraction(i, 法) for i in 實]

# Convert to appropriate units
a = a * 10  # First day in cun (50/31 cun)
b = b * 10  # Second day in cun (100/31 cun)
c = c * 10  # Third day in cun (200/31 cun)
d = d       # Fourth day in chi (40/31 chi)
e = e       # Fifth day in chi (80/31 chi)#----- content ends here -----

"""
"""
