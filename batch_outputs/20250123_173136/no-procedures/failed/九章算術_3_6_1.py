"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people. It is desired that 3 people each receive 3 hu, and 2 people each receive 2 hu.
Question: how much does each group receive?

Answer: *a* people, each gets *b* hu. *c* people, each gets *d* dou.
"""

# Total millet in hu
total_millet = 5  # hu

# Conversion: 1 hu = 10 dou
total_millet_in_dou = total_millet * 10  # dou

# Total people
total_people = 5

# Group 1: 3 people, each gets 3 dou
a = 3  # people
b = Fraction(3, 10)  # hu (3 dou = 3/10 hu)

# Group 2: 2 people, each gets 2 dou
c = 2  # people
d = 2  # dou
"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 3/10
Variable 'd' has wrong value. Expected: 100/13, Actual: 2"""
