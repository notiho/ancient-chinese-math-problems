"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
excess = 50  # 人出五十，適足 (sufficient when each person pays 50)
deficit = 5   # 人出五，不足九十 (shortfall of 90 when each person pays 5)
shortfall = 90

# Step 1: Calculate the number of people (a)
a = (excess - deficit) / (shortfall / deficit - shortfall / excess)

# Step 2: Calculate the price of the dog (b)
b = excess * a

# Convert to fractions for exact representation
a = Fraction(a)
b = Fraction(b)

# Results
a, b


"""


This code calculates the number of people (`a`) and the price of the dog (`b`) using the method described in the problem. The results are stored in variables `a` and `b` as fractions for exact representation.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 3127499741229511/1125899906842624
Variable 'b' has wrong value. Expected: 100, Actual: 4886718345671111/35184372088832"""
