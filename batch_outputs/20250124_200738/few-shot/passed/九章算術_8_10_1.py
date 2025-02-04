"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This is a classic simultaneous equations problem, solved using ancient Chinese "fangcheng" (method of solving linear equations). Let's translate the problem and the procedure into Python code step by step.

The problem can be expressed as:
1. \( 2x + y = 10000 + \frac{x}{2} \)  (Two horses and one cow equal 10,000 plus half the price of a horse)
2. \( x + 2y = 10000 - \frac{y}{2} \)  (One horse and two cows equal 10,000 minus half the price of a cow)

Where \( x \) is the price of a horse, and \( y \) is the price of a cow.

We will solve this using the "fangcheng" method, which is essentially Gaussian elimination.

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: 2x + y - (1/2)x = 10000
# Simplified: (3/2)x + y = 10000
eq1_x = Fraction(3, 2)  # Coefficient of x in equation 1
eq1_y = 1              # Coefficient of y in equation 1
eq1_const = 10000      # Constant term in equation 1

# Equation 2: x + 2y + (1/2)y = 10000
# Simplified: x + (5/2)y = 10000
eq2_x = 1              # Coefficient of x in equation 2
eq2_y = Fraction(5, 2) # Coefficient of y in equation 2
eq2_const = 10000      # Constant term in equation 2

# Step 1: Eliminate x from the second equation
# Multiply eq1 by eq2_x and eq2 by eq1_x to align the x coefficients
factor1 = eq2_x
factor2 = eq1_x

new_eq1_y = factor1 * eq1_y
new_eq1_const = factor1 * eq1_const

new_eq2_y = factor2 * eq2_y
new_eq2_const = factor2 * eq2_const

# Subtract the two equations to eliminate x
final_eq_y = new_eq2_y - new_eq1_y
final_eq_const = new_eq2_const - new_eq1_const

# Solve for y (price of a cow)
y = final_eq_const / final_eq_y

# Step 2: Solve for x (price of a horse) using the first equation
x = (eq1_const - eq1_y * y) / eq1_x

# Results
a = x  # Price of a horse
b = y  # Price of a cow

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code
1. **Equation Setup**: The two equations are expressed in terms of \( x \) and \( y \), and their coefficients are extracted.
2. **Elimination**: Using the "fangcheng" method, we eliminate \( x \) by aligning the coefficients of \( x \) in both equations and subtracting one equation from the other.
3. **Solve for \( y \)**: After eliminating \( x \), we solve for \( y \) (the price of a cow).
4. **Solve for \( x \)**: Using the value of \( y \), we substitute back into one of the original equations to solve for \( x \) (the price of a horse).

### Answer
The price of a horse is \( a \) qian, and the price of a cow is \( b \) qian.
"""


"""
"""
