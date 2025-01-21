"""
今有上禾三秉益實六斗當下禾十秉下禾五秉益實一斗當上禾二秉問上下禾實一秉各幾何
術曰如方程置上禾三秉正下禾一十秉負益實六斗負次置上禾二秉負下禾五秉正益實一斗負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous linear equations. Here's the solution step by step:

### Problem Restatement:
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾).  
- 3 bundles of upper grain plus an additional 6 dou of grain are equivalent to 10 bundles of lower grain.  
- 5 bundles of lower grain plus an additional 1 dou of grain are equivalent to 2 bundles of upper grain.  

Question: What is the amount of grain (in dou) per bundle for both upper and lower grain?

### Procedure:
The procedure involves setting up the equations and solving them using the method of elimination and substitution, as described in the "fangcheng" method.

### Equations:
1. \( 3 \cdot 上禾 + 6 = 10 \cdot 下禾 \)  
2. \( 2 \cdot 上禾 = 5 \cdot 下禾 + 1 \)

### Solution in Python:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 3 * 上禾 - 10 * 下禾 = -6
上禾1 = 3
下禾1 = -10
實1 = -6

# Equation 2: 2 * 上禾 - 5 * 下禾 = 1
上禾2 = 2
下禾2 = -5
實2 = 1

# Step 1: Eliminate one variable (下禾) by multiplying equations to align coefficients
# Multiply Equation 1 by 5 and Equation 2 by 10 to align 下禾 coefficients
上禾1, 下禾1, 實1 = 5 * 上禾1, 5 * 下禾1, 5 * 實1
上禾2, 下禾2, 實2 = 10 * 上禾2, 10 * 下禾2, 10 * 實2

# New equations:
# 15 * 上禾 - 50 * 下禾 = -30
# 20 * 上禾 - 50 * 下禾 = 10

# Step 2: Subtract the first equation from the second to eliminate 下禾
上禾 = 上禾2 - 上禾1
實 = 實2 - 實1

# Solve for 上禾 (實 / 上禾)
上禾實 = Fraction(實, 上禾)

# Step 3: Substitute 上禾實 back into one of the original equations to solve for 下禾實
# Using Equation 1: 3 * 上禾 - 10 * 下禾 = -6
實 = 3 * 上禾實 - 實1
下禾實 = Fraction(實, -下禾1)

# Results
a = 1  # 上禾秉數
b = 上禾實  # 上禾實
c = 1  # 下禾秉數
d = 下禾實  # 下禾實

# Output results
a, b, c, d


"""


### Explanation of Results:
- \( a \): Number of bundles of upper grain (fixed at 1 bundle).  
- \( b \): Amount of grain (in dou) per bundle of upper grain.  
- \( c \): Number of bundles of lower grain (fixed at 1 bundle).  
- \( d \): Amount of grain (in dou) per bundle of lower grain.  

The solution will provide the values of \( b \) and \( d \) as fractions, representing the amount of grain per bundle for upper and lower grain, respectively.
"""


"""
Variable 'd' has wrong value. Expected: 3, Actual: 27/25"""
