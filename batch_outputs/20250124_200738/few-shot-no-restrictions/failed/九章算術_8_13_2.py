"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This is a classic ancient Chinese problem involving simultaneous linear equations. The problem describes a situation where four types of grain (white, green, yellow, and black) are mixed in specific proportions to fill a single dou (a unit of volume). The goal is to determine how much of each type of grain is present in one step of measurement.

The solution involves setting up a system of linear equations and solving it using the method described in the problem, which is essentially Gaussian elimination. Let's translate this into Python code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables for the amount of each type of grain per step
白禾, 青禾, 黃禾, 黑禾 = symbols('白禾 青禾 黃禾 黑禾')

# Set up the equations based on the problem description
# White takes 1 step of green and yellow
# Green takes 1 step of yellow and black
# Yellow takes 1 step of black and white
# Black takes 1 step of white and green
eq1 = Eq(白禾 + 青禾 + 黃禾, 1)  # White's contribution to a full dou
eq2 = Eq(青禾 + 黃禾 + 黑禾, 1)  # Green's contribution to a full dou
eq3 = Eq(黃禾 + 黑禾 + 白禾, 1)  # Yellow's contribution to a full dou
eq4 = Eq(黑禾 + 白禾 + 青禾, 1)  # Black's contribution to a full dou

# Solve the system of equations
solution = solve((eq1, eq2, eq3, eq4), (白禾, 青禾, 黃禾, 黑禾))

# Extract the results
a = solution[白禾]
b = solution[青禾]
c = solution[黃禾]
d = solution[黑禾]

# Print the results
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Variables**: We define `白禾`, `青禾`, `黃禾`, and `黑禾` as the unknowns representing the amount of each type of grain in one step.
2. **Equations**: The problem gives us four equations based on how the grains are mixed to fill one dou.
3. **Solve**: We use `sympy.solve` to solve the system of linear equations.
4. **Results**: The solution gives the amount of each type of grain in one step.

### Output:
The solution will provide the values of `a`, `b`, `c`, and `d`, which represent the amount of each type of grain in one step.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
