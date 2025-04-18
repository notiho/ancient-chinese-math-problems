"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, her output doubles, and in five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the outputs in a decreasing sequence, and in auxiliary, add them, obtaining 31 as the divisor.
Multiply the total 5 chi by the unadded sequence, and each becomes the dividend.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 五日織通五尺
總織 = 5  # in chi

# 日自倍 (outputs double each day)
日織 = [1, 2, 4, 8, 16]  # relative proportions of daily outputs

# 各置列衰副，并得三十一為法
法 = sum(日織)

# 以五尺乘并者，各自為實
實 = [總織 * i for i in 日織]

# 實如法而一，即得
a = Fraction(實[0], 法) * 10  # Convert chi to cun for the first three days
b = Fraction(實[1], 法) * 10
c = Fraction(實[2], 法) * 10
d = Fraction(實[3], 法)  # Fourth day remains in chi
e = Fraction(實[4], 法)  # Fifth day remains in chi
"""
"""
