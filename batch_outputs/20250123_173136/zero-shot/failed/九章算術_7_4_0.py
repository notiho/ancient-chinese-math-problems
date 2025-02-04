"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves finding the number of people (`a`) and the price of gold (`b`) based on the given conditions. Here's the Python code:


"""


from fractions import Fraction

# Given data
rate1 = 400  # Rate per person in the first case
profit1 = 3400  # Profit in the first case
rate2 = 300  # Rate per person in the second case
profit2 = 100  # Profit in the second case

# Step 1: Compute the "實" (numerator)
numerator = (rate1 * profit2) - (rate2 * profit1)

# Step 2: Compute the "法" (denominator)
denominator = (profit2 - profit1)

# Step 3: Compute the number of people (a)
a = Fraction(numerator, denominator)

# Step 4: Compute the price of gold (b)
b = Fraction(profit1, a) + rate1

# Results
a = a  # Number of people
b = b  # Price of gold

# Output the results
a, b


"""


### Explanation:
1. **Given Data**:
   - `rate1` and `rate2` are the amounts contributed by each person in the two cases.
   - `profit1` and `profit2` are the profits in the two cases.

2. **Ancient Method**:
   - The "實" (numerator) is calculated as the difference between the products of the rates and profits.
   - The "法" (denominator) is the difference between the profits.
   - The number of people (`a`) is the fraction of the numerator and denominator.
   - The price of gold (`b`) is calculated using the profit and the number of people.

3. **Output**:
   - The results are stored in variables `a` (number of people) and `b` (price of gold).

You can run this code to compute the values of `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800/33
Variable 'b' has wrong value. Expected: 9800, Actual: 20161/49"""
