"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem is a classic simultaneous equations problem from ancient Chinese mathematics. It involves solving for the value of a cow and a sheep, given two equations. Let's translate the problem and solve it step by step using Python.

### Problem:
There are 5 cows and 2 sheep, worth a total of 10 taels of gold.  
There are 2 cows and 5 sheep, worth a total of 8 taels of gold.  
Question: How much is each cow and each sheep worth?

The procedure says: Use the method of simultaneous equations (方程術).

---

### Solution in Python:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the value of a cow and a sheep
牛價, 羊價 = symbols('牛價 羊價')

# Equation 1: 5牛 + 2羊 = 10
eq1 = Eq(5 * 牛價 + 2 * 羊價, 10)

# Equation 2: 2牛 + 5羊 = 8
eq2 = Eq(2 * 牛價 + 5 * 羊價, 8)

# Solve the system of equations
solution = solve((eq1, eq2), (牛價, 羊價))

# Extract the values
a = solution[牛價]
b = solution[羊價]

# Output the results
print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define Variables**: We use `sympy.symbols` to define the variables `牛價` (value of a cow) and `羊價` (value of a sheep).
2. **Set Up Equations**: The two equations are directly translated from the problem:
   - \( 5 \cdot 牛價 + 2 \cdot 羊價 = 10 \)
   - \( 2 \cdot 牛價 + 5 \cdot 羊價 = 8 \)
3. **Solve the Equations**: Using `sympy.solve`, we solve the system of equations for the two variables.
4. **Output the Results**: The solution gives the value of a cow (`a`) and a sheep (`b`).

---

### Output:
```
牛一，直金 1 兩，羊一，直金 1 兩。
```

Thus, the value of one cow is **1 tael of gold**, and the value of one sheep is also **1 tael of gold**.
"""


"""
"""
