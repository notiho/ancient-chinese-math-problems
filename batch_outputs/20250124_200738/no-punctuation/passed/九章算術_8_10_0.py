"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰馬價 a錢 牛價 b錢 
"""

"""
This is a classic simultaneous equations problem, solved using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving linear equations. Let's break it down step by step and encode the procedure.

The problem states:
- The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
- The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.
- We are to find the price of a horse and a cow.

The procedure for solving this uses the "fangcheng" method, which involves systematically eliminating variables to solve for unknowns.

### Equations:
1. \( 2x + y = 10000 + \frac{1}{2}x \)
2. \( x + 2y = 10000 - \frac{1}{2}y \)

Where:
- \( x \) is the price of a horse (in qian),
- \( y \) is the price of a cow (in qian).

### Procedure:
We will encode the "fangcheng" method step by step in Python.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement
# Equation 1: 2x + y = 10000 + (1/2)x
# Rearrange: (2 - 1/2)x + y = 10000
# Simplify: (3/2)x + y = 10000
eq1_coeff_x = Fraction(3, 2)  # Coefficient of x in equation 1
eq1_coeff_y = 1              # Coefficient of y in equation 1
eq1_const = 10000            # Constant term in equation 1

# Equation 2: x + 2y = 10000 - (1/2)y
# Rearrange: x + (2 + 1/2)y = 10000
# Simplify: x + (5/2)y = 10000
eq2_coeff_x = 1              # Coefficient of x in equation 2
eq2_coeff_y = Fraction(5, 2) # Coefficient of y in equation 2
eq2_const = 10000            # Constant term in equation 2

# Use the fangcheng method to eliminate one variable and solve for the other
# Multiply eq1 by the coefficient of x in eq2, and eq2 by the coefficient of x in eq1
# This aligns the coefficients of x for elimination
multiplier_eq1 = eq2_coeff_x
multiplier_eq2 = eq1_coeff_x

# Multiply equations
eq1_coeff_x *= multiplier_eq1
eq1_coeff_y *= multiplier_eq1
eq1_const *= multiplier_eq1

eq2_coeff_x *= multiplier_eq2
eq2_coeff_y *= multiplier_eq2
eq2_const *= multiplier_eq2

# Subtract eq2 from eq1 to eliminate x
eliminated_x_coeff = eq1_coeff_x - eq2_coeff_x  # This should be 0
eliminated_y_coeff = eq1_coeff_y - eq2_coeff_y
eliminated_const = eq1_const - eq2_const

# Solve for y
y = Fraction(eliminated_const, eliminated_y_coeff)

# Substitute y back into one of the original equations to solve for x
# Using equation 1: (3/2)x + y = 10000
x = Fraction(eq1_const - (eq1_coeff_y * y), eq1_coeff_x)

# Results
a = x  # Price of a horse
b = y  # Price of a cow

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. The equations are derived from the problem statement and rearranged into standard linear form.
2. The coefficients of \( x \) and \( y \) are extracted, and the constants are noted.
3. The "fangcheng" method is applied by aligning the coefficients of \( x \) in both equations, multiplying the equations accordingly, and then subtracting to eliminate \( x \).
4. The resulting single-variable equation is solved for \( y \).
5. The value of \( y \) is substituted back into one of the original equations to solve for \( x \).
6. The results are stored in \( a \) (price of a horse) and \( b \) (price of a cow).

### Final Answer:
The price of a horse is \( a \) qian, and the price of a cow is \( b \) qian.
"""


"""
"""
