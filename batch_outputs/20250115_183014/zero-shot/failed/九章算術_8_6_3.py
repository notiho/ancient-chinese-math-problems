"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the value of the unknowns. Here's the Python code:


"""


from fractions import Fraction

# Define the system of equations:
# 5a + 2b = 10
# 2a + 5b = 8

# Solve for a (price of a cow) and b (price of a sheep):
# Using substitution or elimination method.

# Step 1: Multiply the first equation by 5 and the second equation by 2 to align coefficients of b:
# 25a + 10b = 50
# 4a + 10b = 16

# Step 2: Subtract the second equation from the first to eliminate b:
# (25a + 10b) - (4a + 10b) = 50 - 16
# 21a = 34
a = Fraction(34, 21)  # Price of a cow

# Step 3: Substitute a back into the first equation to solve for b:
# 5a + 2b = 10
# 5(Fraction(34, 21)) + 2b = 10
# Fraction(170, 21) + 2b = 10
# 2b = 10 - Fraction(170, 21)
# 2b = Fraction(210, 21) - Fraction(170, 21)
# 2b = Fraction(40, 21)
# b = Fraction(40, 21) / 2
b = Fraction(20, 21)  # Price of a sheep

# Assign the values to the variables:
牛 = a
羊 = b

# Print the results:
print("牛 (price of a cow):", 牛, "兩")
print("羊 (price of a sheep):", 羊, "兩")


"""


### Explanation of the Code:
1. The problem is represented as a system of two linear equations:
   - \( 5a + 2b = 10 \)
   - \( 2a + 5b = 8 \)
2. We solve this system using the elimination method to find the values of \( a \) (price of a cow) and \( b \) (price of a sheep).
3. The `Fraction` class is used to ensure that the results are represented as fractions, as the problem might involve non-integer solutions.
4. The final results are stored in variables `牛` (price of a cow) and `羊` (price of a sheep), and the results are printed.

### Results:
- \( 牛 (price of a cow) = \frac{34}{21} \) 兩
- \( 羊 (price of a sheep) = \frac{20}{21} \) 兩
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 34/21
Variable 'b' has wrong value. Expected: 34/21, Actual: 20/21
Missing variable in output: 'c'
Missing variable in output: 'd'"""
