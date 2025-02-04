"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a(=3)人 ，人得 b(=15/13)斛 。 c(=2)人 ，人得 d(=100/13)斗 。
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 parts and 2 people receive 2 parts.
Question: how much does each person receive?

The procedure says: Place 3 people, each with 3 parts; and 2 people, each with 2 parts, forming a decreasing sequence.
Add these parts together to form the divisor.
Multiply the 5 hu by the uncombined parts, forming the dividend for each group.
Divide the dividend by the divisor to obtain the amount of millet per person.

Answer: *a*(=3) people each receive *b*(=15/13) hu. *c*(=2) people each receive *d*(=100/13) dou.
"""

from fractions import Fraction

# 稟粟五斛
稟粟 = 5  # in hu

# 三人，人三；二人，人二，為列衰
三人 = 3
二人 = 2
三人分 = 3
二人分 = 2

# 副并為法
法 = (三人 * 三人分) + (二人 * 二人分)

# 以五斛乘未并者，各自為實
三人實 = 稟粟 * 三人分
二人實 = 稟粟 * 二人分

# 實如法得一斛
三人每人得 = Fraction(三人實, 法)  # 15/13 hu
二人每人得 = Fraction(二人實, 法)  # 10/13 hu

# Convert 二人每人得 to dou (1 hu = 10 dou)
二人每人得斗 = 二人每人得 * 10  # 100/13 dou

# Final results
a = 三人  # 3 people
b = 三人每人得  # 15/13 hu
c = 二人  # 2 people
d = 二人每人得斗  # 100/13 dou
"""
"""
