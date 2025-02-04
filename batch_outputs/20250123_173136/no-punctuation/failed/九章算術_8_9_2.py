"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲持 a錢 乙持 b錢 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Let's break it down step by step and translate it into Python code.

### Problem Setup:
- Let `甲` have `x` money.
- Let `乙` have `y` money.
- If `甲` takes half of `乙`'s money, he will have 50 coins: `x + y/2 = 50`.
- If `乙` takes more than half of `甲`'s money, he will also have 50 coins: `y + (3/2)x = 50`.

We need to solve for `x` (甲's money) and `y` (乙's money).

### Procedure:
The "fangcheng" method involves setting up a matrix-like structure and performing operations to solve for the unknowns. Here's the Python implementation:


"""


from fractions import Fraction

# Step 1: Define the equations
# Equation 1: x + y/2 = 50
# Equation 2: y + (3/2)x = 50

# Step 2: Convert the equations into a matrix form
# Coefficients of x and y, and the constants on the right-hand side
# [ 1   1/2 | 50 ]
# [ 3/2  1  | 50 ]

# Representing the coefficients and constants
matrix = [
    [Fraction(1), Fraction(1, 2), Fraction(50)],  # Row for equation 1
    [Fraction(3, 2), Fraction(1), Fraction(50)]   # Row for equation 2
]

# Step 3: Eliminate the first variable (x) from the second equation
# Multiply the first row by 3/2 to align with the x coefficient in the second row
factor = Fraction(3, 2)
row1_scaled = [factor * matrix[0][i] for i in range(3)]

# Subtract the scaled first row from the second row
matrix[1] = [matrix[1][i] - row1_scaled[i] for i in range(3)]

# Step 4: Solve for y
# The second row now represents: (1/4)y = 25
y = matrix[1][2] / matrix[1][1]

# Step 5: Solve for x
# Substitute y back into the first equation: x + (1/2)y = 50
x = (matrix[0][2] - (matrix[0][1] * y)) / matrix[0][0]

# Step 6: Output the results
a = x  # 甲's money
b = y  # 乙's money

# Print the results
a, b


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and the columns represent the coefficients of the variables and the constant term.
2. **Elimination**: The first variable (`x`) is eliminated from the second equation by scaling and subtracting rows.
3. **Back Substitution**: Once one variable (`y`) is solved, it is substituted back into the first equation to solve for the other variable (`x`).
4. **Fractions**: The `Fraction` class is used to ensure precise arithmetic with rational numbers.

### Answer:
The values of `a` (甲's money) and `b` (乙's money) are computed and returned.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
