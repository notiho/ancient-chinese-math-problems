"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine the values of "a" (the amount of grain per秉 for 上禾) and "b" (the amount of grain per秉 for 下禾).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem:
# Equation 1: 5a - 7b = 1斗1升 = 10升 + 1升 = 11升
# Equation 2: 7a - 5b = 2斗5升 = 20升 + 5升 = 25升

# Convert the equations into a system of linear equations:
# 5a - 7b = 11
# 7a - 5b = 25

# Solve for a and b using substitution or elimination:
# Multiply the first equation by 7 and the second equation by 5 to eliminate "a":
# 35a - 49b = 77
# 35a - 25b = 125

# Subtract the second equation from the first:
# -49b + 25b = 77 - 125
# -24b = -48
b = Fraction(-48, -24)  # Simplify
b = Fraction(2)  # b is the amount of grain per秉 for 下禾 in 升

# Substitute b back into the first equation to solve for a:
# 5a - 7b = 11
# 5a - 7(2) = 11
# 5a - 14 = 11
# 5a = 25
a = Fraction(25, 5)  # Simplify
a = Fraction(5)  # a is the amount of grain per秉 for 上禾 in 升

# Results:
print("a =", a, "升")  # 上禾一秉的實
print("b =", b, "升")  # 下禾一秉的實
#----- content ends here -----


"""


### Explanation:
1. The problem is translated into two linear equations based on the given conditions.
2. The units are converted into 升 (1斗 = 10升) for consistency.
3. The system of equations is solved using elimination to find the values of "a" and "b".
4. The solutions are stored in variables `a` and `b` and printed.

### Output:
```
a = 5 升
b = 2 升
```

Thus, the amount of grain per秉 for 上禾 is 5升, and for 下禾 is 2升.
"""


"""
"""
