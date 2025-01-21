"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰甲持 a錢 乙持 b錢 
"""

"""
This problem involves solving a system of equations based on the given relationships between the amounts of money held by two individuals, A (甲) and B (乙). The solution uses the ancient Chinese "fangcheng" (方程) method, which is an early form of solving linear equations.

### Problem:
甲 (A) receives half of 乙's (B's) money and has 50 coins.  
乙 (B) receives more than half of 甲's (A's) money and also has 50 coins.  
Question: How much money do 甲 (A) and 乙 (B) each have?

### Procedure:
The "fangcheng" (方程) method involves setting up equations and solving them systematically. Here, we interpret the relationships as follows:

1. Let `甲錢 = x` (A's money) and `乙錢 = y` (B's money).
2. From the problem:
   - \( x + \frac{y}{2} = 50 \) (A receives half of B's money and has 50 coins).
   - \( y + \frac{3x}{2} = 50 \) (B receives more than half of A's money and has 50 coins).

We solve these equations step by step using the "fangcheng" method.

---


"""


from fractions import Fraction

# Step 1: Define the equations
# Let x = A's money (甲錢), y = B's money (乙錢)
# Equation 1: x + y/2 = 50
# Equation 2: y + 3x/2 = 50

# Step 2: Eliminate fractions by multiplying through by 2
# Equation 1 becomes: 2x + y = 100
# Equation 2 becomes: 2y + 3x = 100

# Step 3: Solve the system of equations using substitution or elimination
# From Equation 1: y = 100 - 2x
# Substitute y into Equation 2: 2(100 - 2x) + 3x = 100
# Simplify: 200 - 4x + 3x = 100
# Combine like terms: -x = -100
# Solve for x: x = 100

# Step 4: Substitute x back into Equation 1 to find y
# y = 100 - 2x
# y = 100 - 2(100)
# y = 100 - 200
# y = 0

# Final Answer
a = 100  # A's money (甲錢)
b = 0    # B's money (乙錢)

# Output the results
a, b


"""


### Answer:
甲 (A) holds **100 coins**, and 乙 (B) holds **0 coins**.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: 0"""
