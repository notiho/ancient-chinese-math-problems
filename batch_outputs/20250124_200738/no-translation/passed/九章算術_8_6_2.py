"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem is a classic simultaneous equations problem, which can be solved using the method of elimination or substitution. The ancient Chinese method described here is essentially a systematic way to solve simultaneous linear equations. Let's translate this into Python code:

### Problem Setup:
We are solving the following equations:
1. \( 5x + 2y = 10 \)
2. \( 2x + 5y = 8 \)

Where \( x \) is the price of one cow (牛), and \( y \) is the price of one sheep (羊).


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients from the equations
# Equation 1: 5x + 2y = 10
a1, b1, c1 = 5, 2, 10

# Equation 2: 2x + 5y = 8
a2, b2, c2 = 2, 5, 8

# Step 1: Eliminate one variable (y) by multiplying equations to align coefficients
# Multiply equation 1 by 5 and equation 2 by 2 (to align y coefficients)
A1 = a1 * 5  # 5 * 5 = 25
B1 = b1 * 5  # 2 * 5 = 10
C1 = c1 * 5  # 10 * 5 = 50

A2 = a2 * 2  # 2 * 2 = 4
B2 = b2 * 2  # 5 * 2 = 10
C2 = c2 * 2  # 8 * 2 = 16

# Subtract the second equation from the first to eliminate y
# (25x + 10y) - (4x + 10y) = 50 - 16
X_coeff = A1 - A2  # 25 - 4 = 21
Y_coeff = B1 - B2  # 10 - 10 = 0
Const = C1 - C2    # 50 - 16 = 34

# Solve for x (price of one cow)
x = Fraction(Const, X_coeff)  # x = 34 / 21

# Step 2: Substitute x back into one of the original equations to solve for y
# Using equation 1: 5x + 2y = 10
y = Fraction(c1 - a1 * x, b1)  # y = (10 - 5x) / 2

# Results
a = x  # Price of one cow
b = y  # Price of one sheep

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. The coefficients of the equations are extracted and aligned to eliminate one variable (in this case, \( y \)).
2. The resulting equation is solved for \( x \) (price of one cow).
3. The value of \( x \) is substituted back into one of the original equations to solve for \( y \) (price of one sheep).
4. The results are stored in variables \( a \) and \( b \), representing the price of one cow and one sheep, respectively.

### Final Answer:
- \( a \): Price of one cow in gold (兩)
- \( b \): Price of one sheep in gold (兩)
"""


"""
"""
