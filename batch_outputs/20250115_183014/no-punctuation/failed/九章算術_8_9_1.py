"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰甲持 a錢 乙持 b錢 
"""

"""
This problem involves solving a system of equations based on the given relationships between the amounts of money held by two individuals, A (甲) and B (乙). The procedure described is a traditional Chinese method for solving simultaneous equations, which can be translated into modern algebraic terms.

### Problem:
- A (甲) takes half of B's (乙's) money and has 50 qian.
- B (乙) takes more than half of A's (甲's) money and also has 50 qian.
- Question: How much money do A and B each have?

### Procedure:
The procedure described in the problem is equivalent to solving the system of equations using a traditional method. Let's translate this into Python code.

---


"""


from fractions import Fraction

# Let 甲 (A) have x qian and 乙 (B) have y qian.
# From the problem:
# 1. A takes half of B's money: x + y/2 = 50
# 2. B takes more than half of A's money: y + (3/2)x = 50

# Define the equations:
# Equation 1: x + y/2 = 50
# Equation 2: y + (3/2)x = 50

# Solve for x and y using substitution or elimination.

# Step 1: Rewrite Equation 1 to express y in terms of x.
# y = 2 * (50 - x)
y = lambda x: 2 * (50 - x)

# Step 2: Substitute y into Equation 2.
# y + (3/2)x = 50
# 2 * (50 - x) + (3/2)x = 50
# Simplify:
# 100 - 2x + (3/2)x = 50
# Combine terms:
# 100 - (4/2)x + (3/2)x = 50
# 100 - (1/2)x = 50
# Solve for x:
# (1/2)x = 100 - 50
# (1/2)x = 50
# x = 100

# Step 3: Solve for y using the expression for y.
x = 100
b = y(x)

# Final results:
a = x  # 甲's money
b = b  # 乙's money

# Output the results
a, b


"""


### Explanation:
- The equations are derived directly from the problem statement.
- The solution uses substitution to solve for one variable in terms of the other, then substitutes back to find the second variable.
- The final result gives the amount of money held by A (甲) and B (乙).

### Answer:
甲持 `a = 100` 錢  
乙持 `b = 0` 錢
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
