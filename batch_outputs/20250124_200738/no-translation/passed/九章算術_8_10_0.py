"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of equations using a method similar to Gaussian elimination, as described in the "方程術" (method of equations). Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# 2馬 + 1牛 = 10000 + 0.5馬
# 1馬 + 2牛 = 10000 - 0.5牛

# Rewrite the equations to standard form:
# 1.5馬 + 1牛 = 10000
# 1馬 + 2.5牛 = 10000

# Coefficients of the equations:
# Equation 1: 1.5馬 + 1牛 = 10000
a1, b1, c1 = Fraction(3, 2), Fraction(1), Fraction(10000)

# Equation 2: 1馬 + 2.5牛 = 10000
a2, b2, c2 = Fraction(1), Fraction(5, 2), Fraction(10000)

# Step 1: Eliminate 馬 (x) from the second equation
# Multiply the first equation by a2 and the second equation by a1
factor1 = a2
factor2 = a1

a1, b1, c1 = a1 * factor1, b1 * factor1, c1 * factor1
a2, b2, c2 = a2 * factor2, b2 * factor2, c2 * factor2

# Subtract the first equation from the second to eliminate 馬 (x)
b2 -= b1
c2 -= c1

# Now we have a single equation for 牛 (y):
# b2牛 = c2
牛 = c2 / b2

# Step 2: Solve for 馬 (x) using the first equation
# a1馬 + b1牛 = c1
馬 = (c1 - b1 * 牛) / a1

# Results
a = 馬
b = 牛

# Output the results
print(f"馬價 a錢 = {a}")
print(f"牛價 b錢 = {b}")
#----- content ends here -----


"""


### Explanation of the Code:
1. The equations are rewritten in standard form using the problem's description.
2. The coefficients of the equations are represented as fractions to ensure precision.
3. The elimination method is applied to remove one variable (馬) and solve for the other (牛).
4. Once 牛 is determined, 馬 is calculated using one of the original equations.
5. The results are printed as fractions for exact values.

### Final Answer:
- `馬價 a錢` is the value of a horse.
- `牛價 b錢` is the value of a cow.
"""


"""
"""
