"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of matrix elimination or Gaussian elimination. Let's translate the problem and solve it step by step using Python.

### Problem Breakdown:
1. **Given:**
   - The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
   - The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.

2. **Unknowns:**
   - Let `x` represent the price of a horse (in qian).
   - Let `y` represent the price of a cow (in qian).

3. **Equations:**
   - \( 2x + y = 10000 + \frac{1}{2}x \)
   - \( x + 2y = 10000 - \frac{1}{2}y \)

4. **Simplify the equations:**
   - From the first equation: \( 2x + y - \frac{1}{2}x = 10000 \) → \( \frac{3}{2}x + y = 10000 \)
   - From the second equation: \( x + 2y + \frac{1}{2}y = 10000 \) → \( x + \frac{5}{2}y = 10000 \)

5. **Solve the system of equations using the fangcheng method.**

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# Equation 1: (3/2)x + y = 10000
# Equation 2: x + (5/2)y = 10000

# Coefficients of the equations
# Representing the system as:
# a1 * x + b1 * y = c1
# a2 * x + b2 * y = c2
a1, b1, c1 = Fraction(3, 2), 1, 10000
a2, b2, c2 = 1, Fraction(5, 2), 10000

# Step 1: Eliminate x from the second equation
# Multiply the first equation by 2 to eliminate fractions
a1, b1, c1 = 3, 2, 20000

# Multiply the second equation by 3 to align coefficients of x
a2, b2, c2 = 3, Fraction(15, 2), 30000

# Subtract the first equation from the second to eliminate x
# (a2 - a1) * x + (b2 - b1) * y = c2 - c1
b_new = b2 - b1  # Coefficient of y
c_new = c2 - c1  # Constant term

# Solve for y
y = c_new / b_new

# Substitute y back into the first equation to solve for x
x = (c1 - b1 * y) / a1

# Results
a = x  # Price of a horse
b = y  # Price of a cow

print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Equations Setup:**
   - The two equations are represented in the form \( ax + by = c \).
   - Fractions are used to handle the coefficients accurately.

2. **Elimination:**
   - The first equation is scaled to eliminate fractions.
   - The second equation is scaled to align the coefficients of \( x \).
   - Subtraction is used to eliminate \( x \), leaving a single equation in terms of \( y \).

3. **Back Substitution:**
   - Once \( y \) (the price of a cow) is found, it is substituted back into one of the original equations to solve for \( x \) (the price of a horse).

4. **Output:**
   - The prices of the horse and cow are printed as fractions for exact values.

---

### Answer:
The output will provide the exact prices of the horse and cow in qian.
"""


"""
"""
