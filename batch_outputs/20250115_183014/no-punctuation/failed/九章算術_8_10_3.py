"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰馬價 a錢 牛價 b錢 
"""

"""
This is a classic simultaneous equations problem solved using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving systems of linear equations. Let's break it down step by step and translate it into Python code.

The problem states:
- The price of 2 horses and 1 cow exceeds 10,000 by an unknown amount.
- The price of 1 horse and 2 cows is less than 10,000 by an unknown amount.
- We are tasked with finding the price of a horse and a cow.

The procedure (術) describes how to solve this using the fangcheng method, which involves setting up a system of equations and solving it step by step.

### Equations:
1. \( 2x + y = 10000 + z \)  (price of 2 horses and 1 cow exceeds 10,000 by \( z \))
2. \( x + 2y = 10000 - w \)  (price of 1 horse and 2 cows is less than 10,000 by \( w \))

Where:
- \( x \) is the price of a horse,
- \( y \) is the price of a cow,
- \( z \) and \( w \) are unknown adjustments.

We aim to solve for \( x \) (horse price) and \( y \) (cow price).

---

### Python Code Implementation:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations
# Equation 1: 2x + y = 10000 + z
# Equation 2: x + 2y = 10000 - w

# Coefficients for the equations
coefficients = [
    [2, 1, 1],  # Coefficients for x, y, z in the first equation
    [1, 2, -1]  # Coefficients for x, y, w in the second equation
]

# Constants on the right-hand side of the equations
constants = [10000, 10000]

# Step 2: Solve using the fangcheng method
# Place the coefficients and constants into a matrix-like structure
# Using the ancient method, we eliminate variables step by step

# Eliminate z and w to solve for x and y
# Multiply the first equation by 2 (to align y coefficients)
row1 = [coefficients[0][0] * 2, coefficients[0][1] * 2, coefficients[0][2] * 2, constants[0] * 2]
row2 = [coefficients[1][0], coefficients[1][1], coefficients[1][2], constants[1]]

# Subtract the second equation from the first
eliminated_row = [
    row1[0] - row2[0],  # x coefficient
    row1[1] - row2[1],  # y coefficient
    row1[2] - row2[2],  # z/w coefficient
    row1[3] - row2[3]   # constant
]

# Now we have a single equation in terms of x and y
# Solve for y in terms of x
x_coefficient = eliminated_row[0]
y_coefficient = eliminated_row[1]
constant = eliminated_row[3]

# y = (constant - x_coefficient * x) / y_coefficient
# Substitute back to find x and y

# Step 3: Solve for x and y
# Assume z = w = 0 for simplicity (as they cancel out in the subtraction)
y = Fraction(constant, y_coefficient)
x = Fraction(constants[0] - coefficients[0][1] * y, coefficients[0][0])

# Step 4: Output the results
a = x  # Price of a horse
b = y  # Price of a cow

print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")


"""


---

### Explanation of the Code:
1. **Setup the equations**: The coefficients of \( x \), \( y \), and the constants are placed into a matrix-like structure.
2. **Eliminate variables**: Using the fangcheng method, we eliminate \( z \) and \( w \) by aligning coefficients and subtracting equations.
3. **Solve for \( x \) and \( y \)**: After elimination, we solve for \( y \) in terms of \( x \), then substitute back to find \( x \).
4. **Output the results**: The prices of the horse (\( a \)) and cow (\( b \)) are printed.

This code adheres to the ancient procedure while using modern Python constructs for clarity.
"""


"""
Code error: Fraction(10000, 0)"""
