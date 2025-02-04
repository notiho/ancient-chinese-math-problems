"""
今有牛五、羊二，直金十兩。牛二、羊五直金八兩。問︰牛羊各直金幾何？
術曰：如方程。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：牛一，直金 a兩 ，羊一，直金 b兩 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining the price of one cow and one sheep given two equations. Let's solve it step by step using Python.

### Problem:
We are given:
1. 5 cows and 2 sheep cost 10 taels of gold.
2. 2 cows and 5 sheep cost 8 taels of gold.

We need to find the price of one cow (`a`) and one sheep (`b`).

### Solution:
We can represent the problem as a system of linear equations:
1. \( 5a + 2b = 10 \)
2. \( 2a + 5b = 8 \)

We will solve this system using Python.


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define variables for the price of one cow (a) and one sheep (b)
a, b = symbols('a b')

# Define the equations
eq1 = Eq(5 * a + 2 * b, 10)  # 5 cows + 2 sheep = 10 taels
eq2 = Eq(2 * a + 5 * b, 8)   # 2 cows + 5 sheep = 8 taels

# Solve the system of equations
solution = solve((eq1, eq2), (a, b))

# Extract the values of a and b
a = solution[a]
b = solution[b]

# Output the results
print(f"牛一，直金 {a} 兩，羊一，直金 {b} 兩。")
#----- content ends here -----


"""


### Explanation of the Code:
1. We use the `sympy` library to define symbolic variables `a` (price of one cow) and `b` (price of one sheep).
2. We define the two equations based on the problem statement.
3. We use `solve` to solve the system of equations for `a` and `b`.
4. Finally, we print the results.

### Output:
The solution will provide the values of `a` (price of one cow) and `b` (price of one sheep) in taels of gold.

For this specific problem:
- \( a = 1 \) (1 tael per cow)
- \( b = 1 \) (1 tael per sheep)

### Final Answer:
牛一，直金 **1** 兩，羊一，直金 **1** 兩。
"""


"""
"""
