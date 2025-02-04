"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
術曰：置三人，人三；二人，人二，為列衰。副并為法。以五斛乘未并者，各自為實。實如法得一斛。
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 hu, and 2 people receive 2 hu.
Question: how much does each person receive?

The procedure says: Place 3 people, each receiving 3, and 2 people, each receiving 2, as a decreasing sequence.
Add these together to form the divisor.
Multiply the 5 hu by the uncombined numbers, each forming its own dividend.
Divide the dividend by the divisor to obtain the amount of millet each person receives.

Answer: *a* people, each receives *b* hu. *c* people, each receives *d* dou.
"""

from fractions import Fraction

# 稟粟五斛
稟粟 = 5  # in hu

# 三人，人三；二人，人二，為列衰
三人 = 3
二人 = 2
三人分配 = 3
二人分配 = 2

# 副并為法
法 = (三人 * 三人分配) + (二人 * 二人分配)

# 以五斛乘未并者，各自為實
三人實 = 稟粟 * 三人分配
二人實 = 稟粟 * 二人分配

# 實如法得一斛
三人每人得 = Fraction(三人實, 法)
二人每人得 = Fraction(二人實, 法)

# Convert to hu and dou (1 hu = 10 dou)
三人每人得_斛 = 三人每人得
二人每人得_斗 = 二人每人得 * 10

a = 三人
b = 三人每人得_斛
c = 二人
d = 二人每人得_斗#----- content ends here -----

"""
"""
