"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem using the described "方程術" (method of equations), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to determine the pulling strength of 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse).

### Problem setup:
Let:
- `a` = pulling strength of 武馬 (strong horse) in 石
- `b` = pulling strength of 中馬 (medium horse) in 石
- `c` = pulling strength of 下馬 (weak horse) in 石

The equations are derived from the borrowing and lending of strength:
1. 武馬借中馬一匹: 武馬's total strength becomes `a + b`, which is sufficient to pull 40 石.
   - Equation: `a + b = 40`
2. 中馬借下馬一匹: 中馬's total strength becomes `b + c`, which is sufficient to pull 40 石.
   - Equation: `b + c = 40`
3. 下馬借武馬一匹: 下馬's total strength becomes `c + a`, which is sufficient to pull 40 石.
   - Equation: `c + a = 40`

We now solve this system of equations using the described method.

---

### Python Code:


"""


from fractions import Fraction

# Step 1: Define the equations
# a + b = 40
# b + c = 40
# c + a = 40

# Step 2: Express the equations in terms of a matrix
# Coefficients of the variables (武馬, 中馬, 下馬)
# [ 1  1  0 ] [a]   [40]
# [ 0  1  1 ] [b] = [40]
# [ 1  0  1 ] [c]   [40]

# Step 3: Solve using elimination (方程術)
# Start with the matrix:
# | 1  1  0 | 40 |
# | 0  1  1 | 40 |
# | 1  0  1 | 40 |

# Eliminate the first variable (a) from the second and third rows
# Multiply the first row by -1 and add to the third row
# Row 3: (1 0 1 | 40) - (1 1 0 | 40) -> (0 -1 1 | 0)
# New matrix:
# | 1  1  0 | 40 |
# | 0  1  1 | 40 |
# | 0 -1  1 |  0 |

# Eliminate the second variable (b) from the third row
# Multiply the second row by 1 and add to the third row
# Row 3: (0 -1 1 | 0) + (0 1 1 | 40) -> (0 0 2 | 40)
# New matrix:
# | 1  1  0 | 40 |
# | 0  1  1 | 40 |
# | 0  0  2 | 40 |

# Solve for c (下馬's strength)
c = Fraction(40, 2)

# Back-substitute to solve for b (中馬's strength)
b = 40 - c

# Back-substitute to solve for a (武馬's strength)
a = 40 - b

# Results
a = float(a)
b = float(b)
c = float(c)


"""


### Explanation of Results:
- `a` = 武馬's pulling strength in 石
- `b` = 中馬's pulling strength in 石
- `c` = 下馬's pulling strength in 石

### Final Answer:
武馬一匹力引 `a` 石，中馬一匹力引 `b` 石，下馬一匹力引 `c` 石.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20.0
Variable 'b' has wrong value. Expected: 120/7, Actual: 20.0
Variable 'c' has wrong value. Expected: 40/7, Actual: 20.0"""
