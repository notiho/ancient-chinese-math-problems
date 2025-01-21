"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 hu in total, and 2 people receive 2 hu in total.
Question: how much does each group receive?

Answer: *a* people, each gets *b* hu. *c* people, each gets *d* dou.
"""

# Total millet
total_millet = 5  # in hu

# Group 1: 3 people share 3 hu
a = 3
b = Fraction(3, a)  # each person in group 1 gets this much hu

# Group 2: 2 people share 2 hu
c = 2
d = Fraction(2, c) * 10  # each person in group 2 gets this much dou (1 hu = 10 dou)

# Final results
a_people = a
b_hu_per_person = b
c_people = c
d_dou_per_person = d
"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 1
Variable 'd' has wrong value. Expected: 100/13, Actual: 10"""
