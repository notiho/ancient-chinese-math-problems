"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This problem involves solving a system of equations to determine the pulling strength of three types of horses: 武馬 (strong horse), 中馬 (medium horse), and 下馬 (weak horse). The problem is essentially a classic linear algebra problem, where we use the given relationships to solve for the pulling strength of each horse.

### Problem Breakdown:
1. Each horse type initially cannot pull 40 石 (units of weight) up the slope.
2. Borrowing relationships:
   - 武馬 borrows 1 中馬.
   - 中馬 borrows 1 下馬.
   - 下馬 borrows 1 武馬.
3. After borrowing, all horses can pull the weight up the slope.
4. We need to determine the pulling strength of each horse type.

### Mathematical Representation:
Let:
- \( x \): pulling strength of 武馬 (strong horse).
- \( y \): pulling strength of 中馬 (medium horse).
- \( z \): pulling strength of 下馬 (weak horse).

From the problem, we derive the following equations:
1. \( x + y = 40 \) (武馬 with the help of 1 中馬 can pull 40 石).
2. \( y + z = 40 \) (中馬 with the help of 1 下馬 can pull 40 石).
3. \( z + x = 40 \) (下馬 with the help of 1 武馬 can pull 40 石).

We solve this system of equations to find \( x \), \( y \), and \( z \).

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables
x, y, z = symbols('x y z')  # x: 武馬, y: 中馬, z: 下馬

# Define the equations
eq1 = Eq(x + y, 40)  # 武馬 + 中馬 = 40
eq2 = Eq(y + z, 40)  # 中馬 + 下馬 = 40
eq3 = Eq(z + x, 40)  # 下馬 + 武馬 = 40

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the results
a = solution[x]  # 武馬 pulling strength
b = solution[y]  # 中馬 pulling strength
c = solution[z]  # 下馬 pulling strength

# Output the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


---

### Explanation of the Solution:
1. The equations are solved simultaneously using symbolic computation.
2. The solution gives the pulling strength of each horse type.

---

### Output:
After running the code, the output will be:
```
武馬一匹力引 20 石
中馬一匹力引 20 石
下馬一匹力引 20 石
```

Thus, each horse type has a pulling strength of **20 石**.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
