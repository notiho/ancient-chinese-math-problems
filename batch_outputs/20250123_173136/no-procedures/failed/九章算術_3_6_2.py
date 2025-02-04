"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people. It is desired that 3 people get 3 hu in total, and 2 people get 2 hu in total.
Question: how much does each group get?

Answer: *a* people, each gets *b* hu. *c* people, each gets *d* dou.
"""

from fractions import Fraction

# Total millet
total_millet = 5  # in hu

# Group 1: 3 people get 3 hu in total
a = 3
b = Fraction(3, a)  # each person gets 3 hu divided by 3 people

# Group 2: 2 people get 2 hu in total
c = 2
d = Fraction(2, c) * 10  # each person gets 2 hu divided by 2 people, converted to dou (1 hu = 10 dou)

# Results
a_people = a
b_hu_per_person = b
c_people = c
d_dou_per_person = d

a_people, b_hu_per_person, c_people, d_dou_per_person
"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 1
Variable 'd' has wrong value. Expected: 100/13, Actual: 10"""
