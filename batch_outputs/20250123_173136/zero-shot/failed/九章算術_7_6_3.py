"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

"""
This problem involves solving for the number of people (`a`) and the price of a pig (`b`). Here's the Python code to compute the values:


"""


from fractions import Fraction

# Given data
excess = 100  # 盈一百
sufficient = 0  # 適足
shortfall = -100  # 不足一百
rate_high = 100  # 人出一百
rate_low = 90  # 人出九十

# Step 1: Calculate the number of people (a)
# Formula: a = (excess - shortfall) / (rate_high - rate_low)
a = Fraction(excess - shortfall, rate_high - rate_low)

# Step 2: Calculate the price of a pig (b)
# Formula: b = rate_low * a
b = rate_low * a

# Results
a, b


"""


This code calculates the number of people (`a`) and the price of a pig (`b`) using the method described in the problem. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 10, Actual: 20
Variable 'b' has wrong value. Expected: 900, Actual: 1800"""
