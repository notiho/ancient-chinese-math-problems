"""
今有稟粟五斛五人分之欲令三人得三二人得二問各幾何
術曰置三人人三二人人二為列衰副并為法以五斛乘未并者各自為實實如法得一斛
荅曰 a人 人得 b斛  c人 人得 d斗 
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 hu, and 2 people receive 2 hu.
Question: how much does each group receive?

The procedure says: Place 3 hu for 3 people and 2 hu for 2 people as a sequence.
Each becomes its own decreasing sequence.
Add them together to form the divisor.
Multiply the 5 hu by the numbers that have not been added together, and each becomes its own dividend.
Divide the dividends by the divisor to obtain the distribution.

Answer: *a* people receive *b* hu, and *c* people receive *d* dou.
"""

# 稟粟五斛
稟粟 = 5

# 三人得三
三人 = 3
三人得 = 3

# 二人得二
二人 = 2
二人得 = 2

# 置三人人三，二人人二，為列衰
列衰 = [三人得, 二人得]

# 副并為法
法 = sum(列衰)

# 以五斛乘未并者，各自為實
三人實 = 稟粟 * 二人得
二人實 = 稟粟 * 三人得

# 實如法得一斛
三人分得 = Fraction(三人實, 法)
二人分得 = Fraction(二人實, 法)

# Convert to hu and dou (1 hu = 10 dou)
a = 三人
b = 三人分得  # in hu
c = 二人
d = 二人分得 * 10  # in dou
"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 2
Variable 'd' has wrong value. Expected: 100/13, Actual: 30"""
