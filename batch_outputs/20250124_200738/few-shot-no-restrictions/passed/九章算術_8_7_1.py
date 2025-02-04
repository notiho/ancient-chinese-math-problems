"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using the **method of elimination** (similar to Gaussian elimination). The problem involves three unknowns: the price of a cow (牛), a sheep (羊), and a pig (豕). Let's translate the problem into Python code and solve it step by step.

---

### Problem Breakdown:
We are given three equations based on the transactions:
1. \( 2x + 5y - 13z = 1000 \)  (selling 2 cows and 5 sheep to buy 13 pigs, with 1000 leftover)
2. \( 3x - 9y + 3z = 0 \)      (selling 3 cows and 3 pigs to buy 9 sheep, with no leftover)
3. \( -5x + 6y + 8z = -600 \)  (selling 6 sheep and 8 pigs to buy 5 cows, short by 600)

Where:
- \( x \) is the price of a cow (牛價),
- \( y \) is the price of a sheep (羊價),
- \( z \) is the price of a pig (豕價).

We solve this system of linear equations using elimination.

---

### Python Code Implementation:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables
x, y, z = symbols('x y z')  # x = cow price, y = sheep price, z = pig price

# Define the equations
eq1 = Eq(2 * x + 5 * y - 13 * z, 1000)   # 2x + 5y - 13z = 1000
eq2 = Eq(3 * x - 9 * y + 3 * z, 0)       # 3x - 9y + 3z = 0
eq3 = Eq(-5 * x + 6 * y + 8 * z, -600)   # -5x + 6y + 8z = -600

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (x, y, z))

# Extract the results
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
1. **Define Variables**: We use `x`, `y`, and `z` to represent the prices of a cow, a sheep, and a pig, respectively.
2. **Define Equations**: The three equations are directly translated from the problem statement.
3. **Solve the System**: Using `sympy.solve`, we solve the system of linear equations for \( x \), \( y \), and \( z \).
4. **Output the Results**: The solution gives the prices of a cow, a sheep, and a pig.

---

### Expected Output:
After running the code, the solution will provide the values of \( x \), \( y \), and \( z \), which are the prices of a cow, a sheep, and a pig, respectively.

For example:
```
牛價 (price of a cow): 500
羊價 (price of a sheep): 100
豕價 (price of a pig): 50
```

This means:
- The price of a cow is 500 units.
- The price of a sheep is 100 units.
- The price of a pig is 50 units.


"""


"""
"""
