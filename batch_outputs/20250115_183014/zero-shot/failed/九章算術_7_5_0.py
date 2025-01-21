"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
# When each person pays 5, the total is 45 short
rate1 = 5
short1 = 45

# When each person pays 7, the total is 3 short
rate2 = 7
short2 = 3

# Calculate the number of people (a) and the price of the sheep (b)
# Using the method described in the problem:
# 实 = (rate2 * short1 - rate1 * short2)
# 法 = (rate2 - rate1)
# 人数 (a) = 实 / 法
# 羊价 (b) = 人数 * rate1 + short1

实 = rate2 * short1 - rate1 * short2
法 = rate2 - rate1
a = Fraction(实, 法)
b = a * rate1 + short1

# Results
a, b


"""


This code calculates the number of people (`a`) and the price of the sheep (`b`) using the method described in the ancient text. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 21, Actual: 150
Variable 'b' has wrong value. Expected: 150, Actual: 795"""
