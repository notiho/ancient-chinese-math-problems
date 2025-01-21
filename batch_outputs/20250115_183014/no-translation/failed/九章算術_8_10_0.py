"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the method described in the "方程術" (method of simultaneous equations). Here's the Python implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2馬 + 1牛 = 10000 + 1/2馬
# 1馬 + 2牛 = 10000 - 1/2牛

# Step 1: Rewrite the equations in standard form:
# (1) 4馬 + 2牛 = 20000  (Multiply the first equation by 2 to eliminate the fraction)
# (2) 2馬 + 4牛 = 20000  (Multiply the second equation by 2 to eliminate the fraction)

# Step 2: Represent the equations as a system of linear equations:
# Let 馬 = x and 牛 = y
# 4x + 2y = 20000
# 2x + 4y = 20000

# Step 3: Solve using the method described in the "方程術":
# Initialize the coefficients and constants
a1, b1, c1 = 4, 2, 20000  # Coefficients and constant for the first equation
a2, b2, c2 = 2, 4, 20000  # Coefficients and constant for the second equation

# Eliminate one variable (e.g., y) using the first equation:
# Multiply the first equation by b2 and the second equation by b1
# Then subtract to eliminate y
factor1 = b2
factor2 = b1
new_a = a1 * factor1 - a2 * factor2
new_c = c1 * factor1 - c2 * factor2

# Solve for x (馬)
x = Fraction(new_c, new_a)

# Substitute x back into one of the original equations to solve for y (牛)
y = Fraction(c1 - a1 * x, b1)

# Results
a = x  # 馬價
b = y  # 牛價

# Output the results
a, b


"""


### Explanation of the Code:
1. The problem is translated into a system of linear equations.
2. The equations are manipulated to eliminate one variable using the method described in the "方程術."
3. The remaining variable is solved, and the value is substituted back to find the other variable.
4. The results are expressed as fractions to maintain precision, as per the ancient method.

### Final Answer:
- `a` (馬價): The price of a horse in 錢.
- `b` (牛價): The price of a cow in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 10000/3
Variable 'b' has wrong value. Expected: 20000/11, Actual: 10000/3"""
