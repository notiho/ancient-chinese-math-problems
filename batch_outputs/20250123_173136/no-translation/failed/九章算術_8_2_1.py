"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The procedure involves solving a system of linear equations using elimination methods described in the text.


"""


from fractions import Fraction

# Step 1: Define the given values
# Upward, middle, and downward wheat bundles
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# Total wheat after redistribution
總實 = 39

# Step 2: Set up the equations based on the problem
# Let a, b, c represent the amount of wheat in one bundle of 上禾, 中禾, 下禾 respectively.
# The equations are:
# 2a + b = 39 (from 上禾)
# a + 3b + c = 39 (from 中禾)
# b + 4c = 39 (from 下禾)

# Step 3: Solve the system of equations using elimination
# Eliminate `a` from the equations
# Multiply the first equation by 1 and subtract it from the second equation
# 2a + b = 39
# a + 3b + c = 39
# Subtract: (a + 3b + c) - (2a + b) = 39 - 39
# Result: -a + 2b + c = 0

# Now we have:
# 2a + b = 39
# -a + 2b + c = 0
# b + 4c = 39

# Solve for `a` in terms of `b` from the first equation
# 2a + b = 39
a = Fraction(39 - b, 2)

# Substitute `a` into the second equation
# -a + 2b + c = 0
# -((39 - b) / 2) + 2b + c = 0
# Multiply through by 2 to eliminate the fraction
# -(39 - b) + 4b + 2c = 0
# -39 + b + 4b + 2c = 0
# 5b + 2c = 39

# Now we have:
# 5b + 2c = 39
# b + 4c = 39

# Solve for `b` and `c` using elimination
# Multiply the first equation by 4 and subtract the second equation
# 4(5b + 2c) - (b + 4c) = 4(39) - 39
# 20b + 8c - b - 4c = 156 - 39
# 19b + 4c = 117

# Solve for `b`
b = Fraction(117 - 4 * c, 19)

# Substitute `b` into the second equation to solve for `c`
# b + 4c = 39
# (117 - 4c) / 19 + 4c = 39
# Multiply through by 19 to eliminate the fraction
# 117 - 4c + 76c = 741
# 72c = 624
c = Fraction(624, 72)

# Solve for `b` using the value of `c`
b = Fraction(117 - 4 * c, 19)

# Solve for `a` using the value of `b`
a = Fraction(39 - b, 2)

# Step 4: Output the results
print(f"上禾一秉實 a = {a} 斗")
print(f"中禾一秉實 b = {b} 斗")
print(f"下禾一秉實 c = {c} 斗")


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations based on the relationships described in the text.
2. The equations are solved step by step using substitution and elimination, as described in the ancient procedure.
3. The `Fraction` class is used to ensure exact arithmetic, as the problem involves precise fractional values.
4. The final results for `a`, `b`, and `c` represent the amount of wheat in one bundle of 上禾, 中禾, and 下禾, respectively.

### Final Answer:
The values of `a`, `b`, and `c` will be printed as the solution to the problem.
"""


"""
Code error: name 'b' is not defined"""
