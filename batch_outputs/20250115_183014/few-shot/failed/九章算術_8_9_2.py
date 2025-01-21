"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money person A (甲) and person B (乙) each have. The problem can be translated into a system of linear equations and solved using the ancient Chinese method of "方程術" (method of solving equations). Here's the solution:

### Problem Breakdown:
1. **Given Conditions:**
   - If A gets half of B's money, A will have 50.
   - If B gets more than half of A's money (太半, meaning \( \frac{3}{2} \) of A's money), B will also have 50.

2. **Equations:**
   Let \( x \) be the amount of money A has, and \( y \) be the amount of money B has.
   - \( x + \frac{1}{2}y = 50 \)  (Equation 1)
   - \( y + \frac{3}{2}x = 50 \)  (Equation 2)

3. **Goal:**
   Solve for \( x \) (A's money) and \( y \) (B's money).

---

### Solution Using 方程術 (Ancient Chinese Method of Elimination):


"""


from fractions import Fraction

# Define the coefficients and constants for the equations
# Equation 1: x + (1/2)y = 50
# Equation 2: y + (3/2)x = 50

# Coefficients for Equation 1
a1 = 1          # Coefficient of x in Equation 1
b1 = Fraction(1, 2)  # Coefficient of y in Equation 1
c1 = 50         # Constant in Equation 1

# Coefficients for Equation 2
a2 = Fraction(3, 2)  # Coefficient of x in Equation 2
b2 = 1          # Coefficient of y in Equation 2
c2 = 50         # Constant in Equation 2

# Step 1: Eliminate one variable (y) by aligning coefficients
# Multiply Equation 1 by 2 to eliminate the fraction
a1 = a1 * 2
b1 = b1 * 2
c1 = c1 * 2

# Now Equation 1 becomes:
# 2x + y = 100

# Step 2: Eliminate y by subtracting Equation 1 from Equation 2
# Multiply Equation 2 by 2 to align coefficients of y
a2 = a2 * 2
b2 = b2 * 2
c2 = c2 * 2

# Now Equation 2 becomes:
# 3x + 2y = 100

# Subtract Equation 1 from Equation 2
# (3x + 2y) - (2x + y) = 100 - 100
x = c2 - c1  # Solve for x
x = Fraction(x)

# Step 3: Substitute x back into one of the original equations to solve for y
# Use Equation 1: 2x + y = 100
y = c1 - (a1 * x)
y = Fraction(y)

# Results
a = x
b = y

# Output the results
a, b


"""


### Explanation of the Code:
1. **Step 1:** The coefficients of \( y \) in both equations are aligned by multiplying through by appropriate factors to eliminate fractions.
2. **Step 2:** The variable \( y \) is eliminated by subtracting one equation from the other, leaving an equation in terms of \( x \) only.
3. **Step 3:** The value of \( x \) is substituted back into one of the original equations to solve for \( y \).

### Final Answer:
- \( a \): The amount of money A has.
- \( b \): The amount of money B has.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 0
Variable 'b' has wrong value. Expected: 25, Actual: 100"""
