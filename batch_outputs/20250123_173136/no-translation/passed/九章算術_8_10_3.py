"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve this problem using the described "方程術" (method of solving simultaneous equations), we first need to translate the problem into equations and then solve them step by step. Here's the Python implementation:


"""


from fractions import Fraction

# Problem setup:
# Let 馬價 = x (price of one horse)
# Let 牛價 = y (price of one cow)

# Equations derived from the problem:
# 2x + y = 10000 + x/2  (Equation 1)
# x + 2y = 10000 - y/2  (Equation 2)

# Simplify Equation 1:
# Multiply through by 2 to eliminate the fraction:
# 4x + 2y = 20000 + x
# 3x + 2y = 20000  (Simplified Equation 1)

# Simplify Equation 2:
# Multiply through by 2 to eliminate the fraction:
# 2x + 4y = 20000 - y
# 2x + 5y = 20000  (Simplified Equation 2)

# Solve the system of equations using the described method:

# Step 1: Represent the equations in matrix form:
# 3x + 2y = 20000
# 2x + 5y = 20000

# Coefficients of the equations:
A = [
    [3, 2],  # Coefficients of x and y in the first equation
    [2, 5]   # Coefficients of x and y in the second equation
]

# Constants on the right-hand side of the equations:
B = [20000, 20000]

# Step 2: Eliminate one variable (e.g., x) using the described method:
# Multiply the first equation by 2 and the second equation by 3:
# 6x + 4y = 40000  (First equation multiplied by 2)
# 6x + 15y = 60000 (Second equation multiplied by 3)

# Subtract the first equation from the second:
# (6x + 15y) - (6x + 4y) = 60000 - 40000
# 11y = 20000
y = Fraction(20000, 11)  # Solve for y (牛價)

# Step 3: Substitute y back into one of the original equations to solve for x:
# Use the first simplified equation: 3x + 2y = 20000
x = Fraction(20000 - 2 * y, 3)  # Solve for x (馬價)

# Final results:
a = x  # 馬價
b = y  # 牛價

# Output the results:
a, b


"""


### Explanation of the Code:
1. **Equation Setup**: The problem is translated into two equations based on the conditions provided.
2. **Simplification**: The equations are simplified to remove fractions.
3. **Elimination Method**: The described "方程術" is essentially the elimination method for solving simultaneous equations. One variable is eliminated by scaling and subtracting the equations.
4. **Substitution**: The value of one variable is substituted back into one of the original equations to solve for the other variable.
5. **Fraction Representation**: The `Fraction` class is used to ensure exact arithmetic without floating-point errors.

### Final Answer:
The values of `a` (馬價) and `b` (牛價) are the solutions to the problem.
"""


"""
"""
