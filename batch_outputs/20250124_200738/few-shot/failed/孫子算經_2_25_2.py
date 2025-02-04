"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the outputs of each day in a decreasing sequence, and add them together to get 31 as the divisor.
Multiply the total 5 chi by the individual terms of the sequence to get the dividends.
Divide each dividend by the divisor to get the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 五日織通五尺
總織 = 5  # chi

# 各置列衰副
列 = [1, 2, 4, 8, 16]  # Daily weaving sequence (doubles each day)

# 并得三十一為法
法 = sum(列)

# 以五尺乘并者，各自為實
實 = [總織 * i for i in列]

# 實如法而一，即得
a = Fraction(實[0], 法) * 10  # Convert chi to cun for the first three days
b = Fraction(實[1], 法) * 10
c = Fraction(實[2], 法) * 10
d = Fraction(實[3], 法)  # Fourth day remains in chi
e = Fraction(實[4], 法)  # Fifth day remains in chi#----- content ends here -----

"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 23)"""
