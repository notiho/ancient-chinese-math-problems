"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a(=45/122)雞 ，吏一人食 b(=41/122)雞 ，從者一人食 c(=97/122)雞 。
"""

"""
This problem is a classic example of solving a system of linear equations, which is described in ancient Chinese mathematics as the "fangcheng" (方程) method. The problem involves determining how many chickens are consumed by a single official (令), a single clerk (吏), and a single attendant (從者), based on three given scenarios.

We will translate the problem into Python code and solve it step by step using the described procedure.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem description:
# 令 + 5吏 + 10從者 = 10
# 10令 + 吏 + 5從者 = 8
# 5令 + 10吏 + 從者 = 6

# Coefficients of the equations
A = [
    [1, 5, 10],  # Coefficients for the first equation
    [10, 1, 5],  # Coefficients for the second equation
    [5, 10, 1]   # Coefficients for the third equation
]

# Constants on the right-hand side of the equations
B = [10, 8, 6]

# Step 1: Normalize the first row
factor = A[0][0]
A[0] = [Fraction(x, factor) for x in A[0]]
B[0] = Fraction(B[0], factor)

# Step 2: Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = A[i][0]
    A[i] = [A[i][j] - factor * A[0][j] for j in range(3)]
    B[i] = B[i] - factor * B[0]

# Step 3: Normalize the second row
factor = A[1][1]
A[1] = [Fraction(x, factor) for x in A[1]]
B[1] = Fraction(B[1], factor)

# Step 4: Eliminate the second variable from the third row
factor = A[2][1]
A[2] = [A[2][j] - factor * A[1][j] for j in range(3)]
B[2] = B[2] - factor * B[1]

# Step 5: Solve for the third variable
c = Fraction(B[2], A[2][2])

# Step 6: Solve for the second variable
b = B[1] - A[1][2] * c

# Step 7: Solve for the first variable
a = B[0] - A[0][1] * b - A[0][2] * c

# Results
a = Fraction(a)  # 令一人食雞數
b = Fraction(b)  # 吏一人食雞數
c = Fraction(c)  # 從者一人食雞數

# Output the results
print(f"令一人食 {a} 雞")
print(f"吏一人食 {b} 雞")
print(f"從者一人食 {c} 雞")
#----- content ends here -----


"""


### Explanation of the Code
1. **Define the equations**: The coefficients of the variables (令, 吏, 從者) and the constants on the right-hand side are defined based on the problem description.
2. **Normalize rows**: Each row is normalized by dividing through by the leading coefficient to simplify calculations.
3. **Eliminate variables**: Using the elimination method, variables are systematically removed from subsequent rows.
4. **Back-substitution**: Once the system is in triangular form, the variables are solved starting from the last row and substituting back into previous rows.
5. **Results**: The solution gives the number of chickens consumed by each individual.

### Final Answer
- 令一人食 \( a = \frac{45}{122} \) 雞
- 吏一人食 \( b = \frac{41}{122} \) 雞
- 從者一人食 \( c = \frac{97}{122} \) 雞
"""


"""
"""
