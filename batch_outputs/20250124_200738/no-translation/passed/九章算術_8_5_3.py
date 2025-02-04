"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will translate the procedure into Python code step by step. This involves solving a system of linear equations using the described elimination method.

The equations derived from the problem are:
1. \( 3x - 10y = -6 \)  
2. \( -2x + 5y = -1 \)

Where \( x \) is the amount of grain in one秉 of 上禾, and \( y \) is the amount of grain in one秉 of 下禾.

Here is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 3x - 10y = -6
a1, b1, c1 = 3, -10, -6

# Equation 2: -2x + 5y = -1
a2, b2, c2 = -2, 5, -1

# Step 1: Eliminate x by multiplying the equations and subtracting
# Multiply equation 1 by 2 and equation 2 by 3 to align coefficients of x
a1, b1, c1 = 2 * a1, 2 * b1, 2 * c1  # 6x - 20y = -12
a2, b2, c2 = 3 * a2, 3 * b2, 3 * c2  # -6x + 15y = -3

# Add the two equations to eliminate x
# (-20y + 15y = -12 - 3)
y = Fraction(c1 + c2, b1 + b2)

# Step 2: Solve for x using one of the original equations
# Substitute y into equation 1: 3x - 10y = -6
x = Fraction(c1 - b1 * y, a1)

# Results
a = x  # 上禾一秉實
b = y  # 下禾一秉實

# Output
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equation Setup**: The coefficients of the two equations are set up based on the problem statement.
2. **Elimination of \( x \)**: The equations are manipulated to eliminate \( x \) by aligning their coefficients and adding them.
3. **Solve for \( y \)**: After eliminating \( x \), \( y \) is solved.
4. **Back-substitution for \( x \)**: Using the value of \( y \), \( x \) is calculated from one of the original equations.
5. **Output**: The values of \( x \) (上禾一秉實) and \( y \) (下禾一秉實) are returned.

### Final Answer:
The values of \( a \) (上禾一秉實) and \( b \) (下禾一秉實) are expressed in terms of fractions (斗).
"""


"""
"""
