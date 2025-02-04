"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics, specifically from the "Nine Chapters on the Mathematical Art" (《九章算術》). The problem involves solving for the prices of cows, sheep, and pigs using the method of elimination (similar to Gaussian elimination in modern algebra). Let's translate this into Python code.

### Problem Breakdown:
We are solving for the prices of:
- 牛 (cows): `a`
- 羊 (sheep): `b`
- 豕 (pigs): `c`

The problem gives us three equations:
1. \( 2a + 5b - 13c = 1000 \)  
2. \( 3a - 9b + 3c = 0 \)  
3. \( -5a + 6b + 8c = -600 \)  

We will solve this system of equations using Python.

---

### Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables for the prices of cows, sheep, and pigs
a, b, c = symbols('a b c')  # a = price of cow, b = price of sheep, c = price of pig

# Define the equations based on the problem
eq1 = Eq(2 * a + 5 * b - 13 * c, 1000)  # 2a + 5b - 13c = 1000
eq2 = Eq(3 * a - 9 * b + 3 * c, 0)      # 3a - 9b + 3c = 0
eq3 = Eq(-5 * a + 6 * b + 8 * c, -600)  # -5a + 6b + 8c = -600

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (a, b, c))

# Extract the solutions
牛價 = solution[a]
羊價 = solution[b]
豕價 = solution[c]

# Print the results
print(f"牛價 (price of cow): {牛價}")
print(f"羊價 (price of sheep): {羊價}")
print(f"豕價 (price of pig): {豕價}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `sympy.symbols` to define the variables \( a \), \( b \), and \( c \), representing the prices of cows, sheep, and pigs.
2. **Define Equations**: The three equations are written using `sympy.Eq` to represent the relationships given in the problem.
3. **Solve the System**: The `sympy.solve` function is used to solve the system of linear equations for \( a \), \( b \), and \( c \).
4. **Output Results**: The solution is printed, showing the prices of cows, sheep, and pigs.

---

### Expected Output:
After running the code, the output will provide the prices of cows, sheep, and pigs:

```
牛價 (price of cow): a
羊價 (price of sheep): b
豕價 (price of pig): c
```

Replace `a`, `b`, and `c` with the actual numerical values obtained from solving the equations.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: a
Variable 'b' has wrong value. Expected: 500, Actual: b
Variable 'c' has wrong value. Expected: 300, Actual: c"""
