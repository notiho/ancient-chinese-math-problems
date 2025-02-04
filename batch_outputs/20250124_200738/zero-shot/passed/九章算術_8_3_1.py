"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to determine the values of "a" (the amount of grain per unit of "上禾") and "b" (the amount of grain per unit of "下禾"). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem
# Equation 1: 5a - 7b = 1斗1升 = 10升 + 1升 = 11升
# Equation 2: 7a - 5b = 2斗5升 = 20升 + 5升 = 25升

# Solve the system of equations using substitution or elimination
# Multiply Equation 1 by 7 and Equation 2 by 5 to align coefficients of 'a'
# 35a - 49b = 77
# 35a - 25b = 125

# Subtract the second equation from the first
# -49b + 25b = 77 - 125
# -24b = -48
b = Fraction(-48, -24)  # Solve for b
b = Fraction(2)  # Simplify

# Substitute b back into one of the original equations to solve for a
# Using Equation 1: 5a - 7b = 11
# 5a - 7(2) = 11
# 5a - 14 = 11
# 5a = 25
a = Fraction(25, 5)  # Solve for a
a = Fraction(5)  # Simplify

# Results
print(f"上禾一秉 a = {a} 升")
print(f"下禾一秉 b = {b} 升")
#----- content ends here -----


"""


### Explanation of the Code:
1. The problem is translated into two linear equations:
   - \( 5a - 7b = 11 \) (where \( 11 \) represents \( 1斗1升 = 10升 + 1升 \))
   - \( 7a - 5b = 25 \) (where \( 25 \) represents \( 2斗5升 = 20升 + 5升 \))

2. The equations are solved using the elimination method:
   - Multiply the first equation by 7 and the second by 5 to align the coefficients of \( a \).
   - Subtract the second equation from the first to solve for \( b \).
   - Substitute \( b \) back into one of the original equations to solve for \( a \).

3. The results are expressed in terms of "升" (liters).

### Output:
```
上禾一秉 a = 5 升
下禾一秉 b = 2 升
```
"""


"""
"""
