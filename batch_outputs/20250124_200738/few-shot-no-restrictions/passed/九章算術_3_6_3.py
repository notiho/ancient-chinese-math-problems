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
Add the auxiliary values to obtain the divisor.
Multiply the 5 hu by the uncombined values, obtaining the dividend for each group.
Divide the dividend by the divisor to obtain the amount of millet per person.

Answer: *a* people, each receives *b* hu. *c* people, each receives *d* dou.
"""

from fractions import Fraction

# 稟粟五斛
總粟 = 5  # in hu

# 三人，人三；二人，人二，為列衰
三人 = 3
二人 = 2
三人分配 = 3  # each of the 3 people gets 3
二人分配 = 2  # each of the 2 people gets 2

# 副并為法
法 = (三人 * 三人分配) + (二人 * 二人分配)

# 以五斛乘未并者，各自為實
三人實 = 總粟 * 三人分配
二人實 = 總粟 * 二人分配

# 實如法得一斛
三人每人得 = Fraction(三人實, 法)
二人每人得 = Fraction(二人實, 法)

# Convert hu to dou (1 hu = 10 dou)
三人每人得斗 = 三人每人得 * 10
二人每人得斗 = 二人每人得 * 10

# Final answer
a = 三人
b = 三人每人得
c = 二人
d = 二人每人得斗

# Output the results
a, b, c, d#----- content ends here -----

"""
"""
