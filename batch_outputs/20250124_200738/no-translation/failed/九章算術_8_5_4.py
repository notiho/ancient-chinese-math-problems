"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to find the "實" (value per 秉) for both 上禾 and 下禾.

The equations are:
1. \( 3 \times 上禾 - 10 \times 下禾 = -6 \)
2. \( -2 \times 上禾 + 5 \times 下禾 = -1 \)

We will solve this system using the described method.


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients and constants from the equations
# Equation 1: 3 * 上禾 - 10 * 下禾 = -6
上禾1 = 3
下禾1 = -10
實1 = -6

# Equation 2: -2 * 上禾 + 5 * 下禾 = -1
上禾2 = -2
下禾2 = 5
實2 = -1

# Step 1: Eliminate 上禾 by multiplying rows and subtracting
# Multiply the first equation by 2 and the second equation by 3
上禾法 = 上禾1 * 2 - 上禾2 * 3  # This will be 0
下禾法 = 下禾1 * 2 - 下禾2 * 3
實法 = 實1 * 2 - 實2 * 3

# Step 2: Solve for 下禾
b = Fraction(實法, 下禾法)

# Step 3: Substitute 下禾 into one of the original equations to solve for 上禾
a = Fraction(實1 - 下禾1 * b, 上禾1)

# Results
print(f"上禾一秉實 a斗 = {a}斗")
print(f"下禾一秉實 b斗 = {b}斗")
#----- content ends here -----


"""


### Explanation of the Code:
1. The equations are set up based on the problem statement.
2. The elimination method is used to remove one variable (上禾) and solve for the other (下禾).
3. Once 下禾 is found, it is substituted back into one of the original equations to solve for 上禾.
4. The results are expressed as fractions to maintain precision, as required by the problem.

### Final Answer:
- \( a \): The value of 上禾 per 秉 in 斗.
- \( b \): The value of 下禾 per 秉 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: -8/7
Variable 'b' has wrong value. Expected: 3, Actual: 9/35"""
