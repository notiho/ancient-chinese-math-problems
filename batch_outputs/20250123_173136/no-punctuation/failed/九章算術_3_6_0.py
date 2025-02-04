"""
今有稟粟五斛五人分之欲令三人得三二人得二問各幾何
術曰置三人人三二人人二為列衰副并為法以五斛乘未并者各自為實實如法得一斛
荅曰 a人 人得 b斛  c人 人得 d斗 
"""

"""
Suppose there are 5 hu of grain to be distributed among 5 people.
It is desired that 3 people receive 3 hu, and 2 people receive 2 hu.
Question: how much does each group receive?

The procedure says: Place 3 people each receiving 3 hu, and 2 people each receiving 2 hu, forming a sequence.
Each becomes its own decreasing sequence.
Add them together to form the divisor.
Multiply the 5 hu by the unadded numbers, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of grain per person.

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
列 = [三人 * 三人得, 二人 * 二人得]

# 副并為法
法 = sum(列)

# 以五斛乘未并者，各自為實
實 = [稟粟 * i for i in 列]

# 實如法得一斛
三人分得 = Fraction(實[0], 法)
二人分得 = Fraction(實[1], 法)

# Convert hu to dou (1 hu = 10 dou)
三人分得斗 = 三人分得 * 10
二人分得斗 = 二人分得 * 10

a = 三人
b = 三人分得
c = 二人
d = 二人分得斗
"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 45/13
Variable 'd' has wrong value. Expected: 100/13, Actual: 200/13"""
