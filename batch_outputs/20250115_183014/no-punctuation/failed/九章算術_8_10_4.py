"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰馬價 a錢 牛價 b錢 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "fangcheng" (方程), which is an early form of solving simultaneous equations. Let's translate the problem into Python code step by step.

The problem states:

"""
Suppose there are two horses and one ox, and their total price exceeds 10,000. If the price of half a horse is added to the price of one horse and two oxen, the total price is less than 10,000. If the price of half an ox is added, what are the prices of the horse and the ox?

The procedure says: Use the method of "fangcheng" (simultaneous equations) and "sunyi" (adjustment).

The "fangcheng" procedure says: Place the coefficients of the variables (horses and oxen) in rows. For the first row, place the coefficients of the first equation. For the second row, place the coefficients of the second equation, and so on. Place the constants (the totals) on the right side. Then, perform elimination by multiplying and dividing rows as needed to isolate each variable.

Answer: The price of a horse is *a* qian, and the price of an ox is *b* qian.
"""


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 2 horses + 1 ox = 10000
# Equation 2: (1/2 horse) + 1 horse + 2 oxen = 10000
coefficients = [
    [2, 1, 10000],  # Row for the first equation
    [Fraction(1, 2) + 1, 2, 10000]  # Row for the second equation
]

# Step 1: Eliminate the first variable (horse) from the second equation
# Multiply the first row by (1/2 + 1) and subtract from the second row
factor = coefficients[1][0] / coefficients[0][0]
coefficients[1] = [
    coefficients[1][i] - factor * coefficients[0][i]
    for i in range(len(coefficients[0]))
]

# Step 2: Solve for the second variable (ox)
b = coefficients[1][2] / coefficients[1][1]

# Step 3: Solve for the first variable (horse)
a = (coefficients[0][2] - coefficients[0][1] * b) / coefficients[0][0]

# Output the results
a, b


"""

"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 4000
Variable 'b' has wrong value. Expected: 20000/11, Actual: 2000"""
