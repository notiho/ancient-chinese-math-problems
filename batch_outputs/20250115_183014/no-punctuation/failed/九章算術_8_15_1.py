"""
今有令一人吏五人從者一十人食雞一十令一十人吏一人從者五人食雞八令五人吏一十人從者一人食雞六問令吏從者食雞各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰令 a人 食 b雞 吏 c人 食 d雞 從者 e人 食 f雞 
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous linear equations. The problem describes three scenarios with different groups of people (leaders, officials, and followers) consuming chickens, and we are tasked with finding how many chickens each type of person consumes.

The equations based on the problem are as follows:
1. \( 1 \cdot x + 5 \cdot y + 10 \cdot z = 10 \) (leaders, officials, followers consuming 10 chickens)
2. \( 10 \cdot x + 1 \cdot y + 5 \cdot z = 8 \) (leaders, officials, followers consuming 8 chickens)
3. \( 5 \cdot x + 10 \cdot y + 1 \cdot z = 6 \) (leaders, officials, followers consuming 6 chickens)

Here, \( x \), \( y \), and \( z \) represent the number of chickens consumed by one leader, one official, and one follower, respectively.

The procedure for solving this system of equations using the "fangcheng" method is described step by step below:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 1x + 5y + 10z = 10
# Equation 2: 10x + 1y + 5z = 8
# Equation 3: 5x + 10y + 1z = 6

# Step 1: Represent the equations as a matrix
# Each row corresponds to an equation: [x coefficient, y coefficient, z coefficient, constant term]
matrix = [
    [1, 5, 10, 10],  # Equation 1
    [10, 1, 5, 8],   # Equation 2
    [5, 10, 1, 6]    # Equation 3
]

# Step 2: Eliminate the first variable (x) from the second and third equations
# Multiply the first row by 10 (to match the x coefficient in the second row) and subtract
factor = matrix[1][0] / matrix[0][0]
for i in range(4):
    matrix[1][i] -= factor * matrix[0][i]

# Multiply the first row by 5 (to match the x coefficient in the third row) and subtract
factor = matrix[2][0] / matrix[0][0]
for i in range(4):
    matrix[2][i] -= factor * matrix[0][i]

# Step 3: Eliminate the second variable (y) from the third equation
# Multiply the second row by the appropriate factor and subtract
factor = matrix[2][1] / matrix[1][1]
for i in range(4):
    matrix[2][i] -= factor * matrix[1][i]

# Step 4: Solve for z (the third variable)
z = Fraction(matrix[2][3], matrix[2][2])

# Step 5: Solve for y (the second variable) using the second equation
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])

# Step 6: Solve for x (the first variable) using the first equation
x = Fraction(matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z, matrix[0][0])

# Results
a = 1  # Number of leaders
b = x  # Chickens consumed by one leader
c = 5  # Number of officials
d = y  # Chickens consumed by one official
e = 10  # Number of followers
f = z  # Chickens consumed by one follower

# Output the results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix, where each row corresponds to an equation, and the last column contains the constant terms.
2. **Elimination**: The "fangcheng" method eliminates variables step by step by subtracting scaled versions of one row from another.
3. **Back Substitution**: After eliminating variables, the remaining equations are solved in reverse order (starting from the last variable).
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Final Answer:
The values of \( a \), \( b \), \( c \), \( d \), \( e \), and \( f \) represent the number of leaders, chickens consumed by one leader, number of officials, chickens consumed by one official, number of followers, and chickens consumed by one follower, respectively.
"""


"""
Code error: both arguments should be Rational instances"""
