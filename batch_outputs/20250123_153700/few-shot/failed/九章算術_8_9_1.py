"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations based on the given relationships between the amounts of money held by two individuals, A (甲) and B (乙). The solution can be derived using the principles of ancient Chinese "fangcheng" (方程), which is an early method for solving simultaneous linear equations.

### Problem Breakdown:
1. **Given Conditions:**
   - If A (甲) takes half of B's (乙) money, A will have 50 units of money.
   - If B (乙) takes more than half of A's (甲) money (specifically, \( \frac{3}{2} \) of half of A's money), B will also have 50 units of money.

2. **Objective:**
   - Determine how much money A (甲) and B (乙) each originally had.

3. **Procedure:**
   - Translate the relationships into equations.
   - Solve the equations using the "fangcheng" method.

---

### Solution in Python Code:


"""


from fractions import Fraction

# Let 甲持錢 = x (money A has)
# Let 乙持錢 = y (money B has)

# Translate the problem into equations:
# Equation 1: x + (1/2)y = 50
# Equation 2: y + (3/2)(1/2)x = 50

# Rewrite the equations for clarity:
# Equation 1: x + (1/2)y = 50
# Equation 2: y + (3/4)x = 50

# Step 1: Express y in terms of x using Equation 1
# y = 2 * (50 - x)

# Step 2: Substitute y into Equation 2
# 2 * (50 - x) + (3/4)x = 50

# Solve for x:
# Expand: 100 - 2x + (3/4)x = 50
# Combine terms: 100 - 50 = 2x - (3/4)x
# 50 = (8/4)x - (3/4)x
# 50 = (5/4)x
# x = 50 * (4/5)

# Calculate x (甲持錢):
x = Fraction(50) * Fraction(4, 5)

# Step 3: Substitute x back into Equation 1 to find y:
# y = 2 * (50 - x)
y = 2 * (50 - x)

# Results:
a = x  # 甲持錢
b = y  # 乙持錢

# Output the results
a, b


"""


---

### Explanation of the Code:
1. **Equations Setup:**
   - The problem is translated into two linear equations based on the relationships provided.
   - Equation 1: \( x + \frac{1}{2}y = 50 \)
   - Equation 2: \( y + \frac{3}{4}x = 50 \)

2. **Substitution:**
   - Solve Equation 1 for \( y \) in terms of \( x \), then substitute into Equation 2.

3. **Simplification:**
   - Solve for \( x \) (A's money) and then use it to calculate \( y \) (B's money).

4. **Results:**
   - The values of \( x \) and \( y \) are stored in variables `a` and `b`, representing the amounts of money held by A and B, respectively.

---

### Final Answer:
- \( a = 40 \) (甲持錢 = 40 units)
- \( b = 20 \) (乙持錢 = 20 units)
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 40
Variable 'b' has wrong value. Expected: 25, Actual: 20"""
