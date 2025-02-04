"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is equivalent to solving simultaneous equations. Here's how we can translate the procedure into Python code:

### Problem Setup:
We are given two relationships between the quantities of "upper millet" (上禾) and "lower millet" (下禾), and their respective yields in dou (斗). The goal is to find the yield of one秉 (bundle) of upper millet and one秉 of lower millet.

### Equations:
1. \( 3 \cdot 上禾 - 10 \cdot 下禾 = -6 \)
2. \( -2 \cdot 上禾 + 5 \cdot 下禾 = -1 \)

We will solve this system using the described procedure.


"""

#----- content starts here -----

from fractions import Fraction

# Initialize the coefficients and constants for the equations
# Equation 1: 3 * 上禾 - 10 * 下禾 = -6
上禾1 = 3
下禾1 = -10
常數1 = -6

# Equation 2: -2 * 上禾 + 5 * 下禾 = -1
上禾2 = -2
下禾2 = 5
常數2 = -1

# Step 1: Eliminate one variable (下禾) using the first equation
# Multiply the first equation by 5 (coefficient of 下禾 in the second equation)
# Multiply the second equation by 10 (coefficient of 下禾 in the first equation)
上禾1_消 = 上禾1 * 5
下禾1_消 = 下禾1 * 5
常數1_消 = 常數1 * 5

上禾2_消 = 上禾2 * 10
下禾2_消 = 下禾2 * 10
常數2_消 = 常數2 * 10

# Subtract the second equation from the first to eliminate 下禾
上禾_最終 = 上禾1_消 - 上禾2_消
常數_最終 = 常數1_消 - 常數2_消

# Solve for 上禾
上禾_實 = Fraction(常數_最終, 上禾_最終)

# Step 2: Solve for 下禾 using the first equation
# Substitute 上禾_實 into the first equation
常數_代入 = 常數1 - (上禾1 * 上禾_實)
下禾_實 = Fraction(常數_代入, 下禾1)

# Results
a = 上禾_實
b = 下禾_實

# Output the results
print(f"上禾一秉實 {a}斗 ，下禾一秉實 {b}斗 。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equation Setup**: The coefficients of the variables (上禾 and 下禾) and the constants are defined based on the given equations.
2. **Variable Elimination**: We eliminate one variable (下禾) by multiplying the equations to align the coefficients of 下禾 and then subtracting one equation from the other.
3. **Solve for 上禾**: After eliminating 下禾, we solve for 上禾.
4. **Solve for 下禾**: Substitute the value of 上禾 back into one of the original equations to solve for 下禾.
5. **Output**: The results are displayed as fractions to ensure precision.

### Answer:
The output will provide the yield of one秉 of upper millet (上禾) and one秉 of lower millet (下禾) in斗.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: -4/7
Variable 'b' has wrong value. Expected: 3, Actual: 3/7"""
