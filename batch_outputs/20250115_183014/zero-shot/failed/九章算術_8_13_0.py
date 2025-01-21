"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of equations to find the values of the unknowns. We'll use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""


from fractions import Fraction

# Define the steps for each type of grain
white_steps = 2
green_steps = 3
yellow_steps = 4
black_steps = 5

# Define the system of equations based on the problem statement
# Let a, b, c, d, e, f, g, h represent the unknowns
# a, c, e, g are the steps of each grain
# b, d, f, h are the actual amounts of grain in斗 (dou)

# Equation 1: White (a) + Green (c) + Yellow (e) + Black (g) = 1斗
# Equation 2: Green (c) + Yellow (e) + Black (g) + White (a) = 1斗
# Equation 3: Yellow (e) + Black (g) + White (a) + Green (c) = 1斗
# Equation 4: Black (g) + White (a) + Green (c) + Yellow (e) = 1斗

# Solve for the unknowns
# Since the problem states that each grain contributes equally to the total斗,
# we can deduce that each grain contributes 1/4斗.

b = Fraction(1, 4)  # White grain amount in斗
d = Fraction(1, 4)  # Green grain amount in斗
f = Fraction(1, 4)  # Yellow grain amount in斗
h = Fraction(1, 4)  # Black grain amount in斗

# Assign the steps for each grain
a = white_steps
c = green_steps
e = yellow_steps
g = black_steps

# Print the results
print(f"White grain: {a} steps, {b}斗")
print(f"Green grain: {c} steps, {d}斗")
print(f"Yellow grain: {e} steps, {f}斗")
print(f"Black grain: {g} steps, {h}斗")


"""


### Explanation:
1. The problem describes a system of equations where the sum of contributions from all grains equals 1斗.
2. Each grain contributes equally to the total, so each grain contributes \( \frac{1}{4} \)斗.
3. The steps for each grain are given directly in the problem: 2 for white, 3 for green, 4 for yellow, and 5 for black.
4. The solution assigns the respective steps and斗 values to the variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h`.

### Output:
```
White grain: 2 steps, 1/4斗
Green grain: 3 steps, 1/4斗
Yellow grain: 4 steps, 1/4斗
Black grain: 5 steps, 1/4斗
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 11/37, Actual: 1/4
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 28/111, Actual: 1/4
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 17/111, Actual: 1/4
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 10/111, Actual: 1/4"""
