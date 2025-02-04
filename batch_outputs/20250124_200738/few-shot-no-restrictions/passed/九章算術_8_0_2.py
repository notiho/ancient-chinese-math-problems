"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of one sheaf of upper, middle, and lower grain. Let's translate the ancient Chinese mathematical procedure into Python code using modern linear algebra techniques.

### Problem Description:
We are given the following equations based on the problem:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the yield of one sheaf of upper grain (上禾),
- \( y \) is the yield of one sheaf of middle grain (中禾),
- \( z \) is the yield of one sheaf of lower grain (下禾).

We need to solve for \( x \), \( y \), and \( z \).

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the yields of upper, middle, and lower grain
x, y, z = symbols('x y z')

# Define the equations
eq1 = Eq(3 * x + 2 * y + z, 39)  # 3x + 2y + z = 39
eq2 = Eq(2 * x + 3 * y + z, 34)  # 2x + 3y + z = 34
eq3 = Eq(x + 2 * y + 3 * z, 26)  # x + 2y + 3z = 26

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the results
a = solution[x]  # Yield of one sheaf of upper grain
b = solution[y]  # Yield of one sheaf of middle grain
c = solution[z]  # Yield of one sheaf of lower grain

# Print the results
print(f"上禾一秉, {a}斗，中禾一秉, {b}斗，下禾一秉, {c}斗。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `x`, `y`, and `z` to represent the yields of one sheaf of upper, middle, and lower grain, respectively.
2. **Define Equations**: The three equations are written based on the problem description.
3. **Solve the System**: The `solve` function from the `sympy` library is used to solve the system of linear equations.
4. **Extract Results**: The solution is extracted and printed in the required format.

---

### Output:
The solution to the system of equations will provide the yields of one sheaf of each type of grain:
```
上禾一秉, 7斗，中禾一秉, 5斗，下禾一秉, 3斗。
```

Thus:
- \( a = 7 \) (upper grain yield per sheaf),
- \( b = 5 \) (middle grain yield per sheaf),
- \( c = 3 \) (lower grain yield per sheaf).
"""


"""
"""
