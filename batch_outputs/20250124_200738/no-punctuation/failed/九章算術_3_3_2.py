"""
今有女子善織日自倍五日織五尺問日織幾何
術曰置一二四八十六為列衰副并為法以五尺乘未并者各自為實實如法得一尺
荅曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, her output doubles compared to the previous day.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place 1, 2, 4, 8, and 16 in a sequence, as a decreasing series.
In auxiliary, add them together to obtain the divisor.
Multiply the total 5 chi by the numbers that have not been added together, each becoming its own dividend.
Divide each dividend by the divisor to obtain the amount woven each day.

Answer: On the first day, she weaves *a* cun; on the second day, she weaves *b* cun; on the third day, she weaves *c* cun; on the fourth day, she weaves *d* chi; on the fifth day, she weaves *e* chi.
"""

# 置一二四八十六為列
列 = [1, 2, 4, 8, 16]

# 副并為法
法 = sum(列)

# 以五尺乘未并者
總織 = 5
實 = [總織 * i for i in列]

# 各自為實，實如法得一尺
分配 = [Fraction(i, 法) for i in 實]

# 初日織 a 寸
a = 分配[0] * 10  # Convert chi to cun

# 次日織 b 寸
b = 分配[1] * 10  # Convert chi to cun

# 次日織 c 寸
c = 分配[2] * 10  # Convert chi to cun

# 次日織 d 尺
d = 分配[3]

# 次日織 e 尺
e = 分配[4]#----- content ends here -----

"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 23)"""
