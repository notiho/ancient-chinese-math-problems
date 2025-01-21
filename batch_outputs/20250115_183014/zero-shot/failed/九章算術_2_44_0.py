"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we need to determine the values of \( a \), \( b \), \( c \), and \( d \) based on the given problem. The problem involves dividing 610 units of money to buy 2100 units of feathers, where the feathers are of two types with different rates (price per unit). Let's translate this into Python code.


"""


from fractions import Fraction

# Total money and total feathers
total_money = 610  # in units of money
total_feathers = 2100  # in units of feathers

# Let the rates be such that:
# a feathers cost 1 unit of money (a feathers per unit of money)
# c feathers cost 1 unit of money (c feathers per unit of money)

# The total feathers are divided into two groups:
# Group 1: a feathers per unit of money
# Group 2: c feathers per unit of money

# Let b be the number of units of money spent on Group 1
# Let d be the number of units of money spent on Group 2

# The total money spent is:
# b + d = total_money

# The total feathers bought is:
# a * b + c * d = total_feathers

# Assume a = 5 (5 feathers per unit of money) and c = 3 (3 feathers per unit of money)
a = 5
c = 3

# Solve for b and d using the equations:
# b + d = total_money
# a * b + c * d = total_feathers

# Substituting a and c:
# 5 * b + 3 * d = 2100
# b + d = 610

# Solve for b and d
# From b + d = 610, we get d = 610 - b
# Substitute d into 5 * b + 3 * d = 2100:
# 5 * b + 3 * (610 - b) = 2100
# 5 * b + 1830 - 3 * b = 2100
# 2 * b = 270
# b = 135

b = 135
d = total_money - b  # d = 610 - 135
d = 475

# Now we have b and d. Verify:
# Total feathers = a * b + c * d
# Total feathers = 5 * 135 + 3 * 475 = 675 + 1425 = 2100 (correct)

# Final values:
# a = 5 feathers per unit of money
# b = 135 units of money
# c = 3 feathers per unit of money
# d = 475 units of money


"""


### Final Answer:
- \( a = 5 \) feathers per unit of money
- \( b = 135 \) units of money
- \( c = 3 \) feathers per unit of money
- \( d = 475 \) units of money
"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 5
Variable 'b' has wrong value. Expected: 3, Actual: 135
Variable 'c' has wrong value. Expected: 960, Actual: 3
Variable 'd' has wrong value. Expected: 4, Actual: 475"""
