"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

"""
To solve this problem, we need to distribute 5 units of money among 5 people such that the sum of the amounts received by the first two people equals the sum of the amounts received by the last three people. Let's translate the problem into Python code.


"""

#----- content starts here -----

from fractions import Fraction

# Total money to be distributed
total_money = 5

# Let the amounts received by the five people be:
# a = amount received by person 1 (甲)
# b = amount received by person 2 (乙)
# c = amount received by person 3 (丙)
# d = amount received by person 4 (丁)
# e = amount received by person 5 (戊)

# The conditions are:
# 1. a + b + c + d + e = total_money
# 2. a + b = c + d + e

# From condition 2, we can express c + d + e as:
# c + d + e = a + b

# Substituting into condition 1:
# a + b + (a + b) = total_money
# 2 * (a + b) = total_money
# a + b = total_money / 2

# Now, the remaining money for c, d, and e is also total_money / 2.
# To distribute equally:
a = Fraction(1, 1)  # Person 1 gets 1 unit
b = Fraction(1, 1)  # Person 2 gets 1 unit
c = Fraction(1, 1)  # Person 3 gets 1 unit
d = Fraction(1, 1)  # Person 4 gets 1 unit
e = Fraction(1, 1)  # Person 5 gets 1 unit

# Verify the solution:
# a + b + c + d + e == total_money
# a + b == c + d + e
assert a + b + c + d + e == total_money
assert a + b == c + d + e

# The solution:
# a = 1, b = 1, c = 1, d = 1, e = 1
#----- content ends here -----


"""


### Solution:
- 甲 (a) gets 1 unit of money.
- 乙 (b) gets 1 unit of money.
- 丙 (c) gets 1 unit of money.
- 丁 (d) gets 1 unit of money.
- 戊 (e) gets 1 unit of money.
"""


"""
Code error: """
