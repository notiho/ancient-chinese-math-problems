"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem is essentially a system of two linear equations, and the "方程術" (method of equations) provides a structured way to solve it.

The equations derived from the problem are:
1. \( \text{甲} + \frac{\text{乙}}{2} = 50 \)
2. \( \text{乙} + \frac{3\text{甲}}{2} = 50 \)

We will solve this using the described method.


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the coefficients and constants from the equations
# Equation 1: 甲 + 乙/2 = 50
# Equation 2: 乙 + 3甲/2 = 50

# Coefficients for the equations
上禾 = [1, Fraction(1, 2)]  # Coefficients of 甲 and 乙 in the first equation
中禾 = [Fraction(3, 2), 1]  # Coefficients of 甲 and 乙 in the second equation
下禾 = [50, 50]            # Constants on the right-hand side of the equations

# Step 2: Solve for 甲 and 乙 using the 方程術
# Multiply the first equation by the coefficient of 乙 in the second equation (1)
# Multiply the second equation by the coefficient of 乙 in the first equation (1/2)
# Subtract the two equations to eliminate 乙

# Adjust the equations
上禾 = [coeff * 中禾[1] for coeff in 上禾]  # Multiply the first equation by 1
中禾 = [coeff * 上禾[1] for coeff in 中禾]  # Multiply the second equation by 1/2

# Subtract the adjusted equations
甲_coeff = 上禾[0] - 中禾[0]  # Coefficient of 甲
constant = 下禾[0] * 中禾[1] - 下禾[1] * 上禾[1]  # Constant term

# Solve for 甲
甲 = Fraction(constant, 甲_coeff)

# Substitute 甲 back into the first equation to solve for 乙
乙 = Fraction(下禾[0] - 上禾[0] * 甲, 上禾[1])

# Results
a = 甲
b = 乙

# Output the results
print(f"甲持 {a} 錢，乙持 {b} 錢。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Define the coefficients and constants**: The coefficients of \( \text{甲} \) and \( \text{乙} \) in each equation are extracted, along with the constants on the right-hand side.
2. **Adjust the equations**: The equations are adjusted to eliminate one variable (\( \text{乙} \)) by multiplying each equation by the appropriate coefficient.
3. **Solve for \( \text{甲} \)**: After eliminating \( \text{乙} \), the resulting equation is solved for \( \text{甲} \).
4. **Solve for \( \text{乙} \)**: The value of \( \text{甲} \) is substituted back into one of the original equations to solve for \( \text{乙} \).
5. **Output the results**: The values of \( \text{甲} \) and \( \text{乙} \) are printed.

### Final Answer:
The values of \( \text{甲} \) and \( \text{乙} \) are stored in `a` and `b`, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 0
Variable 'b' has wrong value. Expected: 25, Actual: 100"""
