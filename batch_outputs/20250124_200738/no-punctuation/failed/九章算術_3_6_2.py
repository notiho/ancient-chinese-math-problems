"""
今有稟粟五斛五人分之欲令三人得三二人得二問各幾何
術曰置三人人三二人人二為列衰副并為法以五斛乘未并者各自為實實如法得一斛
荅曰 a人 人得 b斛  c人 人得 d斗 
"""

#----- content starts here -----
"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 hu in total, and 2 people receive 2 hu in total.
Question: how much does each group receive?

The procedure says: Place 3 for the 3 people and 2 for the 2 people as a sequence.
Each of them becomes an element in the decreasing sequence.
In auxiliary, add them together to form the divisor.
Multiply the 5 hu by the numbers that have not been added together, and each becomes its own dividend.
Divide the dividend by the divisor to obtain the amount of millet for each group.

Answer: *a* people receive *b* hu, and *c* people receive *d* dou.
"""

# 稟粟五斛
稟粟 = 5

# 三人得三
三人 = 3

# 二人得二
二人 = 2

# 置三人人三，二人人二，為列衰
列 = [三人, 二人]

# 副并為法
法 = sum(列)

# 以五斛乘未并者，各自為實
實 = [稟粟 * i for i in 列]

# 實如法得一斛
三人得 = Fraction(實[0], 法)
二人得 = Fraction(實[1], 法)

# Convert to appropriate units (1 hu = 10 dou)
a = 3
b = 三人得  # in hu
c = 2
d = 二人得 * 10  # in dou#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 3
Variable 'd' has wrong value. Expected: 100/13, Actual: 20"""
