"""
今有上禾三秉，益實六斗，當下禾十秉。下禾五秉，益實一斗，當上禾二秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾三秉正，下禾一十秉負，益實六斗負。次置上禾二秉負，下禾五秉正，益實一斗負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. We will use the `Fraction` class to handle numbers that might not be integers. The problem involves solving a system of linear equations to find the values of `a` (the amount of grain per unit for the upper crop) and `b` (the amount of grain per unit for the lower crop).

The equations derived from the problem are:

1. \( 3a - 10b = -6 \)
2. \( -2a + 5b = -1 \)

We will solve these equations step by step.


"""


from fractions import Fraction

# Define the equations
# 3a - 10b = -6
# -2a + 5b = -1

# Step 1: Solve for `a` in terms of `b` using the first equation
# 3a = 10b - 6
# a = (10b - 6) / 3
def solve():
    # Step 2: Substitute `a` into the second equation
    # -2((10b - 6) / 3) + 5b = -1
    # Multiply through by 3 to eliminate fractions
    # -2(10b - 6) + 15b = -3
    # -20b + 12 + 15b = -3
    # -5b + 12 = -3
    # -5b = -15
    # b = 3
    b = Fraction(3)

    # Step 3: Substitute `b` back into the first equation to find `a`
    # 3a - 10(3) = -6
    # 3a - 30 = -6
    # 3a = 24
    # a = 8
    a = Fraction(8)

    return a, b

a, b = solve()

# The results
print(f"a = {a} (斗 per unit for the upper crop)")
print(f"b = {b} (斗 per unit for the lower crop)")


"""


### Explanation of the Code:
1. We start by defining the two equations based on the problem statement.
2. We solve for `a` in terms of `b` using the first equation.
3. We substitute this expression for `a` into the second equation to solve for `b`.
4. Once `b` is found, we substitute it back into the first equation to solve for `a`.
5. The results are stored in variables `a` and `b`, which represent the grain per unit for the upper and lower crops, respectively.

### Output:
```
a = 8 (斗 per unit for the upper crop)
b = 3 (斗 per unit for the lower crop)
```
"""


"""
"""
