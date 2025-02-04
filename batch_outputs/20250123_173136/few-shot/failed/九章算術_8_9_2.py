"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations to determine how much money person A (甲) and person B (乙) each have. The problem can be solved using a method similar to the ancient Chinese "fangcheng" (方程) or system of equations method. Here's the solution:

### Problem Breakdown:
1. **Given Conditions**:
   - If A gets half of B's money, A will have 50 units of money.
   - If B gets more than half of A's money (太半, meaning 3/2 of half), B will also have 50 units of money.

2. **Equations**:
   Let `甲 = x` (A's money) and `乙 = y` (B's money).
   - From the first condition: \( x + \frac{1}{2}y = 50 \)
   - From the second condition: \( y + \frac{3}{2} \cdot \frac{1}{2}x = 50 \), which simplifies to \( y + \frac{3}{4}x = 50 \).

3. **Solve the System of Equations**:
   Using the ancient "fangcheng" method, we solve the two equations step by step.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Define the equations:
# Equation 1: x + (1/2)y = 50
# Equation 2: y + (3/4)x = 50

# Step 1: Represent coefficients
# Coefficients for Equation 1: x + (1/2)y = 50
a1 = 1
b1 = Fraction(1, 2)
c1 = 50

# Coefficients for Equation 2: (3/4)x + y = 50
a2 = Fraction(3, 4)
b2 = 1
c2 = 50

# Step 2: Eliminate one variable (e.g., y) using the fangcheng method
# Multiply Equation 1 by b2 and Equation 2 by b1 to align the coefficients of y
factor1 = b2
factor2 = b1

# New equations after scaling:
# Equation 1: (b2 * a1)x + (b2 * b1)y = b2 * c1
# Equation 2: (b1 * a2)x + (b1 * b2)y = b1 * c2
new_a1 = factor1 * a1
new_b1 = factor1 * b1
new_c1 = factor1 * c1

new_a2 = factor2 * a2
new_b2 = factor2 * b2
new_c2 = factor2 * c2

# Subtract the two equations to eliminate y
# (new_a1 - new_a2)x = new_c1 - new_c2
final_a = new_a1 - new_a2
final_c = new_c1 - new_c2

# Solve for x (甲's money)
x = final_c / final_a

# Step 3: Substitute x back into one of the original equations to solve for y (乙's money)
# Using Equation 1: x + (1/2)y = 50
y = (c1 - a1 * x) / b1

# Results
a = x  # 甲's money
b = y  # 乙's money

# Output the results
a, b


"""


---

### Explanation of the Code:
1. **Define the Equations**: The two equations are represented with their coefficients.
2. **Eliminate One Variable**: Using the "fangcheng" method, we align the coefficients of `y` in both equations and subtract them to eliminate `y`.
3. **Solve for `x`**: After eliminating `y`, we solve for `x` (A's money).
4. **Substitute Back**: Substitute the value of `x` into one of the original equations to solve for `y` (B's money).

---

### Final Answer:
After running the code:
- \( a = 40 \) (甲持 40 錢)
- \( b = 20 \) (乙持 20 錢)
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
