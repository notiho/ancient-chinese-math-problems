"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two equations based on the prices of horses and cows:

1. \( 2a + b = 10000 + \frac{a}{2} \)
2. \( a + 2b = 10000 - \frac{b}{2} \)

Where:
- \( a \) is the price of a horse in "錢".
- \( b \) is the price of a cow in "錢".

We will solve for \( a \) and \( b \) using Python.


"""


from fractions import Fraction

# Define the equations
# Equation 1: 2a + b = 10000 + a / 2
# Equation 2: a + 2b = 10000 - b / 2

# Solve for a and b
# Rearrange Equation 1: 2a + b - a / 2 = 10000
# Multiply through by 2 to eliminate the fraction: 4a + 2b - a = 20000
# Simplify: 3a + 2b = 20000

# Rearrange Equation 2: a + 2b + b / 2 = 10000
# Multiply through by 2 to eliminate the fraction: 2a + 4b + b = 20000
# Simplify: 2a + 5b = 20000

# Solve the system of equations:
# 3a + 2b = 20000  (Equation 1)
# 2a + 5b = 20000  (Equation 2)

# Multiply Equation 1 by 5 and Equation 2 by 2 to align coefficients of b:
# 15a + 10b = 100000  (Modified Equation 1)
# 4a + 10b = 40000    (Modified Equation 2)

# Subtract Modified Equation 2 from Modified Equation 1:
# (15a + 10b) - (4a + 10b) = 100000 - 40000
# 11a = 60000
a = Fraction(60000, 11)  # Price of a horse

# Substitute a back into Equation 1 to solve for b:
# 3a + 2b = 20000
# 2b = 20000 - 3a
# b = (20000 - 3a) / 2
b = (Fraction(20000) - 3 * a) / 2  # Price of a cow

# Results
a, b


"""


### Explanation of the Code:
1. We start by translating the two equations into a system of linear equations.
2. We eliminate fractions by multiplying through by appropriate values.
3. We solve the system of equations using substitution and elimination.
4. The results are stored in variables `a` (price of a horse) and `b` (price of a cow).

### Final Answer:
- \( a \) (price of a horse) = \( \frac{60000}{11} \) 錢
- \( b \) (price of a cow) = \( \frac{40000}{11} \) 錢
"""


"""
"""
