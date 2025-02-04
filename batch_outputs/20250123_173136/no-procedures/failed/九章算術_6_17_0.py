"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

"""
Suppose there are 5 people dividing 5 qian (錢). The condition is that the sum of the amounts received by the first two people (the "upper two") is equal to the sum of the amounts received by the last three people (the "lower three").
Question: how much does each person get?

Answer: Person A (甲) gets *a* qian, Person B (乙) gets *b* qian, Person C (丙) gets *c* qian, Person D (丁) gets *d* qian, and Person E (戊) gets *e* qian.
"""

from fractions import Fraction

# Total qian to divide
total_qian = 5

# Let the amounts received by each person be:
# a = amount for 甲
# b = amount for 乙
# c = amount for 丙
# d = amount for 丁
# e = amount for 戊

# Condition 1: The total sum of all amounts must equal 5 qian
# a + b + c + d + e = 5

# Condition 2: The sum of the amounts received by the first two people equals the sum of the amounts received by the last three people
# a + b = c + d + e

# From the above two conditions, we can solve:
# c + d + e = 5 - (a + b)
# a + b = c + d + e
# Therefore, a + b = (5 - (a + b))
# Let x = a + b, then x = 5 - x
# 2x = 5
# x = 5 / 2

# So, a + b = 5/2 and c + d + e = 5/2

# Distribute the amounts equally among the groups:
a = Fraction(5, 4)  # 甲 gets 5/4 qian
b = Fraction(5, 4)  # 乙 gets 5/4 qian
c = Fraction(5, 6)  # 丙 gets 5/6 qian
d = Fraction(5, 6)  # 丁 gets 5/6 qian
e = Fraction(5, 6)  # 戊 gets 5/6 qian

# Results
a, b, c, d, e
"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 5/4
Variable 'b' has wrong value. Expected: 7/6, Actual: 5/4
Variable 'c' has wrong value. Expected: 1, Actual: 5/6
Variable 'e' has wrong value. Expected: 2/3, Actual: 5/6"""
