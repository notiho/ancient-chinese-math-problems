"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

"""
To solve this problem, we need to distribute 5 units of money among 5 people (甲, 乙, 丙, 丁, 戊) such that the total money received by the first two people (甲 and 乙) equals the total money received by the last three people (丙, 丁, 戊). Let's translate this into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money to be distributed
total_money = 5

# Let the money received by each person be:
# a = money received by 甲
# b = money received by 乙
# c = money received by 丙
# d = money received by 丁
# e = money received by 戊

# The conditions are:
# 1. a + b + c + d + e = total_money
# 2. a + b = c + d + e

# From condition 2, we can substitute c + d + e with a + b in condition 1:
# a + b + (a + b) = total_money
# 2a + 2b = total_money
# a + b = total_money / 2

# Now, distribute the money equally:
a = b = Fraction(total_money, 6)  # Each of the first two people gets 1/6 of the total money
c = d = e = Fraction(total_money, 6) * 2  # Each of the last three people gets 2/6 of the total money

# Results
a = Fraction(1, 6)
b = Fraction(1, 6)
c = Fraction(2, 6)
d = Fraction(2, 6)
e = Fraction(2, 6)

# Output the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. The total money is divided such that the sum of the first two people's shares equals the sum of the last three people's shares.
2. By solving the equations, we find that each of the first two people (甲 and 乙) gets 1/6 of the total money, and each of the last three people (丙, 丁, 戊) gets 2/6 of the total money.

### Final Answer:
- 甲得 `a = 1/6` 錢
- 乙得 `b = 1/6` 錢
- 丙得 `c = 2/6` 錢
- 丁得 `d = 2/6` 錢
- 戊得 `e = 2/6` 錢
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 1/6
Variable 'b' has wrong value. Expected: 7/6, Actual: 1/6
Variable 'c' has wrong value. Expected: 1, Actual: 1/3
Variable 'd' has wrong value. Expected: 5/6, Actual: 1/3
Variable 'e' has wrong value. Expected: 2/3, Actual: 1/3"""
