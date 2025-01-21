"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of gold (`b`) based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given data
rate1 = 400  # Amount each person contributes in the first case
profit1 = 3400  # Profit in the first case
rate2 = 300  # Amount each person contributes in the second case
profit2 = 100  # Profit in the second case

# Step 1: Compute the "實" (numerator)
numerator = (rate1 * profit2) - (rate2 * profit1)

# Step 2: Compute the "法" (denominator)
denominator = profit2 - profit1

# Step 3: Solve for the number of people (a)
a = Fraction(numerator, denominator)

# Step 4: Solve for the price of gold (b)
b = Fraction(rate1 * a - profit1, a)

# Results
a, b


"""


### Explanation:
1. **Given Data**:
   - `rate1` and `rate2` are the amounts each person contributes in the two cases.
   - `profit1` and `profit2` are the profits in the two cases.

2. **Numerator ("實")**:
   - Multiply the rate of contribution by the profit for each case, then subtract the smaller from the larger.

3. **Denominator ("法")**:
   - Subtract the smaller profit from the larger profit.

4. **Solve for `a` (number of people)**:
   - Divide the numerator by the denominator to find the number of people.

5. **Solve for `b` (price of gold)**:
   - Use the equation for profit to solve for the price of gold.

### Output:
The variables `a` and `b` will contain the solutions:
- `a`: Number of people.
- `b`: Price of gold.
"""


"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800/33
Variable 'b' has wrong value. Expected: 9800, Actual: 19039/49"""
