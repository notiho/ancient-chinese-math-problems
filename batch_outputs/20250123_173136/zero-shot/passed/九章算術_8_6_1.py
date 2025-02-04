"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of `a` (price of one cow in gold) and `b` (price of one sheep in gold).

The equations are:
1. \( 5a + 2b = 10 \)
2. \( 2a + 5b = 8 \)

We will solve this system of equations using Python.


"""


from fractions import Fraction

# Define the equations
# 5a + 2b = 10
# 2a + 5b = 8

# Step 1: Solve for `a` in terms of `b` using the first equation
# a = (10 - 2b) / 5
# Substitute this into the second equation

# Step 2: Substitute into the second equation
# 2((10 - 2b) / 5) + 5b = 8
# Multiply through by 5 to eliminate fractions
# 2(10 - 2b) + 25b = 40
# 20 - 4b + 25b = 40
# 21b = 20
# b = 20 / 21

b = Fraction(20, 21)

# Step 3: Solve for `a` using the first equation
# 5a + 2b = 10
# 5a = 10 - 2b
# a = (10 - 2b) / 5

a = (10 - 2 * b) / 5

# The results
a, b


"""


### Explanation of the Code:
1. We use the `Fraction` class to ensure that the calculations are exact and can handle non-integer results.
2. We solve the first equation for `a` in terms of `b` and substitute it into the second equation to find `b`.
3. Once `b` is found, we substitute it back into the first equation to find `a`.

### Final Answer:
The values of `a` and `b` are stored in the variables `a` and `b`, respectively.
"""


"""
"""
