"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a(=50/31)寸 。次日織 b(=100/31)寸 。次日織 c(=200/31)寸 。次日織 d(=40/31)尺 。次日織 e(=80/31)尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving, and her daily output doubles. In five days, she weaves 5 chi.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a decreasing sequence.
Add them together to obtain the divisor.
Multiply the 5 chi by the numbers that have not been added together, each becoming a dividend.
Divide the dividends by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a*(=50/31) cun. On the second day, she weaves *b*(=100/31) cun. On the third day, she weaves *c*(=200/31) cun. On the fourth day, she weaves *d*(=40/31) chi. On the fifth day, she weaves *e*(=80/31) chi.
"""

from fractions import Fraction

# 日自倍，五日織五尺
總織 = 5  # chi
日倍列 = [1, 2, 4, 8, 16]  # Sequence of daily doubling

# 副并為法
法 = sum(日倍列)

# 以五尺乘未并者，各自為實
實 = [總織 * 倍 for 倍 in 日倍列]

# 實如法得一尺
a, b, c = [Fraction(實[i], 法) * 10 for i in range(3)]  # Convert to cun (1 chi = 10 cun)
d, e = [Fraction(實[i], 法) for i in range(3, 5)]  # Keep in chi

# Results:
# 初日織 a(=50/31)寸
# 次日織 b(=100/31)寸
# 次日織 c(=200/31)寸
# 次日織 d(=40/31)尺
# 次日織 e(=80/31)尺#----- content ends here -----

"""
"""
