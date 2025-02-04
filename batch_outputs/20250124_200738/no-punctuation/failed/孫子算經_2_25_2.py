"""
今有女子善織日自倍五日織通五尺問日織幾何
術曰各置列衰副并得三十一為法以五尺乘并者各自為實實如法而一即得
答曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day she doubles her output.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Place the outputs for each day in a sequence, each becoming its own decreasing term.
In auxiliary, add them, obtaining 31 as the divisor.
Multiply the total 5 chi by the unadded terms, each becoming its own dividend.
Divide each dividend by the divisor, obtaining the daily outputs.

Answer: On the first day, she weaves *a* cun. On the second day, she weaves *b* cun. On the third day, she weaves *c* cun. On the fourth day, she weaves *d* chi. On the fifth day, she weaves *e* chi.
"""

# Total weaving in 5 days
總織 = 5  # chi

# Convert chi to cun (1 chi = 10 cun)
總織 = 總織 * 10  # cun

# Daily weaving sequence (doubles each day)
日織序列 = [1, 2, 4, 8, 16]

# Add them to get the divisor
法 = sum(日織序列)

# Multiply total weaving by each term in the sequence
實 = [總織 * i for i in 日織序列]

# Divide each term by the divisor to get daily outputs
outputs = [Fraction(i, 法) for i in 実]

# Convert the outputs back to chi and cun
a = outputs[0]  # First day in cun
b = outputs[1]  # Second day in cun
c = outputs[2]  # Third day in cun
d = Fraction(outputs[3], 10)  # Fourth day in chi
e = Fraction(outputs[4], 10)  # Fifth day in chi#----- content ends here -----

"""
Code error: name '実' is not defined"""
