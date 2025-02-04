"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This is a classic simultaneous equations problem, solved using the ancient Chinese method of "fangcheng" (方程), which is an early form of solving systems of linear equations. Let's translate the problem and solution into Python code step by step.

The problem states:
- The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
- The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.

We need to find the price of a horse (*a*) and the price of a cow (*b*).

The procedure for solving this uses the "fangcheng" method, which involves systematically eliminating variables to solve the system of equations.

### Equations:
1. \( 2a + b = 10000 + \frac{1}{2}a \)
2. \( a + 2b = 10000 - \frac{1}{2}b \)

Rewriting these equations:
1. \( \frac{3}{2}a + b = 10000 \)
2. \( a + \frac{5}{2}b = 10000 \)

Now, let's solve this step by step using Python.


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients of the equations
# Equation 1: (3/2)a + b = 10000
coeff1_a = Fraction(3, 2)
coeff1_b = 1
const1 = 10000

# Equation 2: a + (5/2)b = 10000
coeff2_a = 1
coeff2_b = Fraction(5, 2)
const2 = 10000

# Use the fangcheng method to eliminate one variable
# Multiply the first equation by 2 to eliminate fractions
coeff1_a *= 2
coeff1_b *= 2
const1 *= 2

# Now Equation 1 becomes: 3a + 2b = 20000
# Equation 2 remains: a + (5/2)b = 10000

# Multiply Equation 2 by 2 to eliminate fractions
coeff2_a *= 2
coeff2_b *= 2
const2 *= 2

# Now Equation 2 becomes: 2a + 5b = 20000

# Eliminate variable 'a' by aligning coefficients
# Multiply Equation 1 by 2 and Equation 2 by 3
eq1_a = coeff1_a * 2  # 6a
eq1_b = coeff1_b * 2  # 4b
eq1_const = const1 * 2  # 40000

eq2_a = coeff2_a * 3  # 6a
eq2_b = coeff2_b * 3  # 15b
eq2_const = const2 * 3  # 60000

# Subtract Equation 1 from Equation 2 to eliminate 'a'
final_b_coeff = eq2_b - eq1_b  # 15b - 4b = 11b
final_const = eq2_const - eq1_const  # 60000 - 40000 = 20000

# Solve for 'b'
b = Fraction(final_const, final_b_coeff)

# Substitute 'b' back into one of the original equations to solve for 'a'
# Using Equation 1: 3a + 2b = 20000
a = Fraction(const1 - (coeff1_b * b), coeff1_a)

# Output the results
a_value = a
b_value = b

a_value, b_value
#----- content ends here -----


"""


### Explanation of the Code:
1. The coefficients of the equations are represented as fractions to maintain precision.
2. The equations are manipulated to eliminate one variable using the "fangcheng" method.
3. After eliminating one variable, the remaining variable is solved.
4. The solved value is substituted back into one of the original equations to find the other variable.

### Final Answer:
- The price of a horse (*a*) is \( a_value \) qian.
- The price of a cow (*b*) is \( b_value \) qian.
"""


"""
"""
