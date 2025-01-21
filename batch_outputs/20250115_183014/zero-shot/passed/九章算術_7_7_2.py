"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
shortfall = 90  # Not enough by 90 when each person pays 5
rate_low = 5    # Rate per person when shortfall occurs
rate_high = 50  # Rate per person when it is just enough

# Step 1: Calculate the number of people (a)
# Difference in rates
rate_difference = rate_high - rate_low

# Number of people (a)
a = Fraction(shortfall, rate_difference)

# Step 2: Calculate the price of the dog (b)
# Price of the dog (b)
b = rate_high * a

# Results
a, b


"""


### Explanation:
1. **Number of people (a):**  
   The difference in rates (`rate_high - rate_low`) is used as the divisor, and the shortfall (`shortfall`) is the dividend. This gives the number of people.

2. **Price of the dog (b):**  
   Once the number of people is determined, the price of the dog is calculated by multiplying the number of people (`a`) by the rate at which the payment is just enough (`rate_high`).

### Output:
The variables `a` (number of people) and `b` (price of the dog) will contain the solutions.
"""


"""
"""
