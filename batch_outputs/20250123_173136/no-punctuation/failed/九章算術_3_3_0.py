"""
今有女子善織日自倍五日織五尺問日織幾何
術曰置一二四八十六為列衰副并為法以五尺乘未并者各自為實實如法得一尺
荅曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

"""
Suppose there is a woman skilled in weaving. Each day, her output doubles.
In five days, she weaves 5 chi in total.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a sequence as a decreasing series.
In auxiliary, add them together to form the divisor.
Multiply the 5 chi by the unadded numbers in the sequence, each becoming its own dividend.
Divide each dividend by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a* cun; on the second day, she weaves *b* cun; on the third day, she weaves *c* cun; on the fourth day, she weaves *d* chi; on the fifth day, she weaves *e* chi.
"""

# 置一二四八十六為列
列 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列)

# 以五尺乘未并者
總織 = 5  # 五尺
實 = [總織 * i for i in 列]

# 各自為實，實如法得一尺
結果 = [Fraction(i, 法) for i in 实]

# 初日織 a 寸
a = 結果[0] * 10  # 將尺轉為寸

# 次日織 b 寸
b = 結果[1] * 10  # 將尺轉為寸

# 次日織 c 寸
c = 結果[2] * 10  # 將尺轉為寸

# 次日織 d 尺
d = 結果[3]

# 次日織 e 尺
e = 結果[4]
"""
Code error: name '实' is not defined"""
