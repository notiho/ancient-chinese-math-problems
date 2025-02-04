"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
To solve this problem, we will translate the described procedure into Python code step by step. The problem involves solving a system of linear equations using the ancient Chinese method described in the text. Here's the implementation:


"""


from fractions import Fraction

# Step 1: Define the given values
# Up, middle, and down wheat bundles
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# Total amount of wheat when redistributed
總實 = 39

# Step 2: Set up the equations
# Let a, b, c represent the amount of wheat in one bundle of 上禾, 中禾, 下禾 respectively.
# The equations are:
# 2a + b = 39 (from 上禾 taking 1 中禾 and 1 下禾)
# a + 3b + c = 39 (from 中禾 taking 1 下禾 and 1 上禾)
# b + 4c = 39 (from 下禾 taking 1 上禾 and 1 中禾)

# Step 3: Solve the system of equations using the described method
# Initialize the coefficients and constants
上禾 = [2, 1, 0, 39]  # 2a + b + 0c = 39
中禾 = [1, 3, 1, 39]  # a + 3b + c = 39
下禾 = [0, 1, 4, 39]  # 0a + b + 4c = 39

# Eliminate a from 中禾 and 下禾
for i in range(3):
    中禾[i] = 中禾[i] * 上禾[0] - 上禾[i] * 中禾[0]
    下禾[i] = 下禾[i] * 上禾[0] - 上禾[i] * 下禾[0]

# Eliminate b from 下禾
for i in range(3, 0, -1):
    下禾[i] = 下禾[i] * 中禾[1] - 中禾[i] * 下禾[1]

# Solve for c
c = Fraction(下禾[3], 下禾[2])

# Solve for b
b = Fraction(中禾[3] - 中禾[2] * c, 中禾[1])

# Solve for a
a = Fraction(上禾[3] - 上禾[1] * b, 上禾[0])

# Step 4: Output the results
a斗 = a
b斗 = b
c斗 = c

# Results
print(f"上禾一秉實 {a斗} 斗")
print(f"中禾一秉實 {b斗} 斗")
print(f"下禾一秉實 {c斗} 斗")


"""


### Explanation of the Code:
1. The equations are set up based on the problem description.
2. The elimination process follows the ancient Chinese method described in the text:
   - Eliminate variables step by step using multiplication and subtraction.
   - Solve for the remaining variables using substitution.
3. The results are expressed as fractions to ensure precision.

### Final Answer:
The values of `a斗`, `b斗`, and `c斗` represent the amount of wheat in one bundle of 上禾, 中禾, and 下禾, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 741/44
Variable 'b' has wrong value. Expected: 7/25, Actual: 117/22
Variable 'c' has wrong value. Expected: 4/25, Actual: 39/11"""
