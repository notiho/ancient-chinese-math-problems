"""
今有賣牛二、羊五，以買十三豕，有餘錢一千。賣牛三、豕三，以買九羊，錢適足。賣羊六、豕八，以買五牛，錢不足六百。問︰牛、羊、豕價各幾何？
術曰：如方程，置牛二、羊五正，豕一十三負，餘錢數正；次牛三正，羊九負，豕三正；次牛五負，羊六正，豕八正，不足錢負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛價 a ，羊價 b ，豕價 c 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining the prices of cows, sheep, and pigs based on three transactions. Let's solve it step by step using Python and linear algebra.

### Problem Restatement:
We are given three equations based on the transactions:
1. Selling 2 cows and 5 sheep can buy 13 pigs, with 1000 money left over.
2. Selling 3 cows and 3 pigs can buy 9 sheep, with no money left over.
3. Selling 6 sheep and 8 pigs can buy 5 cows, but 600 money is still needed.

Let the price of a cow be `a`, the price of a sheep be `b`, and the price of a pig be `c`. We need to solve for `a`, `b`, and `c`.

### Equations:
From the problem, we can write the equations as:
1. \( 2a + 5b - 13c = 1000 \)
2. \( 3a - 9b + 3c = 0 \)
3. \( -5a + 6b + 8c = -600 \)

This forms a system of linear equations.

---

### Python Code Solution:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the prices of cow, sheep, and pig
a, b, c = symbols('a b c')

# Define the equations
eq1 = Eq(2 * a + 5 * b - 13 * c, 1000)  # 2a + 5b - 13c = 1000
eq2 = Eq(3 * a - 9 * b + 3 * c, 0)      # 3a - 9b + 3c = 0
eq3 = Eq(-5 * a + 6 * b + 8 * c, -600)  # -5a + 6b + 8c = -600

# Solve the system of equations
solution = solve((eq1, eq2, eq3), (a, b, c))

# Extract the results
牛價 = solution[a]
羊價 = solution[b]
豕價 = solution[c]

# Print the results
print(f"牛價 (Cow price): {牛價}")
print(f"羊價 (Sheep price): {羊價}")
print(f"豕價 (Pig price): {豕價}")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `a`, `b`, and `c` to represent the prices of cows, sheep, and pigs, respectively.
2. **Define Equations**: The three equations are written using `Eq` from the `sympy` library.
3. **Solve the System**: The `solve` function is used to solve the system of linear equations.
4. **Output the Results**: The solution is printed, showing the prices of cows, sheep, and pigs.

---

### Expected Output:
The solution will provide the values of \( a \), \( b \), and \( c \), which are the prices of cows, sheep, and pigs, respectively.

For example:
```
牛價 (Cow price): 500
羊價 (Sheep price): 200
豕價 (Pig price): 100
```

This is just an example output. The actual values will depend on solving the equations.
"""


"""
Variable 'a' has wrong value. Expected: 1200, Actual: a
Variable 'b' has wrong value. Expected: 500, Actual: b
Variable 'c' has wrong value. Expected: 300, Actual: c"""
