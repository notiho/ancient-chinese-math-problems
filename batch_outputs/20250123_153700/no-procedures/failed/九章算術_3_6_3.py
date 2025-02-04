"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

"""
Suppose there are 5 hu of millet to be distributed among 5 people.
It is desired that 3 people receive 3 hu in total, and 2 people receive 2 hu in total.
Question: how much does each group receive?

Answer: *a* people, each gets *b* hu; *c* people, each gets *d* dou.
"""

from fractions import Fraction

# Total millet
total_millet = 5  # in hu

# Group 1: 3 people get 3 hu in total
a = 3
b = Fraction(3, a)  # Each person in group 1 gets 3 hu divided by 3 people

# Group 2: 2 people get 2 hu in total
c = 2
d = Fraction(2 * 10, c)  # Convert 2 hu to dou (1 hu = 10 dou), then divide by 2 people

# Results
a, b, c, d
"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 1
Variable 'd' has wrong value. Expected: 100/13, Actual: 10"""
