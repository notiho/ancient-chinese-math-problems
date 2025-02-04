"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This is a classic example of a system of linear equations from ancient Chinese mathematics. The problem involves determining the contribution of each type of grain (white, green, yellow, and black) to a full dou when combined in specific proportions. Let's translate the procedure into Python code.

### Problem Breakdown:
- White grain (白禾) contributes 1 step of green and yellow.
- Green grain (青禾) contributes 1 step of yellow and black.
- Yellow grain (黃禾) contributes 1 step of black and white.
- Black grain (黑禾) contributes 1 step of white and green.
- The total combined volume equals 1 dou.

We need to solve for the contribution of each type of grain (白, 青, 黃, 黑) per step.

### Solution:
We will use Python to solve this system of linear equations.


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the contribution of each type of grain per step
白, 青, 黃, 黑 = symbols('白 青 黃 黑')

# Define the equations based on the problem
eq1 = Eq(白 + 青 + 黃, 1)  # White takes 1 step of green and yellow to make 1 dou
eq2 = Eq(青 + 黃 + 黑, 1)  # Green takes 1 step of yellow and black to make 1 dou
eq3 = Eq(黃 + 黑 + 白, 1)  # Yellow takes 1 step of black and white to make 1 dou
eq4 = Eq(黑 + 白 + 青, 1)  # Black takes 1 step of white and green to make 1 dou

# Solve the system of equations
solution = solve((eq1, eq2, eq3, eq4), (白, 青, 黃, 黑))

# Extract the results
a = solution[白]
b = solution[青]
c = solution[黃]
d = solution[黑]

# Print the results
print(f"白禾一步實 {a}斗")
print(f"青禾一步實 {b}斗")
print(f"黃禾一步實 {c}斗")
print(f"黑禾一步實 {d}斗")
#----- content ends here -----


"""


### Explanation:
1. **Define Variables**: Each variable (白, 青, 黃, 黑) represents the contribution of that type of grain per step.
2. **Set Up Equations**: Each equation corresponds to the relationship described in the problem, where the sum of contributions equals 1 dou.
3. **Solve the System**: Using `sympy.solve`, we solve the system of linear equations.
4. **Output Results**: The solution gives the contribution of each type of grain per step.

### Output:
The solution will provide the values of `a`, `b`, `c`, and `d`, which represent the contributions of white, green, yellow, and black grains per step, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
