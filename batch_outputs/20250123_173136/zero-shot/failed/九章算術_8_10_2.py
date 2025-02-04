"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve the problem, we need to translate the ancient Chinese math problem into Python code. The problem involves two equations based on the prices of horses and cows. Let the price of a horse be `a` (in 錢) and the price of a cow be `b` (in 錢). The equations are:

1. \( 2a + b = 10000 + \frac{a}{2} \)
2. \( a + 2b = 10000 - \frac{b}{2} \)

We will solve these equations step by step using Python and the `Fraction` class to ensure precision.


"""


from fractions import Fraction

# Define the equations
# Equation 1: 2a + b = 10000 + a/2
# Rearrange: 4a + 2b = 20000 + a
# Simplify: 3a + 2b = 20000
# Equation 2: a + 2b = 10000 - b/2
# Rearrange: 2a + 4b = 20000 - b
# Simplify: 2a + 5b = 20000

# Solve the system of equations:
# 3a + 2b = 20000  (1)
# 2a + 5b = 20000  (2)

# Multiply equation (1) by 2 and equation (2) by 3 to eliminate `a`:
# 6a + 4b = 40000  (1') 
# 6a + 15b = 60000 (2')

# Subtract (1') from (2'):
# (6a + 15b) - (6a + 4b) = 60000 - 40000
# 11b = 20000
b = Fraction(20000, 11)

# Substitute b back into equation (1) to solve for a:
# 3a + 2b = 20000
# 3a = 20000 - 2b
a = Fraction(20000) - 2 * b
a = a / 3

# Results
a = float(a)  # Convert to float for readability
b = float(b)  # Convert to float for readability

# Print the results
a, b


"""


The solution gives the price of a horse (`a`) and the price of a cow (`b`) in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 5454.545454545455
Variable 'b' has wrong value. Expected: 20000/11, Actual: 1818.1818181818182"""
