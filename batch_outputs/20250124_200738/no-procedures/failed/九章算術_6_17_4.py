"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (錢). 
The rule is that the sum of the amounts received by the first two people (the "upper two") equals the sum of the amounts received by the last three people (the "lower three").
Question: how much does each person get?

Answer: Jia (甲) gets *a* qian, Yi (乙) gets *b* qian, Bing (丙) gets *c* qian, Ding (丁) gets *d* qian, and Wu (戊) gets *e* qian.
"""

from fractions import Fraction

# Total money to be divided
total_money = 5

# Let the amounts received by the five people be:
# a = Jia (甲), b = Yi (乙), c = Bing (丙), d = Ding (丁), e = Wu (戊)
# Rule: a + b = c + d + e
# Rule: a + b + c + d + e = total_money

# Assume a = b (upper two get equal amounts) and c = d = e (lower three get equal amounts)
# Then:
# a + a = c + c + c
# 2a = 3c
# a + a + c + c + c = total_money
# 2a + 3c = total_money

# Solve for a and c
c = Fraction(total_money, 5)  # Each of the lower three gets 1 qian
a = Fraction(3 * c, 2)        # Each of the upper two gets 1.5 qian

# Assign values
b = a  # Yi gets the same as Jia
d = c  # Ding gets the same as Bing
e = c  # Wu gets the same as Bing

# Results
甲得 = a
乙得 = b
丙得 = c
丁得 = d
戊得 = e

甲得, 乙得, 丙得, 丁得, 戊得#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 3/2
Variable 'b' has wrong value. Expected: 7/6, Actual: 3/2
Variable 'd' has wrong value. Expected: 5/6, Actual: 1
Variable 'e' has wrong value. Expected: 2/3, Actual: 1"""
