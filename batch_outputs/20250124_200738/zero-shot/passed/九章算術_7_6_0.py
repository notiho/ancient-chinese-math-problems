"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
excess_amount = 100  # 盈一百
sufficient_amount = 90  # 適足
excess_total = 100  # 盈一百

# Step 1: Calculate the number of people (a)
difference_in_contribution = excess_amount - sufficient_amount  # 少減多
a = Fraction(excess_total, difference_in_contribution)  # 人數

# Step 2: Calculate the price of the pig (b)
b = sufficient_amount * a  # 豕價

# Results
a, b
#----- content ends here -----


"""


This code calculates the number of people (`a`) and the price of the pig (`b`) using the method described in the problem. The results are stored in the variables `a` and `b`.
"""


"""
"""
