"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Let's break it down step by step and translate it into Python code.

### Problem Description
- **Given:**
  - 6 bundles of upper millet (上禾) lose 1 dou and 8 sheng (1 dou = 10 sheng) when compared to 10 bundles of lower millet (下禾).
  - 15 bundles of lower millet lose 5 sheng when compared to 5 bundles of upper millet.
- **Question:**
  - What is the yield of 1 bundle of upper millet (上禾) and 1 bundle of lower millet (下禾)?

### Procedure
1. Represent the problem as two linear equations:
   - \( 6x - 10y = 1 \text{ dou } 8 \text{ sheng } = 18 \text{ sheng} \)
   - \( -5x + 15y = 5 \text{ sheng} \)
   Here, \(x\) is the yield of 1 bundle of upper millet (in sheng), and \(y\) is the yield of 1 bundle of lower millet (in sheng).

2. Solve the equations using the fangcheng method:
   - Eliminate one variable by multiplying and subtracting the equations.
   - Solve for the remaining variable.
   - Back-substitute to find the other variable.

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 6x - 10y = 18
a1, b1, c1 = 6, -10, 18

# Equation 2: -5x + 15y = 5
a2, b2, c2 = -5, 15, 5

# Step 1: Eliminate one variable (e.g., x) by multiplying and subtracting equations
# Multiply equation 1 by 5 and equation 2 by 6 to align coefficients of x
a1, b1, c1 = 5 * a1, 5 * b1, 5 * c1
a2, b2, c2 = 6 * a2, 6 * b2, 6 * c2

# Subtract the equations to eliminate x
# (5 * eq1) - (6 * eq2)
b = b1 - b2  # Coefficient of y
c = c1 - c2  # Constant term
# Resulting equation: by = c
y = Fraction(c, b)  # Solve for y (yield of 1 bundle of lower millet)

# Step 2: Back-substitute to find x (yield of 1 bundle of upper millet)
# Use equation 1: 6x - 10y = 18
x = Fraction(c1 - b1 * y, a1)  # Solve for x

# Convert results to sheng
a = x  # Yield of 1 bundle of upper millet (in sheng)
b = y  # Yield of 1 bundle of lower millet (in sheng)

# Output the results
print(f"上禾一秉實 {a} 升")
print(f"下禾一秉實 {b} 升")
#----- content ends here -----


"""


### Explanation of the Code
1. **Input the coefficients** of the two equations.
2. **Eliminate one variable** by aligning the coefficients of \(x\) and subtracting the equations.
3. **Solve for the remaining variable** (\(y\)).
4. **Back-substitute** \(y\) into one of the original equations to solve for \(x\).
5. **Output the results** as the yield of 1 bundle of upper millet (\(x\)) and 1 bundle of lower millet (\(y\)).

### Final Answer
The Python code will compute:
- \(a\): Yield of 1 bundle of upper millet (in sheng).
- \(b\): Yield of 1 bundle of lower millet (in sheng).
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 16/7
Variable 'b' has wrong value. Expected: 3, Actual: -3/7"""
