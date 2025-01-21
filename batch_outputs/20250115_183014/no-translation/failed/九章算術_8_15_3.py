"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
To solve this problem using the described "方程術" (method of solving simultaneous equations), we will translate the problem into Python code step by step. The problem involves three equations with three unknowns, which can be solved using elimination and substitution.

The equations are:
1. \( x + 5y + 10z = 10 \)  (where \( x \), \( y \), and \( z \) are the chicken consumption rates of 令, 吏, and 從者 respectively)
2. \( 10x + y + 5z = 8 \)
3. \( 5x + 10y + z = 6 \)

Let's implement the solution:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: x + 5y + 10z = 10
a1, b1, c1, d1 = 1, 5, 10, 10

# Equation 2: 10x + y + 5z = 8
a2, b2, c2, d2 = 10, 1, 5, 8

# Equation 3: 5x + 10y + z = 6
a3, b3, c3, d3 = 5, 10, 1, 6

# Step 1: Eliminate x from equations 2 and 3 using equation 1
# Multiply equation 1 by 10 and subtract from equation 2
factor1 = a2 / a1
b2_new = b2 - factor1 * b1
c2_new = c2 - factor1 * c1
d2_new = d2 - factor1 * d1

# Multiply equation 1 by 5 and subtract from equation 3
factor2 = a3 / a1
b3_new = b3 - factor2 * b1
c3_new = c3 - factor2 * c1
d3_new = d3 - factor2 * d1

# Step 2: Eliminate y from equation 3 using the new equation 2
factor3 = b3_new / b2_new
c3_final = c3_new - factor3 * c2_new
d3_final = d3_new - factor3 * d2_new

# Step 3: Solve for z
z = Fraction(d3_final, c3_final)

# Step 4: Solve for y using the new equation 2
y = Fraction(d2_new - c2_new * z, b2_new)

# Step 5: Solve for x using equation 1
x = Fraction(d1 - b1 * y - c1 * z, a1)

# Results
a, b = 1, x  # 令
c, d = 5, y  # 吏
e, f = 10, z  # 從者

# Output results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Step 1**: Eliminate \( x \) from equations 2 and 3 by subtracting appropriate multiples of equation 1.
2. **Step 2**: Eliminate \( y \) from the modified equation 3 using the modified equation 2.
3. **Step 3**: Solve for \( z \) from the final equation.
4. **Step 4**: Back-substitute \( z \) into the modified equation 2 to solve for \( y \).
5. **Step 5**: Back-substitute \( y \) and \( z \) into equation 1 to solve for \( x \).

### Final Answer:
- \( a = 1 \), \( b = x \) (令食 \( x \) 雞)
- \( c = 5 \), \( d = y \) (吏食 \( y \) 雞)
- \( e = 10 \), \( f = z \) (從者食 \( z \) 雞)
"""


"""
Code error: both arguments should be Rational instances"""
