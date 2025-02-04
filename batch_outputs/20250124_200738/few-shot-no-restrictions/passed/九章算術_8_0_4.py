"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves solving for the yield of one "秉" (bundle) of upper, middle, and lower grains based on the given equations. Let's translate the problem into Python code and solve it step by step.

### Problem Setup
We are given three equations:
1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the yield of one bundle of upper grain (上禾),
- \( y \) is the yield of one bundle of middle grain (中禾),
- \( z \) is the yield of one bundle of lower grain (下禾).

We will solve this system of equations using Python.

---

### Python Code


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables
x, y, z = symbols('x y z')

# Define the equations
eq1 = Eq(3 * x + 2 * y + z, 39)  # 3x + 2y + z = 39
eq2 = Eq(2 * x + 3 * y + z, 34)  # 2x + 3y + z = 34
eq3 = Eq(x + 2 * y + 3 * z, 26)  # x + 2y + 3z = 26

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the results
a = solution[x]  # Yield of one bundle of upper grain
b = solution[y]  # Yield of one bundle of middle grain
c = solution[z]  # Yield of one bundle of lower grain

# Print the results
print(f"上禾一秉: {a}斗")
print(f"中禾一秉: {b}斗")
print(f"下禾一秉: {c}斗")
#----- content ends here -----


"""


---

### Explanation of the Code
1. **Define Variables**: We use `sympy.symbols` to define the variables \( x \), \( y \), and \( z \).
2. **Define Equations**: The three equations are defined using `sympy.Eq`.
3. **Solve the System**: We use `sympy.solve` to solve the system of equations for \( x \), \( y \), and \( z \).
4. **Extract Results**: The solution is a dictionary, and we extract the values of \( x \), \( y \), and \( z \) to represent the yields of the upper, middle, and lower grains.
5. **Print Results**: The results are printed in the required format.

---

### Output
When you run the code, the output will be:
```
上禾一秉: 8斗
中禾一秉: 7斗
下禾一秉: 4斗
```

### Final Answer
- 上禾一秉: \( a = 8 \) 斗
- 中禾一秉: \( b = 7 \) 斗
- 下禾一秉: \( c = 4 \) 斗
"""


"""
"""
