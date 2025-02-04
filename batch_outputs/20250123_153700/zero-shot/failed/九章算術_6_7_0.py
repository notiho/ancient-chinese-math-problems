"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a返 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. We'll compute the value of "a" (the number of returns, or "返") using the given relationships.

### Problem Breakdown:
1. The weight of the first basket is 1石17斤 (1石 = 100斤, so 1石17斤 = 117斤).
2. The first basket is carried for 76 steps, with 50 returns.
3. The weight of the second basket is 1石 (100斤).
4. The second basket is carried for 100 steps, and we need to calculate the number of returns (a).

The method described involves:
- Multiplying the steps by the weight of the basket to create a proportional relationship.
- Using the first scenario to determine the proportionality constant.
- Applying that constant to the second scenario to find the number of returns.

### Python Code:

"""


from fractions import Fraction

# Given data
weight1 = 1 * 100 + 17  # 1石17斤 = 117斤
steps1 = 76
returns1 = 50

weight2 = 1 * 100  # 1石 = 100斤
steps2 = 100

# Calculate the proportionality constant
# (steps1 * weight1) / returns1
proportionality_constant = Fraction(steps1 * weight1, returns1)

# Use the proportionality constant to calculate the number of returns for the second basket
# returns2 = (steps2 * weight2) / proportionality_constant
a = Fraction(steps2 * weight2, proportionality_constant)

# The result is stored in variable 'a'


"""


### Explanation:
1. `proportionality_constant` is calculated as `(steps1 * weight1) / returns1`.
2. Using this constant, the number of returns for the second scenario is calculated as `(steps2 * weight2) / proportionality_constant`.

### Final Answer:
The variable `a` will contain the number of returns for the second basket.
"""


"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 125000/2223"""
