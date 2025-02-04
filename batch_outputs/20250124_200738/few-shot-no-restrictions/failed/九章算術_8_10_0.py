"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This is a classic system of linear equations problem from ancient Chinese mathematics, solved using a method similar to Gaussian elimination. Let's break it down step by step and translate it into Python code.

### Problem:
- Two horses and one cow together cost slightly over 10,000, which is equivalent to the price of half a horse.
- One horse and two cows together cost slightly less than 10,000, which is equivalent to the price of half a cow.
- Question: What are the prices of a horse and a cow?

### Solution:
We can represent the problem as a system of two equations:
1. \( 2x + y = 10000 + \frac{x}{2} \)
2. \( x + 2y = 10000 - \frac{y}{2} \)

Where:
- \( x \) is the price of a horse.
- \( y \) is the price of a cow.

Simplify the equations:
1. \( 2x + y - \frac{x}{2} = 10000 \) → \( \frac{4x}{2} + y - \frac{x}{2} = 10000 \) → \( \frac{7x}{2} + y = 10000 \)
2. \( x + 2y + \frac{y}{2} = 10000 \) → \( x + \frac{4y}{2} + \frac{y}{2} = 10000 \) → \( x + \frac{5y}{2} = 10000 \)

Now solve this system of equations using Python.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# Equation 1: (7/2)x + y = 10000
# Equation 2: x + (5/2)y = 10000

# Coefficients of the equations
a1, b1, c1 = Fraction(7, 2), 1, 10000  # (7/2)x + y = 10000
a2, b2, c2 = 1, Fraction(5, 2), 10000  # x + (5/2)y = 10000

# Solve using elimination
# Multiply the first equation by 2 to eliminate fractions
a1, b1, c1 = a1 * 2, b1 * 2, c1 * 2  # 7x + 2y = 20000
# Equation 1 becomes: 7x + 2y = 20000
# Equation 2 remains: x + (5/2)y = 10000

# Eliminate y by multiplying the second equation by 2
a2, b2, c2 = a2 * 2, b2 * 2, c2 * 2  # 2x + 5y = 20000
# Equation 2 becomes: 2x + 5y = 20000

# Subtract the second equation from the first to eliminate y
# (7x + 2y) - (2x + 5y) = 20000 - 20000
a3, b3, c3 = a1 - a2, b1 - b2, c1 - c2  # 5x - 3y = 0
# Equation 3: 5x - 3y = 0

# Solve for x in terms of y
# 5x = 3y → x = (3/5)y
x = Fraction(3, 5) * y

# Substitute x = (3/5)y into one of the original equations to solve for y
# Use Equation 1: 7x + 2y = 20000
# 7((3/5)y) + 2y = 20000
# (21/5)y + 2y = 20000
# (21/5)y + (10/5)y = 20000
# (31/5)y = 20000
y = Fraction(20000, 1) * Fraction(5, 31)  # y = 20000 * (5/31)

# Solve for x using x = (3/5)y
x = Fraction(3, 5) * y

# Convert to integers for final answer
a = x
b = y

# Output the results
print(f"馬價 a = {a} 錢")  # Price of a horse
print(f"牛價 b = {b} 錢")  # Price of a cow
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The system of equations is simplified and represented using fractions to maintain precision.
2. The elimination method is used to solve for one variable in terms of the other.
3. Substitution is used to find the exact values of \( x \) (price of a horse) and \( y \) (price of a cow).
4. The results are printed as fractions for precision.

---

### Final Answer:
The price of a horse (\( a \)) and the price of a cow (\( b \)) will be computed and displayed in terms of "錢".
"""


"""
Code error: name 'y' is not defined"""
