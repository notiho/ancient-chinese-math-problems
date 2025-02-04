"""
今有稟粟五斛，五人分之，欲令三人得三，二人得二。問︰各幾何？
荅曰： a人 ，人得 b斛 。 c人 ，人得 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 hu of millet to be distributed among 5 people. It is desired that 3 people each receive 3 hu, and 2 people each receive 2 hu.
Question: how much does each group receive?

Answer: *a* people each get *b* hu, and *c* people each get *d* dou.
"""

# Total millet
total_millet = 5  # in hu

# Convert hu to dou (1 hu = 10 dou)
total_millet_in_dou = total_millet * 10

# Total people
total_people = 5

# 3 people get 3 parts each (3 hu total)
a = 3  # number of people
b = Fraction(3 * total_millet_in_dou, 5 * 10)  # each person gets in hu

# 2 people get 2 parts each (2 hu total)
c = 2  # number of people
d = Fraction(2 * total_millet_in_dou, 5 * 10)  # each person gets in dou

# Final results
a_people = a
b_hu_per_person = b
c_people = c
d_dou_per_person = d#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 15/13, Actual: 3
Variable 'd' has wrong value. Expected: 100/13, Actual: 2"""
