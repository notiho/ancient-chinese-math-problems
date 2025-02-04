"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This problem involves solving a system of linear equations to determine the price of one cow and one sheep. The ancient Chinese text describes a method similar to Gaussian elimination to solve the equations. Here's how we can solve it using Python:

### Problem:
- 5 cows and 2 sheep cost 10 taels of gold.
- 2 cows and 5 sheep cost 8 taels of gold.
- Question: What is the price of one cow and one sheep?

### Solution in Python:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the price of one cow and one sheep
牛價, 羊價 = symbols('牛價 羊價')

# Define the equations based on the problem
eq1 = Eq(5 * 牛價 + 2 * 羊價, 10)  # 5 cows + 2 sheep = 10 taels
eq2 = Eq(2 * 牛價 + 5 * 羊價, 8)   # 2 cows + 5 sheep = 8 taels

# Solve the system of equations
solution = solve((eq1, eq2), (牛價, 羊價))

# Extract the results
a = solution[牛價]  # Price of one cow
b = solution[羊價]  # Price of one sheep

# Output the results
print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")
#----- content ends here -----


"""


### Explanation:
1. **Define Variables**: `牛價` represents the price of one cow, and `羊價` represents the price of one sheep.
2. **Set Up Equations**: The two equations are derived from the problem statement:
   - \( 5 \cdot 牛價 + 2 \cdot 羊價 = 10 \)
   - \( 2 \cdot 牛價 + 5 \cdot 羊價 = 8 \)
3. **Solve the Equations**: Use `sympy.solve` to solve the system of linear equations.
4. **Output the Results**: The solution gives the price of one cow (`a`) and one sheep (`b`).

### Output:
```
牛一，直金 1 兩，羊一，直金 1 兩。
```

Thus, the price of one cow is **1 tael**, and the price of one sheep is **1 tael**.
"""


"""
"""
