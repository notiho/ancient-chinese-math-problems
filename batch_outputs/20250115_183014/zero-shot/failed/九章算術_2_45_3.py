"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we need to determine the values of `a`, `b`, `c`, and `d` based on the given information. Here's the Python code to compute the values:


"""


from fractions import Fraction

# Given data
total_money = 980  # Total money in units
total_arrows = 5820  # Total arrows in units

# Let the rates be:
# a arrows per 1 unit of money (cheaper rate)
# c arrows per 1 unit of money (more expensive rate)
# b units of money for a arrows
# d units of money for c arrows

# The problem states that the total money and total arrows are distributed between these two rates.

# Step 1: Assume the cheaper rate is `a` arrows per 1 unit of money, and the expensive rate is `c` arrows per 1 unit of money.
# Step 2: Let `b` units of money be spent on the cheaper rate, and `d` units of money be spent on the expensive rate.
# Step 3: The total money spent is `b + d = total_money`.
# Step 4: The total arrows bought is `a*b + c*d = total_arrows`.

# From the problem, we know:
# a = 7 (cheaper rate: 7 arrows per 1 unit of money)
# c = 5 (expensive rate: 5 arrows per 1 unit of money)

a = 7
c = 5

# Using the total money and total arrows equations:
# b + d = 980
# 7*b + 5*d = 5820

# Solve for b and d
# From b + d = 980, we get d = 980 - b
# Substitute d into the second equation:
# 7*b + 5*(980 - b) = 5820
# 7*b + 4900 - 5*b = 5820
# 2*b = 920
# b = 460

b = 460  # Money spent at the cheaper rate
d = total_money - b  # Money spent at the expensive rate
d = 980 - 460

# Verify the solution
# Total arrows from the cheaper rate: a * b = 7 * 460
# Total arrows from the expensive rate: c * d = 5 * 520
# Total arrows = 7*460 + 5*520 = 5820

# Final values
a = 7  # Cheaper rate: 7 arrows per 1 unit of money
b = 460  # Money spent at the cheaper rate
c = 5  # Expensive rate: 5 arrows per 1 unit of money
d = 520  # Money spent at the expensive rate


"""


The solution is:
- `a = 7` arrows per 1 unit of money (cheaper rate)
- `b = 460` units of money spent at the cheaper rate
- `c = 5` arrows per 1 unit of money (expensive rate)
- `d = 520` units of money spent at the expensive rate
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 7
Variable 'b' has wrong value. Expected: 5, Actual: 460
Variable 'c' has wrong value. Expected: 5520, Actual: 5
Variable 'd' has wrong value. Expected: 6, Actual: 520"""
