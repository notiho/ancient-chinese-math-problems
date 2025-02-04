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

The procedure says: Place 3 people, each receiving 3, and 2 people, each receiving 2, in a decreasing sequence.
Add these as the divisor.
Multiply the 5 hu by the uncombined numbers, obtaining the dividend for each group.
Divide the dividend by the divisor to obtain the amount of millet each person receives.

Answer: *a* people, each receiving *b* hu. *c* people, each receiving *d* dou.
"""

from fractions import Fraction

# 稟粟五斛
粟 = 5  # hu

# 三人，人三；二人，人二
三人 = 3
二人 = 2

# 為列衰
列衰 = [三人, 二人]

# 副并為法
法 = sum(列衰)

# 以五斛乘未并者，各自為實
實 = [粟 * i for i in 列衰]

# 實如法得一斛
三人得 = Fraction(實[0], 法)
二人得 = Fraction(實[1], 法)

# Convert hu to dou (1 hu = 10 dou)
三人得斗 = 三人得 * 10
二人得斗 = 二人得 * 10

# Final results
a = 3  # 三人
b = 三人得  # hu per person
c = 2  # 二人
d = 二人得斗  # dou per person

# Output results
a, b, c, d#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 3
Variable 'd' has wrong value. Expected: 100/13, Actual: 20"""
