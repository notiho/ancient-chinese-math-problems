"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This is a classic ancient Chinese problem involving a system of linear equations. The problem describes three types of horses (武馬, 中馬, 下馬) and their respective contributions to carrying loads. The solution involves using a method similar to Gaussian elimination to solve the system of equations. Let's translate this into Python code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables for the pulling power of each type of horse
武馬力, 中馬力, 下馬力 = symbols('武馬力 中馬力 下馬力')

# Define the equations based on the problem description
# Each horse initially carries 40 石 but cannot ascend the slope.
# After borrowing horses:
# 武馬借中馬一匹 (武馬 gains the pulling power of 1 中馬)
# 中馬借下馬一匹 (中馬 gains the pulling power of 1 下馬)
# 下馬借武馬一匹 (下馬 gains the pulling power of 1 武馬)
# All horses can ascend the slope after borrowing.

# Equation 1: 武馬 + 中馬力 = 40
eq1 = Eq(武馬力 + 中馬力, 40)

# Equation 2: 中馬 + 下馬力 = 40
eq2 = Eq(中馬力 + 下馬力, 40)

# Equation 3: 下馬 + 武馬力 = 40
eq3 = Eq(下馬力 + 武馬力, 40)

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (武馬力, 中馬力, 下馬力))

# Extract the results
a = solution[武馬力]
b = solution[中馬力]
c = solution[下馬力]

# Print the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Define Variables**: We use `sympy.symbols` to define the pulling power of each type of horse as variables: `武馬力`, `中馬力`, and `下馬力`.
2. **Set Up Equations**: Based on the problem, we create three equations:
   - 武馬力 + 中馬力 = 40
   - 中馬力 + 下馬力 = 40
   - 下馬力 + 武馬力 = 40
3. **Solve the System**: Using `sympy.solve`, we solve the system of linear equations.
4. **Output the Results**: The solution gives the pulling power of each type of horse.

### Output:
The solution will compute the pulling power of each type of horse:
```
武馬一匹力引 20 石
中馬一匹力引 20 石
下馬一匹力引 20 石
```

This means each horse contributes equally to the load after borrowing.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
