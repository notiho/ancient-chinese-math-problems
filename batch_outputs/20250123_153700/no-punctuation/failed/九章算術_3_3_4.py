"""
今有女子善織日自倍五日織五尺問日織幾何
術曰置一二四八十六為列衰副并為法以五尺乘未并者各自為實實如法得一尺
荅曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

"""
Suppose there is a woman skilled in weaving. Each day, she doubles her output.
In five days, she weaves 5 chi in total.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a sequence, each representing the output of a day.
Add them together to obtain the divisor.
Multiply the total 5 chi by each of the numbers in the sequence (before summing), obtaining the dividend for each day.
Divide each dividend by the divisor to obtain the output for each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 五日織五尺
總織 = 5

# 置一二四八十六為列
列 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列)

# 以五尺乘未并者，各自為實
實 = [總織 * i for i in列]

# 實如法得每日織量
每日織量 = [Fraction(i, 法) for i in 實]

# 初日織 a 寸
a = 每日織量[0] * 10  # Convert chi to cun

# 次日織 b 寸
b = 每日織量[1] * 10  # Convert chi to cun

# 次日織 c 寸
c = 每日織量[2] * 10  # Convert chi to cun

# 次日織 d 尺
d = 每日織量[3]

# 次日織 e 尺
e = 每日織量[4]
"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 25)"""
