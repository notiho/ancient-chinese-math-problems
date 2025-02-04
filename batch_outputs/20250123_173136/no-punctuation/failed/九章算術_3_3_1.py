"""
今有女子善織日自倍五日織五尺問日織幾何
術曰置一二四八十六為列衰副并為法以五尺乘未并者各自為實實如法得一尺
荅曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

"""
Suppose there is a woman skilled in weaving. Each day, she doubles her output.
In five days, she weaves 5 chi.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a sequence, each representing the output for a day.
Add them together, obtaining the divisor.
Multiply the total 5 chi by the numbers in the sequence that have not been added together, each becoming the dividend.
Divide each dividend by the divisor, obtaining the output for each day.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# 置一二四八十六為列
列 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列)

# 以五尺乘未并者
總織 = 5  # 五尺
實 = [總織 * i for i in 列]

# 各自為實，實如法得一尺
結果 = [Fraction(i, 法) for i in 実]

# 初日織 a 寸
a = 結果[0] * 10  # 將 chi 轉為 cun

# 次日織 b 寸
b = 結果[1] * 10  # 將 chi 轉為 cun

# 次日織 c 寸
c = 結果[2] * 10  # 將 chi 轉為 cun

# 次日織 d 尺
d = 結果[3]

# 次日織 e 尺
e = 結果[4]
"""
Code error: name '実' is not defined"""
