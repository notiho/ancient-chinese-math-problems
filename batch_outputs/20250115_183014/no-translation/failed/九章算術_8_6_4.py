"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：牛 a ，直金 b兩 ，羊 c ，直金 d兩 。
"""

"""
To solve this problem, we need to translate the ancient Chinese "方程術" (method of solving systems of linear equations) into Python code. The problem involves solving a system of two linear equations:

1. \( 5x + 2y = 10 \) (where \( x \) is the price of a cow and \( y \) is the price of a sheep in gold taels).
2. \( 2x + 5y = 8 \).

Here is the Python code following the described procedure:


"""


from fractions import Fraction

# Define the coefficients of the equations
# 5x + 2y = 10
# 2x + 5y = 8
coefficients = [
    [5, 2, 10],  # First equation: 5x + 2y = 10
    [2, 5, 8]    # Second equation: 2x + 5y = 8
]

# Step 1: Eliminate the first variable (x) from the second equation
# Multiply the first equation by 2 (to match the coefficient of x in the second equation)
# Multiply the second equation by 5 (to match the coefficient of x in the first equation)
row1 = [coefficients[0][0] * 2, coefficients[0][1] * 2, coefficients[0][2] * 2]
row2 = [coefficients[1][0] * 5, coefficients[1][1] * 5, coefficients[1][2] * 5]

# Subtract the two equations to eliminate x
row2 = [row2[i] - row1[i] for i in range(3)]

# Now row2 represents the equation for y: ay = b
# Solve for y
y = Fraction(row2[2], row2[1])

# Step 2: Substitute y back into the first equation to solve for x
x = Fraction(coefficients[0][2] - coefficients[0][1] * y, coefficients[0][0])

# Results
a = "牛"
b = x
c = "羊"
d = y

print(f"{a}直金 {b}兩")
print(f"{c}直金 {d}兩")


"""


### Explanation of the Code:
1. The coefficients of the two equations are stored in a list.
2. The first step eliminates \( x \) by multiplying the equations to make the coefficients of \( x \) equal, then subtracting one equation from the other.
3. After eliminating \( x \), the second equation is solved for \( y \).
4. The value of \( y \) is substituted back into the first equation to solve for \( x \).
5. The results are printed as the price of a cow (\( x \)) and the price of a sheep (\( y \)) in gold taels.

### Answer:
- \( 牛 \)直金 \( b \)兩
- \( 羊 \)直金 \( d \)兩
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 牛
Variable 'c' has wrong value. Expected: 1, Actual: 羊"""
