"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

"""
This is a classic problem from ancient Chinese mathematics. Let's translate and solve it step by step in Python.

The problem states:

- If each person contributes 100, there is an excess of 100.
- If each person contributes 90, the amount is exactly sufficient.
- We are tasked with finding the number of people (`a`) and the price of the pig (`b`).

The solution involves the following steps:

1. The difference between the two contributions (100 - 90 = 10) is the amount contributed by one person.
2. The total excess (100) and the total shortfall (0 in this case) are used to calculate the number of people.
3. Once the number of people is determined, the total price of the pig can be calculated.

Here is the Python code:


"""


from fractions import Fraction

# Given data
excess = 100  # Excess amount when each person contributes 100
sufficient = 0  # Shortfall when each person contributes 90
rate_difference = 100 - 90  # Difference in contribution per person

# Calculate the number of people (a)
a = Fraction(excess - sufficient, rate_difference)

# Calculate the price of the pig (b)
b = a * 90  # Total price is the number of people times the sufficient contribution per person

# Results
a, b


"""


This code will compute the values of `a` (number of people) and `b` (price of the pig). The results will be stored in the variables `a` and `b`.
"""


"""
"""
