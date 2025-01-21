"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
To solve this problem, we need to translate the ancient Chinese method of solving simultaneous linear equations (方程術) into Python code. The problem involves three equations with three unknowns (牛價, 羊價, 豕價). Here's the step-by-step solution:


"""


from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 2牛 + 5羊 - 13豕 = 1000
# Equation 2: 3牛 - 9羊 + 3豕 = 0
# Equation 3: -5牛 + 6羊 + 8豕 = -600
coefficients = [
    [2, 5, -13, 1000],  # First equation
    [3, -9, 3, 0],      # Second equation
    [-5, 6, 8, -600]    # Third equation
]

# Step 1: Normalize the first row (make the first coefficient 1)
for i in range(4):
    coefficients[0][i] = Fraction(coefficients[0][i], coefficients[0][0])

# Step 2: Eliminate the first variable from the second and third rows
for i in range(1, 3):
    factor = coefficients[i][0]
    for j in range(4):
        coefficients[i][j] -= factor * coefficients[0][j]

# Step 3: Normalize the second row (make the second coefficient 1)
for i in range(1, 4):
    coefficients[1][i] = Fraction(coefficients[1][i], coefficients[1][1])

# Step 4: Eliminate the second variable from the third row
factor = coefficients[2][1]
for i in range(1, 4):
    coefficients[2][i] -= factor * coefficients[1][i]

# Step 5: Solve for the third variable (豕價)
c = Fraction(coefficients[2][3], coefficients[2][2])

# Step 6: Solve for the second variable (羊價)
b = coefficients[1][3] - coefficients[1][2] * c

# Step 7: Solve for the first variable (牛價)
a = coefficients[0][3] - coefficients[0][2] * c - coefficients[0][1] * b

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Normalize the first row**: Divide the first row by the first coefficient to make it 1.
2. **Eliminate the first variable**: Subtract multiples of the first row from the second and third rows to eliminate the first variable from those rows.
3. **Normalize the second row**: Divide the second row by its second coefficient to make it 1.
4. **Eliminate the second variable**: Subtract a multiple of the second row from the third row to eliminate the second variable.
5. **Back-substitution**: Solve for the third variable (豕價), then substitute back to find the second variable (羊價) and the first variable (牛價).

### Final Answer:
The values of `a`, `b`, and `c` represent the prices of 牛 (a), 羊 (b), and 豕 (c), respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: 23800/1359
Variable 'b' has wrong value. Expected: 500, Actual: 4600/453
Variable 'c' has wrong value. Expected: 300, Actual: -97400/1359"""
