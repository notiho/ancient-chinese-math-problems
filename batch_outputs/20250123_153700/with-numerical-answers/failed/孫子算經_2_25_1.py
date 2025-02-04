"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a(=50/31)寸 ，次日織 b(=100/31)寸 ，次日織 c(=200/31)寸 ，次日織 d(=40/31)尺 ，次日織 e(=80/31)尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the sequence of daily outputs in a decreasing series. Add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by each of the terms in the sequence, obtaining the dividends.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a*(=50/31) cun. On the second day, she weaves *b*(=100/31) cun. On the third day, she weaves *c*(=200/31) cun. On the fourth day, she weaves *d*(=40/31) chi. On the fifth day, she weaves *e*(=80/31) chi.
"""

# 五日織通五尺
總織 = 5  # in chi

# 日自倍
日倍數列 = [1, 2, 4, 8, 16]

# 各置列衰副，并得三十一為法
法 = sum(日倍數列)

# 以五尺乘并者，各自為實
實 = [總織 * 倍數 for 倍數 in 日倍數列]

# 實如法而一，即得
a = Fraction(實[0], 法)  # 初日織 50/31 寸
b = Fraction(實[1], 法)  # 次日織 100/31 寸
c = Fraction(實[2], 法)  # 次日織 200/31 寸
d = Fraction(實[3], 法)  # 次日織 40/31 尺
e = Fraction(實[4], 法)  # 次日織 80/31 尺
"""
Variable 'a' has wrong value. Expected: 50/31, Actual: 5/31
Variable 'b' has wrong value. Expected: 100/31, Actual: 10/31
Variable 'c' has wrong value. Expected: 200/31, Actual: 20/31"""
