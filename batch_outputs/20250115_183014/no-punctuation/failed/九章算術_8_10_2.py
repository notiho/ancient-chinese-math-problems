"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰馬價 a錢 牛價 b錢 
"""

This is a classic simultaneous equations problem from ancient Chinese mathematics, solved using the method of "fangcheng" (early matrix-like method). Let's break it down step by step and encode it into Python.

The problem is as follows:

"""
Suppose there are two horses and one cow, and their total price exceeds 10,000 qian.
If the price of half a horse is added to the price of one horse and two cows, the total price is less than 10,000 qian.
Question: What are the prices of a horse and a cow?

The procedure says: Use the method of "fangcheng" (simultaneous equations) and "loss and gain" (adjustments).
The method of "fangcheng" says:
1. Place the coefficients of the unknowns (horses and cows) in rows, with their respective totals on the right side.
2. Multiply the top row by the middle row and divide by the diagonal coefficient, then adjust accordingly.
3. Continue this process for the middle and bottom rows.
4. Solve for the unknowns step by step, starting from the bottom row.

Answer: The price of a horse is *a* qian, and the price of a cow is *b* qian.
"""

from fractions import Fraction

# Coefficients of the equations:
# 2 horses + 1 cow = 10,000 qian
# 1/2 horse + 1 horse + 2 cows = 10,000 qian

# Representing the equations in matrix form:
# Row 1: 2x + 1y = 10,000
# Row 2: (1/2)x + 1x + 2y = 10,000
# Simplify Row 2: (3/2)x + 2y = 10,000

# Initialize the matrix (coefficients and constants)
# Each row is [coefficient of x, coefficient of y, constant]
matrix = [
    [2, 1, 10000],  # Row 1
    [Fraction(3, 2), 2, 10000]  # Row 2
]

# Step 1: Eliminate the x term from Row 2 by scaling and subtracting
# Multiply Row 1 by (3/2) and subtract from Row 2
scale_factor = Fraction(3, 2)
matrix[1] = [
    matrix[1][0] - scale_factor * matrix[0][0],  # Coefficient of x
    matrix[1][1] - scale_factor * matrix[0][1],  # Coefficient of y
    matrix[1][2] - scale_factor * matrix[0][2]   # Constant
]

# Step 2: Solve for y (price of a cow)
# Row 2 is now in the form [0, coefficient of y, constant]
b = matrix[1][2] / matrix[1][1]

# Step 3: Solve for x (price of a horse)
# Substitute y into Row 1
a = (matrix[0][2] - matrix[0][1] * b) / matrix[0][0]

# Output the results
a = float(a)
b = float(b)
a, b
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
