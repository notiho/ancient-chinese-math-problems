"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This is a classic ancient Chinese problem involving systems of linear equations. The problem describes three types of horses (武馬, 中馬, 下馬) with different pulling strengths, and the goal is to determine the pulling strength of each type of horse in terms of *shi* (石), a unit of weight.

The solution involves setting up equations based on the borrowing and sharing of loads, and solving them using elimination methods described in ancient Chinese mathematics (similar to Gaussian elimination). Let's translate this into Python code:

---


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables for the pulling strength of each type of horse
武馬, 中馬, 下馬 = symbols('武馬 中馬 下馬')

# Equation 1: 武馬 + 中馬 = 40 (武馬 borrows one 中馬's strength)
eq1 = Eq(武馬 + 中馬, 40)

# Equation 2: 中馬 + 下馬 = 40 (中馬 borrows one 下馬's strength)
eq2 = Eq(中馬 + 下馬, 40)

# Equation 3: 下馬 + 武馬 = 40 (下馬 borrows one 武馬's strength)
eq3 = Eq(下馬 + 武馬, 40)

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (武馬, 中馬, 下馬))

# Extract the results
a = solution[武馬]
b = solution[中馬]
c = solution[下馬]

# Print the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We define `武馬`, `中馬`, and `下馬` as the pulling strengths of the three types of horses.
2. **Set Up Equations**: Based on the problem:
   - 武馬 + 中馬 = 40 (武馬 borrows one 中馬's strength)
   - 中馬 + 下馬 = 40 (中馬 borrows one 下馬's strength)
   - 下馬 + 武馬 = 40 (下馬 borrows one 武馬's strength)
3. **Solve the System**: Using `sympy.solve`, we solve the system of linear equations.
4. **Output Results**: The solution gives the pulling strength of each type of horse.

### Output:
The solution will output the pulling strength of each horse in terms of *shi* (石):
```
武馬一匹力引 20 石
中馬一匹力引 20 石
下馬一匹力引 20 石
```

This means each horse has an equal pulling strength of 20 *shi*.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
