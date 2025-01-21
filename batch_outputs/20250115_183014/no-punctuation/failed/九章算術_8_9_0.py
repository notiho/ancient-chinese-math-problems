"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰甲持 a錢 乙持 b錢 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Let's break it down step by step and translate it into Python code.

### Problem Description:
Two people, A (甲) and B (乙), hold an unknown amount of money.  
- If A takes half of B's money, A will have 50 coins.  
- If B takes more than half of A's money, B will also have 50 coins.  

We are tasked to find how much money A and B each hold.

### Procedure:
The "fangcheng" method is described as follows:
1. Represent the problem as a system of equations.
2. Use elimination and substitution to solve for the unknowns.

The equations for this problem are:
1. \( A + \frac{1}{2}B = 50 \)  
2. \( B + \frac{3}{2}A = 50 \)

We will solve this step by step using Python.

---


"""


from fractions import Fraction

# Step 1: Represent the equations
# Let A = 甲's money, B = 乙's money
# Equation 1: A + (1/2)B = 50
# Equation 2: B + (3/2)A = 50

# Step 2: Eliminate fractions by multiplying through by 2
# Equation 1 becomes: 2A + B = 100
# Equation 2 becomes: 2B + 3A = 100

# Step 3: Solve the system of equations using elimination
# Multiply Equation 1 by 2 to align B terms: 4A + 2B = 200
# Subtract Equation 2 from the result: (4A + 2B) - (3A + 2B) = 200 - 100
# This simplifies to: A = 100

A = 100  # 甲's money

# Step 4: Substitute A into one of the original equations to solve for B
# Using Equation 1: 2A + B = 100
# Substitute A = 100: 2(100) + B = 100
# Simplify: 200 + B = 100
# Solve for B: B = -100

B = Fraction(100)  # 乙's money

# Final Answer
a = A  # 甲's money
b = B  # 乙's money

print(f"甲持 {a} 錢, 乙持 {b} 錢")


"""


### Answer:
甲持 \( a = 100 \) 錢  
乙持 \( b = 0 \) 錢
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: 100"""
