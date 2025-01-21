"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a(=50/31)寸 。次日織 b(=100/31)寸 。次日織 c(=200/31)寸 。次日織 d(=40/31)尺 。次日織 e(=80/31)尺 。
"""

"""
Suppose there is a woman skilled in weaving. Each day, her output doubles. In five days, she weaves 5 chi.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a decreasing sequence.
Add them together to form the divisor.
Multiply the 5 chi by the numbers not yet added, each becoming its own dividend.
Divide each dividend by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a*(=50/31) cun. On the second day, she weaves *b*(=100/31) cun. On the third day, she weaves *c*(=200/31) cun. On the fourth day, she weaves *d*(=40/31) chi. On the fifth day, she weaves *e*(=80/31) chi.
"""

# 置一、二、四、八、十六為列衰
列衰 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列衰)

# 以五尺乘未并者，各自為實
總織 = 5  # 五尺
實 = [總織 * i for i in列衰]

# 實如法得一尺
a, b, c, d, e = [Fraction(i, 法) for i in 實]  # 50/31, 100/31, 200/31, 40/31, 80/31
"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 22)"""
