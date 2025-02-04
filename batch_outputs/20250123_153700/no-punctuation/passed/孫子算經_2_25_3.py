"""
今有女子善織日自倍五日織通五尺問日織幾何
術曰各置列衰副并得三十一為法以五尺乘并者各自為實實如法而一即得
答曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

"""
Suppose there is a woman skilled in weaving. Each day, she doubles her output.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the daily outputs in a sequence, each as a decreasing term.
Add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by the unadded terms, each as a dividend.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total woven in 5 days: 5 chi
總織 = 5  # chi

# Convert chi to cun (1 chi = 10 cun)
總織 = 總織 * 10  # cun

# Daily weaving sequence doubles: 1, 2, 4, 8, 16
日織序列 = [1, 2, 4, 8, 16]

# Add them together to get the divisor (法)
法 = sum(日織序列)

# Multiply the total woven by each term in the sequence to get the dividend (實)
實 = [總織 * i for i in 日織序列]

# Divide each dividend by the divisor to get the daily outputs
每日織 = [Fraction(i, 法) for i in 實]

# Convert the results back to chi and cun
a = 每日織[0]  # First day in cun
b = 每日織[1]  # Second day in cun
c = 每日織[2]  # Third day in cun
d = 每日織[3] / 10  # Fourth day in chi
e = 每日織[4] / 10  # Fifth day in chi
"""
"""
