"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics. The problem involves determining the price of a horse and a cow based on the given relationships. Let's solve it step by step using Python.

### Problem Breakdown:
1. **Given:**
   - The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
   - The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.

2. **Unknowns:**
   - Let the price of a horse be `x` (in qian).
   - Let the price of a cow be `y` (in qian).

3. **Equations:**
   - \( 2x + y = 10000 + \frac{x}{2} \)
   - \( x + 2y = 10000 - \frac{y}{2} \)

4. **Simplify the equations:**
   - From the first equation:
     \( 2x + y - \frac{x}{2} = 10000 \)
     Multiply through by 2 to eliminate the fraction:
     \( 4x + 2y - x = 20000 \)
     \( 3x + 2y = 20000 \)  (Equation 1)

   - From the second equation:
     \( x + 2y + \frac{y}{2} = 10000 \)
     Multiply through by 2 to eliminate the fraction:
     \( 2x + 4y + y = 20000 \)
     \( 2x + 5y = 20000 \)  (Equation 2)

5. **Solve the system of equations:**
   - \( 3x + 2y = 20000 \)
   - \( 2x + 5y = 20000 \)

### Python Code:


"""

#----- content starts here -----

from sympy import symbols, Eq, solve

# Define the variables
x, y = symbols('x y')  # x: price of a horse, y: price of a cow

# Define the equations
eq1 = Eq(3 * x + 2 * y, 20000)  # 3x + 2y = 20000
eq2 = Eq(2 * x + 5 * y, 20000)  # 2x + 5y = 20000

# Solve the system of equations
solution = solve((eq1, eq2), (x, y))

# Extract the solutions
a = solution[x]  # Price of a horse
b = solution[y]  # Price of a cow

# Print the results
print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")
#----- content ends here -----


"""


### Explanation of the Code:
1. We use the `sympy` library to symbolically define the variables `x` (price of a horse) and `y` (price of a cow).
2. The two equations are defined based on the simplified relationships derived above.
3. The `solve` function is used to solve the system of linear equations.
4. The solution is extracted and printed.

### Output:
The solution will provide the values of `a` (price of a horse) and `b` (price of a cow) in qian.
"""


"""
"""
