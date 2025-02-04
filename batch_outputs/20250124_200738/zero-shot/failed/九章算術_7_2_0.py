"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the number of people (`a`) and the price of the item (`b`) based on the given conditions.

### Problem Breakdown:
1. When each person contributes half the price, there is an excess of 4 units.
2. When each person contributes less than half the price, there is a deficit of 3 units.
3. We need to find the number of people (`a`) and the price of the item (`b`).

### Solution:
We will use the method described in the problem to compute the values of `a` and `b`.


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions
excess = 4  # 盈 (excess)
deficit = 3  # 不足 (deficit)

# Step 1: Place the rates of contribution (1/2 and 1/2 - 1/2)
rate1 = Fraction(1, 2)  # Each person contributes half
rate2 = rate1 - Fraction(1, 2)  # Each person contributes less than half

# Step 2: Multiply the rates by the number of people (a) and add excess/deficit
# rate1 * a + excess = b
# rate2 * a - deficit = b

# Step 3: Combine the equations to solve for a and b
# From the equations:
# b = rate1 * a + excess
# b = rate2 * a - deficit
# Equating the two:
# rate1 * a + excess = rate2 * a - deficit
# (rate1 - rate2) * a = deficit + excess

a = (deficit + excess) / (rate1 - rate2)  # Solve for a
b = rate1 * a + excess  # Solve for b

# Convert to integers if possible
a = int(a)
b = int(b)

# Output the results
print("Number of people (a):", a)
print("Price of the item (b):", b)
#----- content ends here -----


"""


### Explanation of the Code:
1. We define the rates of contribution (`rate1` and `rate2`) based on the problem statement.
2. Using the given conditions, we set up two equations for the price of the item (`b`) and solve for the number of people (`a`).
3. Finally, we compute the price of the item (`b`) using one of the equations.

### Output:
The code will compute and display the values of `a` (number of people) and `b` (price of the item).
"""


"""
Variable 'a' has wrong value. Expected: 42, Actual: 14
Variable 'b' has wrong value. Expected: 17, Actual: 11"""
