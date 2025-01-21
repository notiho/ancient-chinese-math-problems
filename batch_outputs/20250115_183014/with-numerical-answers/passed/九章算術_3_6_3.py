"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a(=3)人 ，人得 b(=15/13)斛 。 c(=2)人 ，人得 d(=100/13)斗 。
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 parts, and 2 people receive 2 parts.
Question: how much does each person receive?

The procedure says: Place 3 people, each receiving 3 parts; and 2 people, each receiving 2 parts, forming a decreasing sequence.
Add the auxiliary values, obtaining the divisor.
Multiply the 5 hu by the uncombined values, each becoming its own dividend.
Divide the dividends by the divisor, obtaining the amount of millet per person.

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
b = Fraction(三人實, 法)  # Each of the 3 people gets 15/13 hu
d = Fraction(二人實, 法) * 10  # Each of the 2 people gets 100/13 dou (1 hu = 10 dou)

# Assigning values
a = 三人  # 3 people
c = 二人  # 2 people
"""
"""
