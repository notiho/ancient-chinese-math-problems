"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of a pig (`b`) based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given data
excess = 100  # 盈一百
sufficient = 0  # 適足
deficit = -100  # 不足一百

rate_high = 100  # 人出一百
rate_low = 90  # 人出九十

# Step 1: Calculate the number of people (a)
real_difference = excess - deficit  # 盈及不足之數為實
rate_difference = rate_high - rate_low  # 以少減多，餘為法
a = Fraction(real_difference, rate_difference)  # 實如法得一人

# Step 2: Calculate the price of a pig (b)
b = rate_high * a  # 以適足乘人數得物價

# Results
a, b


"""


### Explanation:
1. **Real Difference (`盈及不足之數為實`)**: The difference between the excess amount (100) and the deficit amount (-100) is `100 - (-100) = 200`.
2. **Rate Difference (`以少減多，餘為法`)**: The difference between the two rates (100 and 90) is `100 - 90 = 10`.
3. **Number of People (`a`)**: The number of people is calculated as the ratio of the real difference to the rate difference: `a = 200 / 10 = 20`.
4. **Price of a Pig (`b`)**: The price of a pig is calculated by multiplying the rate (100) by the number of people (`a`): `b = 100 * 20 = 2000`.

### Final Values:
- `a = 20` (Number of people)
- `b = 2000` (Price of a pig)
"""


"""
Variable 'a' has wrong value. Expected: 10, Actual: 20
Variable 'b' has wrong value. Expected: 900, Actual: 2000"""
