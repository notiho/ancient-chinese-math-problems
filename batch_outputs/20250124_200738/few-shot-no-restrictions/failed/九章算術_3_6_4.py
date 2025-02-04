"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 hu in total, and 2 people receive 2 hu in total.
Question: how much does each person receive?

The procedure says: Place the 3 people, each receiving 3, and the 2 people, each receiving 2, as a decreasing sequence.
Add the auxiliary values to obtain the divisor.
Multiply the 5 hu by the uncombined values, obtaining the dividend for each group.
Divide the dividend by the divisor to obtain the amount of millet each person receives.

Answer: *a* people, each receives *b* hu. *c* people, each receives *d* dou.
"""

from fractions import Fraction

# 稟粟五斛
粟 = 5  # in hu

# 三人，人三；二人，人二
三人 = 3
二人 = 2

# 為列衰
列衰 = [三人, 二人]

# 副并為法
法 = sum(列衰)

# 以五斛乘未并者，各自為實
實三人 = 粟 * 三人
實二人 = 粟 * 二人

# 實如法得一斛
三人分得 = Fraction(實三人, 法)
二人分得 = Fraction(實二人, 法)

# Convert to dou (1 hu = 10 dou)
三人分得斗 = 三人分得 * 10
二人分得斗 = 二人分得 * 10

# Final answer
a = 3  # 三人
b = 三人分得  # 每人得 b 斛
c = 2  # 二人
d = 二人分得斗  # 每人得 d 斗

a, b, c, d#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 3
Variable 'd' has wrong value. Expected: 100/13, Actual: 20"""
