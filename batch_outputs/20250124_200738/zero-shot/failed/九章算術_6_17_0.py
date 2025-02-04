"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
術曰：置錢錐行衰，并上二人為九，并下三人為六。六少於九，三。以三均加焉，副并為法。以所分錢乘未并者各自為實。實如法得一錢。
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

"""
To solve this problem, we need to distribute 5 coins among 5 people such that the sum of the coins received by the first two people equals the sum of the coins received by the last three people. Let's translate the problem into Python code.


"""

#----- content starts here -----

from fractions import Fraction

# Total coins to distribute
total_coins = 5

# Let the coins received by each person be:
# a = coins received by person 1 (甲)
# b = coins received by person 2 (乙)
# c = coins received by person 3 (丙)
# d = coins received by person 4 (丁)
# e = coins received by person 5 (戊)

# The conditions are:
# 1. a + b + c + d + e = total_coins
# 2. a + b = c + d + e

# From condition 2, we can express c + d + e as a + b.
# Substituting this into condition 1:
# a + b + (a + b) = total_coins
# 2 * (a + b) = total_coins
# a + b = total_coins / 2

# Since the total_coins is 5, we have:
a_plus_b = Fraction(total_coins, 2)  # a + b = 5/2

# Similarly, c + d + e = a + b = 5/2

# To distribute the coins equally:
a = b = Fraction(a_plus_b, 2)  # a = b = (5/2) / 2 = 5/4
c = d = e = Fraction(a_plus_b, 3)  # c = d = e = (5/2) / 3 = 5/6

# Results
a = Fraction(5, 4)  # Coins received by person 1 (甲)
b = Fraction(5, 4)  # Coins received by person 2 (乙)
c = Fraction(5, 6)  # Coins received by person 3 (丙)
d = Fraction(5, 6)  # Coins received by person 4 (丁)
e = Fraction(5, 6)  # Coins received by person 5 (戊)

# The solution is:
# 甲得 a錢 = 5/4錢
# 乙得 b錢 = 5/4錢
# 丙得 c錢 = 5/6錢
# 丁得 d錢 = 5/6錢
# 戊得 e錢 = 5/6錢
#----- content ends here -----


"""


This Python code calculates the distribution of coins among the five people while satisfying the given conditions.
"""


"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 5/4
Variable 'b' has wrong value. Expected: 7/6, Actual: 5/4
Variable 'c' has wrong value. Expected: 1, Actual: 5/6
Variable 'e' has wrong value. Expected: 2/3, Actual: 5/6"""
