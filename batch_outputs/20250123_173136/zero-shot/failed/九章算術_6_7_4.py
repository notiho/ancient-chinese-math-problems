"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a返 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the step-by-step solution:

1. The problem describes a relationship between weight, steps, and returns. We are given:
   - First case: weight = 1石17斤, steps = 76, returns = 50.
   - Second case: weight = 1石, steps = 100.
   - We need to calculate the number of returns (`a`) for the second case.

2. The formula provided is:
   \[
   \text{法} = \text{今所行步數} \times \text{今籠重斤數}
   \]
   \[
   \text{實} = \text{故籠重斤數} \times \text{故步數} \times \text{返數}
   \]
   \[
   \text{返數} = \frac{\text{實}}{\text{法}}
   \]

3. Convert the weights into a consistent unit (斤). 1石 = 120斤.

4. Implement the calculation in Python.

Here is the Python code:


"""


from fractions import Fraction

# First case
current_weight = 1 * 120 + 17  # Convert 1石17斤 to 斤
current_steps = 76
current_returns = 50

# Second case
new_weight = 1 * 120  # Convert 1石 to 斤
new_steps = 100

# 法 (denominator)
denominator = current_steps * current_weight

# 實 (numerator)
numerator = current_weight * current_steps * current_returns

# Calculate the number of returns for the second case
a = Fraction(numerator, denominator) * new_steps / new_weight

# Result
a  # The number of returns


"""


The variable `a` will contain the solution in terms of returns.
"""


"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 125/3"""
