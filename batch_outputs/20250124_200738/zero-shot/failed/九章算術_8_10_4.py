"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of equations to find the price of a horse (`a`) and the price of a cow (`b`).

The problem can be represented as:
1. \( 2a + b = 10000 + \frac{1}{2}a \)
2. \( a + 2b = 10000 - \frac{1}{2}b \)

We will solve these equations step by step using Python.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# Equation 1: 2a + b = 10000 + (1/2)a
# Rearrange to: (2 - 1/2)a + b = 10000
# Simplify: (3/2)a + b = 10000
# Equation 2: a + 2b = 10000 - (1/2)b
# Rearrange to: a + (2 + 1/2)b = 10000
# Simplify: a + (5/2)b = 10000

# Let us solve these equations
# From Equation 1: b = 10000 - (3/2)a
# Substitute into Equation 2: a + (5/2)(10000 - (3/2)a) = 10000

# Solve for a
a = Fraction(10000 * 2, 11)  # Simplified calculation for a
b = 10000 - Fraction(3, 2) * a  # Substitute a into Equation 1 to find b

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. The equations are derived from the problem statement.
2. The first equation is simplified to \( \frac{3}{2}a + b = 10000 \).
3. The second equation is simplified to \( a + \frac{5}{2}b = 10000 \).
4. Substituting \( b = 10000 - \frac{3}{2}a \) from the first equation into the second equation allows us to solve for \( a \).
5. Once \( a \) is found, it is substituted back into the first equation to find \( b \).

### Solution:
The values of \( a \) (price of a horse) and \( b \) (price of a cow) are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 20000/11
Variable 'b' has wrong value. Expected: 20000/11, Actual: 80000/11"""
