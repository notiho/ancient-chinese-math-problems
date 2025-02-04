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
excess = 100  # 盈一百
sufficient = 0  # 適足
shortfall = -100  # 不足一百 (implied by the problem)

rate_high = 100  # 人出一百
rate_low = 90  # 人出九十

# Step 1: Calculate the number of people (a)
# Formula: (excess - shortfall) / (rate_high - rate_low)
a = Fraction(excess - shortfall, rate_high - rate_low)

# Step 2: Calculate the price of the pig (b)
# Formula: sufficient * a
b = rate_high * a

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Number of people (a)**:
   - The difference between the excess and shortfall is divided by the difference in rates (rate_high - rate_low).
   - This gives the number of people.

2. **Price of the pig (b)**:
   - Multiply the number of people (a) by the rate at which the amount is sufficient (rate_high).

### Output:
The variables `a` and `b` will contain the number of people and the price of the pig, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 10, Actual: 20
Variable 'b' has wrong value. Expected: 900, Actual: 2000"""
