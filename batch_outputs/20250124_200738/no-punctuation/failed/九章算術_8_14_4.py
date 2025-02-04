"""
今有甲禾二秉乙禾三秉丙禾四秉重皆過於石甲二重如乙一乙三重如丙一丙四重如甲一問甲乙丙禾一秉各重幾何
術曰如方程置重過於石之物為負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲禾一秉重 a石 乙禾一秉重 b石 丙禾一秉重 c石 
"""

"""
This is a classic problem involving a system of linear equations, solved using the ancient Chinese method of elimination (similar to Gaussian elimination). Let's translate the problem and solve it step by step in Python.

### Problem Description:
We are given:
- 2 bundles of Jia grain, 3 bundles of Yi grain, and 4 bundles of Bing grain, all weighing more than 1 shi.
- The relationships between the weights are:
  - 2 bundles of Jia grain weigh the same as 1 bundle of Yi grain.
  - 3 bundles of Yi grain weigh the same as 1 bundle of Bing grain.
  - 4 bundles of Bing grain weigh the same as 1 bundle of Jia grain.

We are tasked to find the weight of 1 bundle of Jia grain, Yi grain, and Bing grain.

### Procedure:
The procedure involves setting up a system of equations, representing the relationships, and solving them using elimination.

### Translation into Python:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the system of equations based on the problem:
# Let x = weight of 1 bundle of Jia grain in shi
# Let y = weight of 1 bundle of Yi grain in shi
# Let z = weight of 1 bundle of Bing grain in shi

# The relationships are:
# 2x = y
# 3y = z
# 4z = x

# Step 2: Express the relationships as equations:
# Equation 1: 2x - y = 0
# Equation 2: 3y - z = 0
# Equation 3: 4z - x = 0

# Step 3: Solve the system of equations using elimination.

# Start with Equation 1: y = 2x
# Substitute y = 2x into Equation 2: 3(2x) - z = 0 -> 6x - z = 0 -> z = 6x
# Substitute z = 6x into Equation 3: 4(6x) - x = 0 -> 24x - x = 0 -> 23x = 0

# Step 4: Normalize the weights (since the system is homogeneous, we can scale the solution).
# Let x = 1 (weight of Jia grain is the base unit).
# Then y = 2x = 2, and z = 6x = 6.

# Step 5: Output the results.
a = Fraction(1)  # Weight of 1 bundle of Jia grain in shi
b = Fraction(2)  # Weight of 1 bundle of Yi grain in shi
c = Fraction(6)  # Weight of 1 bundle of Bing grain in shi

# Final Answer:
print(f"甲禾一秉重 {a} 石")
print(f"乙禾一秉重 {b} 石")
print(f"丙禾一秉重 {c} 石")
#----- content ends here -----


"""


### Explanation of the Solution:
1. The relationships between the weights are expressed as equations.
2. The equations are solved using substitution and elimination.
3. Since the system is homogeneous, the solution is scaled such that the weight of Jia grain (x) is set to 1 shi.
4. The weights of Yi grain (y) and Bing grain (z) are calculated relative to Jia grain.

### Final Answer:
- 甲禾一秉重 1 石
- 乙禾一秉重 2 石
- 丙禾一秉重 6 石
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1
Variable 'b' has wrong value. Expected: 11/23, Actual: 2
Variable 'c' has wrong value. Expected: 10/23, Actual: 6"""
