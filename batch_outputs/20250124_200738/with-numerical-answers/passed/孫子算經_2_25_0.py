"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a(=50/31)寸 ，次日織 b(=100/31)寸 ，次日織 c(=200/31)寸 ，次日織 d(=40/31)尺 ，次日織 e(=80/31)尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the sequence of outputs [as a geometric progression], and sum them to obtain 31 as the divisor.
Multiply the total 5 chi by each term in the sequence, obtaining the dividends.
Divide each dividend by the divisor to obtain the daily outputs.

Answer: On the first day, she weaves *a*(=50/31) cun. On the second day, she weaves *b*(=100/31) cun. On the third day, she weaves *c*(=200/31) cun. On the fourth day, she weaves *d*(=40/31) chi. On the fifth day, she weaves *e*(=80/31) chi.
"""

# 日自倍，五日織通五尺
總織 = 5  # 5 chi
日倍率 = [1, 2, 4, 8, 16]  # Daily weaving progression (geometric sequence)

# 各置列衰副，并得三十一為法
法 = sum(日倍率)  # 31

# 以五尺乘并者，各自為實
實 = [總織 * 倍 for 倍 in 日倍率]

# 實如法而一，即得
a = Fraction(實[0], 法) * 10  # Convert chi to cun for the first three days
b = Fraction(實[1], 法) * 10  # Convert chi to cun for the first three days
c = Fraction(實[2], 法) * 10  # Convert chi to cun for the first three days
d = Fraction(實[3], 法)  # Remain in chi for the last two days
e = Fraction(實[4], 法)  # Remain in chi for the last two days

# Results:
# a = 50/31 cun
# b = 100/31 cun
# c = 200/31 cun
# d = 40/31 chi
# e = 80/31 chi#----- content ends here -----

"""
"""
