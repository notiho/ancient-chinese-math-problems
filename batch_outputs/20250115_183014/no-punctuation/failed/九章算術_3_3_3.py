"""
今有女子善織日自倍五日織五尺問日織幾何
術曰置一二四八十六為列衰副并為法以五尺乘未并者各自為實實如法得一尺
荅曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

"""
Suppose there is a woman skilled in weaving. Each day, she doubles her output.
In five days, she weaves 5 chi in total.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a sequence, each representing the output for a day.
Add them together to obtain the divisor.
Multiply the total 5 chi by each of the individual values in the sequence (before summing), obtaining the dividend for each day.
Divide each dividend by the divisor to obtain the output for each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 日自倍，列置 1, 2, 4, 8, 16
日倍列 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(日倍列)

# 置五尺
總織 = 5

# 以五尺乘未并者，各自為實
實 = [總織 * i for i in 日倍列]

# 實如法得每日織量
每日織量 = [Fraction(i, 法) for i in 实]

# 分別計算每日織量
a = 每日織量[0] * 10  # 第一日織量，轉換為寸
b = 每日織量[1] * 10  # 第二日織量，轉換為寸
c = 每日織量[2] * 10  # 第三日織量，轉換為寸
d = 每日織量[3]       # 第四日織量，保持為尺
e = 每日織量[4]       # 第五日織量，保持為尺
"""
Code error: name '实' is not defined"""
