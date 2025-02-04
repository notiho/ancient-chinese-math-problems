"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves two unknowns (the amount of money held by甲 and乙), and we will solve it using the described method, which is essentially a system of linear equations.

### Problem Setup:
Let:
- `甲 = x` (the amount of money甲 holds)
- `乙 = y` (the amount of money乙 holds)

The problem gives us two equations:
1. \( x + \frac{y}{2} = 50 \)
2. \( y + \frac{3x}{2} = 50 \)

We will solve this system of equations step by step using the described ancient method.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the equations
# Equation 1: x + y/2 = 50
# Equation 2: y + 3x/2 = 50

# Step 2: Represent the coefficients of the equations
# Coefficients for Equation 1: x + y/2 = 50
a1 = 1  # Coefficient of x in Equation 1
b1 = Fraction(1, 2)  # Coefficient of y in Equation 1
c1 = 50  # Constant term in Equation 1

# Coefficients for Equation 2: y + 3x/2 = 50
a2 = Fraction(3, 2)  # Coefficient of x in Equation 2
b2 = 1  # Coefficient of y in Equation 2
c2 = 50  # Constant term in Equation 2

# Step 3: Solve for x and y using elimination
# Multiply Equation 1 by 2 to eliminate fractions
a1_new = a1 * 2
b1_new = b1 * 2
c1_new = c1 * 2

# Equation 1 becomes: 2x + y = 100
# Coefficients: a1_new = 2, b1_new = 1, c1_new = 100

# Multiply Equation 2 by 2 to eliminate fractions
a2_new = a2 * 2
b2_new = b2 * 2
c2_new = c2 * 2

# Equation 2 becomes: 3x + 2y = 100
# Coefficients: a2_new = 3, b2_new = 2, c2_new = 100

# Step 4: Eliminate y by multiplying and subtracting equations
# Multiply Equation 1 by 2 and Equation 2 by 1
a1_final = a1_new * 2
b1_final = b1_new * 2
c1_final = c1_new * 2

a2_final = a2_new * 1
b2_final = b2_new * 1
c2_final = c2_new * 1

# Subtract the two equations: (4x + 2y) - (3x + 2y) = 200 - 100
x_coefficient = a1_final - a2_final
y_coefficient = b1_final - b2_final
constant = c1_final - c2_final

# This simplifies to: x = 100
x = Fraction(constant, x_coefficient)

# Step 5: Substitute x back into one of the original equations to solve for y
# Using Equation 1: x + y/2 = 50
y = Fraction(c1 - a1 * x, b1)

# Step 6: Output the results
a = x
b = y

print(f"甲持 {a} 錢 ，乙持 {b} 錢 。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Define the equations**: The two equations are derived from the problem statement.
2. **Eliminate fractions**: Both equations are multiplied by 2 to eliminate fractions for easier manipulation.
3. **Eliminate one variable**: Using the elimination method, we eliminate \( y \) to solve for \( x \).
4. **Substitute back**: Once \( x \) is found, it is substituted back into one of the original equations to solve for \( y \).
5. **Output the results**: The final values of \( x \) (甲's money) and \( y \) (乙's money) are printed.

---

### Answer:
The solution will output the values of \( a \) (甲's money) and \( b \) (乙's money) in terms of fractions or integers, depending on the result of the calculations.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
