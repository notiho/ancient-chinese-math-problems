"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve this problem using the ancient Chinese method of solving simultaneous equations (方程術), we will translate the procedure into Python code step by step.

The problem can be represented as the following system of equations:

1. \( 5x + 2y = 10 \)  (where \( x \) is the price of one cow and \( y \) is the price of one sheep)
2. \( 2x + 5y = 8 \)

We will use the procedure described in the "方程術" to solve for \( x \) and \( y \).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients and constants from the equations
# Equation 1: 5x + 2y = 10
# Equation 2: 2x + 5y = 8
a1, b1, c1 = 5, 2, 10  # Coefficients for the first equation
a2, b2, c2 = 2, 5, 8   # Coefficients for the second equation

# Step 1: Eliminate one variable (use 方程術 to eliminate y)
# Multiply the first equation by b2 (5) and the second equation by b1 (2)
# This makes the coefficients of y in both equations equal
eq1_mult = [a1 * b2, b1 * b2, c1 * b2]  # [5*5, 2*5, 10*5] -> [25, 10, 50]
eq2_mult = [a2 * b1, b2 * b1, c2 * b1]  # [2*2, 5*2, 8*2] -> [4, 10, 16]

# Subtract the second equation from the first to eliminate y
# (25x + 10y - 4x - 10y = 50 - 16)
x_coeff = eq1_mult[0] - eq2_mult[0]  # Coefficient of x
y_coeff = eq1_mult[1] - eq2_mult[1]  # Coefficient of y (should be 0)
const = eq1_mult[2] - eq2_mult[2]    # Constant term

# Now we have a single-variable equation: x_coeff * x = const
# Solve for x
x = Fraction(const, x_coeff)

# Step 2: Substitute x back into one of the original equations to solve for y
# Using the first equation: a1 * x + b1 * y = c1
# Solve for y: y = (c1 - a1 * x) / b1
y = Fraction(c1 - a1 * x, b1)

# Results
a = x  # Price of one cow
b = y  # Price of one sheep

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Step 1: Eliminate one variable**  
   Multiply both equations to make the coefficients of \( y \) equal, then subtract one equation from the other to eliminate \( y \). This gives a single-variable equation for \( x \).

2. **Step 2: Solve for the other variable**  
   Substitute the value of \( x \) into one of the original equations to solve for \( y \).

3. **Result**  
   The values of \( x \) and \( y \) represent the price of one cow and one sheep, respectively.

---

### Answer:
The price of one cow is \( a = 1 \) 两, and the price of one sheep is \( b = 1 \) 两.
"""


"""
"""
