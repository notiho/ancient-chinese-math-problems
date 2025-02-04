"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves solving for the prices of cows, sheep, and pigs based on the given transactions. Let's break it down step by step and solve it using Python.

The problem can be represented as a system of three linear equations:

1. \( 2x + 5y - 13z = 1000 \)  (selling 2 cows and 5 sheep to buy 13 pigs, with 1000 leftover)
2. \( 3x - 9y + 3z = 0 \)  (selling 3 cows and 3 pigs to buy 9 sheep, with no leftover)
3. \( -5x + 6y + 8z = -600 \)  (selling 6 sheep and 8 pigs to buy 5 cows, short by 600)

Where:
- \( x \) is the price of a cow,
- \( y \) is the price of a sheep,
- \( z \) is the price of a pig.

We will solve this system of equations using Python's `sympy` library, which is designed for symbolic mathematics.

---

### Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables
x, y, z = symbols('x y z')  # x: price of a cow, y: price of a sheep, z: price of a pig

# Define the equations
eq1 = Eq(2 * x + 5 * y - 13 * z, 1000)  # 2x + 5y - 13z = 1000
eq2 = Eq(3 * x - 9 * y + 3 * z, 0)      # 3x - 9y + 3z = 0
eq3 = Eq(-5 * x + 6 * y + 8 * z, -600)  # -5x + 6y + 8z = -600

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the solutions
a = solution[x]  # Price of a cow
b = solution[y]  # Price of a sheep
c = solution[z]  # Price of a pig

# Print the results
print(f"牛價 (price of a cow): {a}")
print(f"羊價 (price of a sheep): {b}")
print(f"豕價 (price of a pig): {c}")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Define Variables**: We define \( x, y, z \) as the prices of cows, sheep, and pigs, respectively.
2. **Define Equations**: Each transaction is translated into a linear equation.
3. **Solve the System**: Using `sympy.solve`, we solve the system of equations for \( x, y, z \).
4. **Output the Results**: The solution gives the prices of cows, sheep, and pigs.

---

### Expected Output:

After running the code, you will get the prices of the cow, sheep, and pig:

```
牛價 (price of a cow): a
羊價 (price of a sheep): b
豕價 (price of a pig): c
```

Replace \( a, b, c \) with the actual numerical results from the computation.
"""


"""
"""
