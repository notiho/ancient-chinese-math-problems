"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves finding the values of \(a\), \(b\), and \(c\) (the amount of grain in one秉 of upper, middle, and lower grain respectively) using the given conditions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given conditions:
# Upper grain (2秉), middle grain (3秉), lower grain (4秉)
# After exchanging 1秉 between them, each becomes full (1斗).

# Let:
# a = amount of grain in 1秉 of upper grain
# b = amount of grain in 1秉 of middle grain
# c = amount of grain in 1秉 of lower grain

# Equations based on the problem:
# 1. 2a + b = 1 (upper grain becomes full after taking 1秉 from middle grain)
# 2. 3b + c = 1 (middle grain becomes full after taking 1秉 from lower grain)
# 3. 4c + a = 1 (lower grain becomes full after taking 1秉 from upper grain)

# Solve the equations:
# From equation 1: b = 1 - 2a
# Substitute b into equation 2: 3(1 - 2a) + c = 1
# Simplify: 3 - 6a + c = 1
# c = 6a - 2
# Substitute c into equation 3: 4(6a - 2) + a = 1
# Simplify: 24a - 8 + a = 1
# 25a = 9
# a = 9/25

a = Fraction(9, 25)

# Calculate b using b = 1 - 2a
b = 1 - 2 * a

# Calculate c using c = 6a - 2
c = 6 * a - 2

# Results:
# a, b, c represent the amount of grain in 1秉 of upper, middle, and lower grain respectively.
#----- content ends here -----


"""


### Explanation of the solution:
1. We start with the three equations derived from the problem:
   - \(2a + b = 1\)
   - \(3b + c = 1\)
   - \(4c + a = 1\)
2. Solve for \(b\) in terms of \(a\) from the first equation.
3. Substitute \(b\) into the second equation to express \(c\) in terms of \(a\).
4. Substitute \(c\) into the third equation to solve for \(a\).
5. Once \(a\) is found, substitute back to find \(b\) and \(c\).

### Final Results:
- \(a = \frac{9}{25}\)斗
- \(b = \frac{7}{25}\)斗
- \(c = \frac{8}{25}\)斗
"""


"""
"""
