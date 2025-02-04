"""
今有女子善織日自倍五日織通五尺問日織幾何
術曰各置列衰副并得三十一為法以五尺乘并者各自為實實如法而一即得
答曰初日織 a寸 次日織 b寸 次日織 c寸 次日織 d尺 次日織 e尺 
"""

#----- content starts here -----
"""
Suppose there is a woman skilled in weaving. Each day, she doubles her output.
In five days, she weaves a total of 5 chi.
Question: how much does she weave each day?

The procedure says: Arrange the sequence of daily outputs in decreasing order.
Add them together, obtaining 31 as the divisor.
Multiply the total 5 chi by each of the individual terms in the sequence, obtaining the dividend for each day.
Divide each dividend by the divisor, obtaining the daily output.

Answer: On the first day, she weaves *a* cun; on the second day, she weaves *b* cun; on the third day, she weaves *c* cun; on the fourth day, she weaves *d* chi; on the fifth day, she weaves *e* chi.
"""

# Total woven in five days: 5 chi
總織 = 5

# Convert chi to cun (1 chi = 10 cun)
總織 = 總織 * 10

# Daily output sequence (doubles each day)
日序 = [1, 2, 4, 8, 16]

# Add the sequence to get the divisor
法 = sum(日序)

# Multiply the total by each term in the sequence to get the dividend
實 = [總織 * i for i in 日序]

# Divide each dividend by the divisor to get daily outputs
outputs = [Fraction(i, 法) for i in 実]

# Convert outputs to chi and cun
a = outputs[0]  # First day (in cun)
b = outputs[1]  # Second day (in cun)
c = outputs[2]  # Third day (in cun)
d = Fraction(outputs[3], 10)  # Fourth day (in chi)
e = Fraction(outputs[4], 10)  # Fifth day (in chi)#----- content ends here -----

"""
Code error: name '実' is not defined"""
