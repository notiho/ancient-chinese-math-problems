"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using a method akin to Gaussian elimination. Let's translate the problem and solution into Python code.

### Problem Restatement:
There are two types of grain, "upper grain" (上禾) and "lower grain" (下禾).  
- 6 bundles of upper grain lose 1 dou and 8 sheng of grain when processed, equivalent to 10 bundles of lower grain.  
- 15 bundles of lower grain lose 5 sheng of grain when processed, equivalent to 5 bundles of upper grain.  

Question: How much grain does 1 bundle of upper grain and 1 bundle of lower grain yield?

### Procedure:
The procedure involves setting up two equations and solving them using elimination:
1. Represent the problem as two equations:
   - \( 6x - 10y = 18 \) (1 dou = 10 sheng, so 1 dou 8 sheng = 18 sheng)
   - \( -5x + 15y = 5 \) (5 sheng remains as is)

2. Solve the equations using elimination:
   - Multiply and eliminate terms to isolate variables.
   - Solve for each variable step by step.

### Python Code Implementation:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 6x - 10y = 18
上禾系數1 = 6
下禾系數1 = -10
常數1 = 18

# Equation 2: -5x + 15y = 5
上禾系數2 = -5
下禾系數2 = 15
常數2 = 5

# Step 1: Eliminate one variable (e.g., 上禾)
# Multiply the first equation by 5 and the second equation by 6 to align 上禾 coefficients
上禾倍數1 = 5
上禾倍數2 = 6

上禾系數1 *= 上禾倍數1
下禾系數1 *= 上禾倍數1
常數1 *= 上禾倍數1

上禾系數2 *= 上禾倍數2
下禾系數2 *= 上禾倍數2
常數2 *= 上禾倍數2

# Subtract the two equations to eliminate 上禾
下禾系數 = 下禾系數1 - 下禾系數2
常數 = 常數1 - 常數2

# Solve for 下禾 (y)
下禾實 = Fraction(常數, 下禾系數)

# Step 2: Solve for 上禾 (x) using one of the original equations
# Substitute 下禾實 into the first equation
常數1 -= 下禾系數1 * 下禾實
上禾實 = Fraction(常數1, 上禾系數1)

# Convert results to sheng
a = 上禾實  # 上禾一秉實
b = 下禾實  # 下禾一秉實

# Output the results
a, b


"""


### Explanation of the Code:
1. The two equations are scaled to align the coefficients of one variable (上禾) for elimination.
2. After eliminating 上禾, the resulting equation is solved for 下禾.
3. The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
4. The results are expressed as fractions to ensure precision.

### Answer:
The yield per bundle is:
- \( a \) sheng for 1 bundle of upper grain.
- \( b \) sheng for 1 bundle of lower grain.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 16/7
Variable 'b' has wrong value. Expected: 3, Actual: -3/7"""
