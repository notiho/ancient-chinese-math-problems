"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (錢). The rule is that the sum of the amounts received by the first two people (the "upper two") is equal to the sum of the amounts received by the last three people (the "lower three").
Question: how much does each person get?

Answer: Jia (甲) gets *a* qian, Yi (乙) gets *b* qian, Bing (丙) gets *c* qian, Ding (丁) gets *d* qian, Wu (戊) gets *e* qian.
"""

from fractions import Fraction

# Total money
total_money = 5

# Let the amounts received by the five people be:
# Jia (甲): a
# Yi (乙): b
# Bing (丙): c
# Ding (丁): d
# Wu (戊): e

# Rule 1: The total money is 5 qian
# a + b + c + d + e = 5

# Rule 2: The sum of the amounts received by the first two people equals the sum of the amounts received by the last three people
# a + b = c + d + e

# From Rule 1 and Rule 2, we can deduce:
# c + d + e = 5 - (a + b)
# a + b = c + d + e = 5 / 2 = 2.5

# Distribute the money equally among the groups:
a = Fraction(2, 1)  # Jia gets 2 qian
b = Fraction(1, 2)  # Yi gets 0.5 qian
c = Fraction(1, 2)  # Bing gets 0.5 qian
d = Fraction(1, 2)  # Ding gets 0.5 qian
e = Fraction(1, 2)  # Wu gets 0.5 qian

# Results
a, b, c, d, e#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 2
Variable 'b' has wrong value. Expected: 7/6, Actual: 1/2
Variable 'c' has wrong value. Expected: 1, Actual: 1/2
Variable 'd' has wrong value. Expected: 5/6, Actual: 1/2
Variable 'e' has wrong value. Expected: 2/3, Actual: 1/2"""
