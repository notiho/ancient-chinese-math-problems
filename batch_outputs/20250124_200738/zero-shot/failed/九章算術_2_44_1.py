"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we need to determine the values of `a`, `b`, `c`, and `d` based on the given problem. Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 610  # total money in 錢
total_feathers = 2100  # total feathers in 翭

# Step 1: Compute the average rate (feathers per 錢)
average_rate = Fraction(total_feathers, total_money)

# Step 2: Determine the rates for the two groups
# Let the rates be a翭 per 錢 and c翭 per 錢
# Assume a翭 > c翭
a = average_rate.numerator + 1  # a翭 per 錢
c = average_rate.numerator - 1  # c翭 per 錢

# Step 3: Compute the corresponding money for each group
# Let b錢 be the money for a翭 per 錢, and d錢 be the money for c翭 per 錢
# Total money = b + d
# Total feathers = a * b + c * d
# Solve for b and d
b = Fraction(total_feathers - c * total_money, a - c)
d = total_money - b

# Step 4: Verify the solution
assert a * b + c * d == total_feathers
assert b + d == total_money

# Results
a = a  # a翭 per 錢
b = b  # b錢
c = c  # c翭 per 錢
d = d  # d錢

# Output the results
a, b, c, d
#----- content ends here -----


"""


This code calculates the values of `a`, `b`, `c`, and `d` based on the problem's description. The results are stored in the respective variables.
"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 211
Variable 'b' has wrong value. Expected: 3, Actual: -62695
Variable 'c' has wrong value. Expected: 960, Actual: 209
Variable 'd' has wrong value. Expected: 4, Actual: 63305"""
