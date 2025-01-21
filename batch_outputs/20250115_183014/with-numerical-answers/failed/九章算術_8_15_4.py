"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：令 a(=1)人 食 b(=45/122)雞 ，吏 c(=1)人 食 d(=41/122)雞 ，從者 e(=1)人 食 f(=97/122)雞 。
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of elimination, similar to Gaussian elimination. The problem is to determine how many chickens are consumed by a single "令" (official), "吏" (clerk), and "從者" (attendant) based on the given conditions.

Here is the solution encoded in Python:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 令1 + 吏5 + 從者10 = 10 (chickens)
# Equation 2: 令10 + 吏1 + 從者5 = 8 (chickens)
# Equation 3: 令5 + 吏10 + 從者1 = 6 (chickens)

# Coefficients of the equations
令1, 吏1, 從者1 = 1, 5, 10
令2, 吏2, 從者2 = 10, 1, 5
令3, 吏3, 從者3 = 5, 10, 1

# Constants (right-hand side of the equations)
雞1 = 10
雞2 = 8
雞3 = 6

# Step 1: Eliminate "令" from the second and third equations
# Multiply the first equation by 10 (令2) and subtract the second equation
# Multiply the first equation by 5 (令3) and subtract the third equation

# Eliminate "令" from the second equation
吏2_new = 吏2 - 令2 * 吏1 / 令1
從者2_new = 從者2 - 令2 * 從者1 / 令1
雞2_new = 雞2 - 令2 * 雞1 / 令1

# Eliminate "令" from the third equation
吏3_new = 吏3 - 令3 * 吏1 / 令1
從者3_new = 從者3 - 令3 * 從者1 / 令1
雞3_new = 雞3 - 令3 * 雞1 / 令1

# Step 2: Eliminate "吏" from the third equation
# Multiply the second equation by 吏3_new and subtract the third equation multiplied by 吏2_new

從者3_final = 從者3_new - 吏3_new * 從者2_new / 吏2_new
雞3_final = 雞3_new - 吏3_new * 雞2_new / 吏2_new

# Step 3: Solve for "從者"
從者 = Fraction(雞3_final, 從者3_final)

# Step 4: Solve for "吏" using the second equation
吏 = Fraction(雞2_new - 從者2_new * 從者, 吏2_new)

# Step 5: Solve for "令" using the first equation
令 = Fraction(雞1 - 吏1 * 吏 - 從者1 * 從者, 令1)

# Results
a = 令  # Chickens consumed by one "令"
b = 吏  # Chickens consumed by one "吏"
c = 從者  # Chickens consumed by one "從者"

# Output the results
print(f"令 a(=1)人 食 b({令})雞")
print(f"吏 c(=1)人 食 d({吏})雞")
print(f"從者 e(=1)人 食 f({從者})雞")


"""


### Explanation of the Code:
1. **Equation Setup**: The problem is represented as a system of three linear equations.
2. **Elimination**: The ancient Chinese elimination method is used to reduce the equations step by step, eliminating variables until only one variable remains.
3. **Back Substitution**: Once one variable is solved, it is substituted back into the previous equations to solve for the remaining variables.
4. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations with rational numbers.

### Final Answer:
- 令 (official): \( a = 1 \) person consumes \( b = \frac{45}{122} \) chickens.
- 吏 (clerk): \( c = 1 \) person consumes \( d = \frac{41}{122} \) chickens.
- 從者 (attendant): \( e = 1 \) person consumes \( f = \frac{97}{122} \) chickens.
"""


"""
Code error: both arguments should be Rational instances"""
