"""
今有稟粟五斛五人分之欲令三人得三二人得二問各幾何
術曰置三人人三二人人二為列衰副并為法以五斛乘未并者各自為實實如法得一斛
荅曰 a人 人得 b斛  c人 人得 d斗 
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people each receive 3 parts, and 2 people each receive 2 parts.
Question: how much does each person receive?

The procedure says: Place 3 parts for 3 people and 2 parts for 2 people in a sequence.
Each becomes its own decreasing sequence.
Add them together to obtain the divisor.
Multiply the 5 hu by the unadded parts, and each becomes its own dividend.
Divide by the divisor to obtain the amount of millet for each part.

Answer: *a* people each receive *b* hu, and *c* people each receive *d* dou.
"""

from fractions import Fraction

# 稟粟五斛
粟 = 5  # in hu

# 三人人三，二人人二
三人 = 3
二人 = 2
三人分 = 3
二人分 = 2

# 副并為法
法 = (三人 * 三人分) + (二人 * 二人分)

# 以五斛乘未并者
三人實 = 粟 * 三人分
二人實 = 粟 * 二人分

# 各自為實，實如法得一斛
三人得 = Fraction(三人實, 法)
二人得 = Fraction(二人實, 法)

# Convert hu to dou (1 hu = 10 dou)
三人得斗 = 三人得 * 10
二人得斗 = 二人得 * 10

a = 三人
b = 三人得
c = 二人
d = 二人得斗
"""
"""
