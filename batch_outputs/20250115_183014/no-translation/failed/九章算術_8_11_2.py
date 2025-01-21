"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem using the described "方程術" (method of equations), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations to determine the pulling capacity of 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse).

---

### Problem Setup:
- 武馬 (strong horse): \( x \) (力引 per horse)
- 中馬 (medium horse): \( y \) (力引 per horse)
- 下馬 (weak horse): \( z \) (力引 per horse)

### Equations:
1. 武馬借中馬一匹: \( x + y = 40 \)
2. 中馬借下馬一匹: \( y + z = 40 \)
3. 下馬借武馬一匹: \( z + x = 40 \)

We will solve this system of equations using the described method.

---

### Python Code:


"""


from fractions import Fraction

# Step 1: Define the equations
# 武馬借中馬一匹: x + y = 40
# 中馬借下馬一匹: y + z = 40
# 下馬借武馬一匹: z + x = 40

# Coefficients of the equations
# Equation 1: x + y = 40
a1, b1, c1, d1 = 1, 1, 0, 40

# Equation 2: y + z = 40
a2, b2, c2, d2 = 0, 1, 1, 40

# Equation 3: z + x = 40
a3, b3, c3, d3 = 1, 0, 1, 40

# Step 2: Eliminate variables using the 方程術
# Multiply equations to align coefficients and eliminate variables step by step

# Eliminate x from Equation 2 and Equation 3
# Multiply Equation 1 by c2 (1) and subtract from Equation 2
# Multiply Equation 1 by c3 (1) and subtract from Equation 3
b2_new = b2 - b1 * a2 / a1
c2_new = c2 - c1 * a2 / a1
d2_new = d2 - d1 * a2 / a1

b3_new = b3 - b1 * a3 / a1
c3_new = c3 - c1 * a3 / a1
d3_new = d3 - d1 * a3 / a1

# Step 3: Solve for z using the simplified equations
z = Fraction(d3_new, c3_new)

# Step 4: Solve for y using the simplified Equation 2
y = Fraction(d2_new - c2_new * z, b2_new)

# Step 5: Solve for x using Equation 1
x = Fraction(d1 - b1 * y, a1)

# Results
a, b = 1, x
c, d = 1, y
e, f = 1, z

# Output the results
a, b, c, d, e, f


"""


---

### Explanation of the Code:
1. **Define the equations**: The coefficients of the equations are set up based on the problem description.
2. **Eliminate variables**: Using the described "方程術," variables are eliminated step by step by aligning coefficients and subtracting equations.
3. **Solve for remaining variables**: After elimination, the remaining variables are solved using substitution and division.
4. **Output the results**: The pulling capacity of each type of horse is calculated and displayed.

---

### Final Answer:
- 武馬 \( a = 1 \), 力引 \( b = x \) 石
- 中馬 \( c = 1 \), 力引 \( d = y \) 石
- 下馬 \( e = 1 \), 力引 \( f = z \) 石
"""


"""
Code error: both arguments should be Rational instances"""
