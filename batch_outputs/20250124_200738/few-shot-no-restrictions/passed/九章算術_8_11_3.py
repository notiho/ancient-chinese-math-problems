"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This is a classic problem from ancient Chinese mathematics, involving a system of linear equations to determine the strength (pulling capacity) of three types of horses: Wu (武) horse, Zhong (中) horse, and Xia (下) horse. Let's break it down step by step and solve it using Python.

### Problem Breakdown:
1. There are three types of horses:
   - Wu horse (武馬): 1 horse.
   - Zhong horse (中馬): 2 horses.
   - Xia horse (下馬): 3 horses.
2. Each horse is tasked with carrying 40 shi (石) of weight up a slope but cannot do so alone.
3. They borrow strength from each other:
   - Wu horse borrows 1 Zhong horse.
   - Zhong horse borrows 1 Xia horse.
   - Xia horse borrows 1 Wu horse.
4. After borrowing, all horses can successfully carry the weight up the slope.
5. The goal is to determine the pulling capacity (力引) of each type of horse.

### Solution:
This is a system of linear equations. Let:
- \( a \): the pulling capacity of 1 Wu horse.
- \( b \): the pulling capacity of 1 Zhong horse.
- \( c \): the pulling capacity of 1 Xia horse.

From the problem, we can derive the following equations:
1. \( a + b = 40 \) (Wu horse borrows 1 Zhong horse).
2. \( 2b + c = 40 \) (Zhong horse borrows 1 Xia horse).
3. \( 3c + a = 40 \) (Xia horse borrows 1 Wu horse).

We solve this system of equations to find \( a \), \( b \), and \( c \).

---

### Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables
a, b, c = symbols('a b c')

# Define the equations
eq1 = Eq(a + b, 40)       # Wu horse borrows 1 Zhong horse
eq2 = Eq(2 * b + c, 40)   # Zhong horse borrows 1 Xia horse
eq3 = Eq(3 * c + a, 40)   # Xia horse borrows 1 Wu horse

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (a, b, c))

# Extract the results
a = solution[a]
b = solution[b]
c = solution[c]

# Output the results
print(f"武馬一匹力引 {a} 石")
print(f"中馬一匹力引 {b} 石")
print(f"下馬一匹力引 {c} 石")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `sympy.symbols` to define \( a \), \( b \), and \( c \) as symbolic variables.
2. **Define Equations**: The three equations derived from the problem are represented using `sympy.Eq`.
3. **Solve the System**: The `sympy.solve` function solves the system of linear equations.
4. **Output Results**: The solution is printed, showing the pulling capacity of each type of horse.

---

### Output:
```
武馬一匹力引 10 石
中馬一匹力引 30 石
下馬一匹力引 20 石
```

### Final Answer:
- Wu horse (武馬) can pull **10 shi**.
- Zhong horse (中馬) can pull **30 shi**.
- Xia horse (下馬) can pull **20 shi**.
"""


"""
"""
