"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 as a decreasing sequence.
Add them together to obtain the divisor.
Multiply the total of 5 chi by each of the unadded numbers, making each its own dividend.
Divide the dividends by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 日自倍，五日織五尺
總織 = 5  # 尺

# 置一、二、四、八、十六為列衰
列衰 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列衰)

# 以五尺乘未并者，各自為實
實 = [總織 * i for i in列衰]

# 實如法得一尺
每日織 = [Fraction(i, 法) for i in 實]

# 初日織 a寸
a = 每日織[0] * 10  # 1 尺 = 10 寸

# 次日織 b寸
b = 每日織[1] * 10  # 1 尺 = 10 寸

# 次日織 c寸
c = 每日織[2] * 10  # 1 尺 = 10 寸

# 次日織 d尺
d = 每日織[3]

# 次日織 e尺
e = 每日織[4]#----- content ends here -----

"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 24)"""
