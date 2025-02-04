"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
To solve this problem using the described "方程術" (method of simultaneous equations), we need to translate the procedure into Python code step by step. Here's how it can be done:


"""

#----- content starts here -----

from fractions import Fraction

# Problem setup
# 上禾六秉正，下禾一十秉負，損實一斗八升正
eq1 = [6, -10, Fraction(1 * 10 + 8, 10)]  # Convert 1斗8升 to 升 (1斗 = 10升)

# 上禾五秉負，下禾一十五秉正，損實五升正
eq2 = [-5, 15, Fraction(5, 1)]  # 5升

# Step 1: Normalize the equations to eliminate one variable
# Multiply eq1 by 5 and eq2 by 6 to align coefficients of 上禾
eq1 = [5 * term for term in eq1]
eq2 = [6 * term for term in eq2]

# Subtract eq2 from eq1 to eliminate 上禾
eq3 = [eq1[i] - eq2[i] for i in range(3)]  # Resulting equation: [0, -60, ...]

# Step 2: Solve for 下禾 (b)
b = Fraction(eq3[2], eq3[1])  # 下禾一秉實

# Step 3: Substitute b back into one of the original equations to solve for 上禾 (a)
a = Fraction(eq1[2] - eq1[1] * b, eq1[0])  # 上禾一秉實

# Results
a = a * 10  # Convert to 升
b = b * 10  # Convert to 升

# Output
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Equation Setup**: The two equations are set up based on the problem description. The units are converted to consistent terms (升).
2. **Normalization**: The coefficients of one variable (上禾) are aligned by multiplying the equations by appropriate factors.
3. **Elimination**: One variable (上禾) is eliminated by subtracting the equations, leaving an equation with only 下禾.
4. **Solve for 下禾**: The resulting equation is solved for 下禾.
5. **Substitute Back**: The value of 下禾 is substituted back into one of the original equations to solve for 上禾.
6. **Convert Units**: The results are converted back to 升 for the final answer.

### Final Answer:
`a` is the amount of 上禾 per 秉 in 升, and `b` is the amount of 下禾 per 秉 in 升.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 11/2
Variable 'b' has wrong value. Expected: 3, Actual: 3/2"""
