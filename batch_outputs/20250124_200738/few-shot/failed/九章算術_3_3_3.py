"""
今有女子善織，日自倍，五日織五尺。問︰日織幾何？
術曰：置一、二、四、八、十六為列衰，副并為法，以五尺乘未并者，各自為實，實如法得一尺。
荅曰：初日織 a寸 。次日織 b寸 。次日織 c寸 。次日織 d尺 。次日織 e尺 。
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles.
In five days, she weaves 5 chi. 
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a decreasing sequence.
Add them together to obtain the divisor.
Multiply the 5 chi by the individual terms of the sequence (before summing), obtaining the dividends.
Divide each dividend by the divisor to obtain the weaving output for each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. 
On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. 
On the fifth day, she weaves *e* chi.
"""

# 置一、二、四、八、十六為列衰
列衰 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列衰)

# 以五尺乘未并者，各自為實
總織 = 5  # 五尺
實 = [總織 * i for i in 列衰]

# 實如法得一尺
織量 = [Fraction(i, 法) for i in 実]

# Convert to appropriate units (1 chi = 10 cun)
a = 織量[0] * 10  # 初日織 a 寸
b = 織量[1] * 10  # 次日織 b 寸
c = 織量[2] * 10  # 次日織 c 寸
d = 織量[3]       # 次日織 d 尺
e = 織量[4]       # 次日織 e 尺#----- content ends here -----

"""
Code error: name '実' is not defined"""
