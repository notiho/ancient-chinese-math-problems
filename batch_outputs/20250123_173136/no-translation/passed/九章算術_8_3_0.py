"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
To solve this problem using the described "方程術" (method of simultaneous equations), we need to translate the ancient procedure into Python code. Here's the step-by-step implementation:


"""


from fractions import Fraction

# Problem setup
# First equation: 上禾 5秉 - 下禾 7秉 = 1斗1升
# Second equation: 上禾 7秉 - 下禾 5秉 = 2斗5升

# Convert all units to 升 (1斗 = 10升)
eq1_constant = 1 * 10 + 1  # 1斗1升 = 11升
eq2_constant = 2 * 10 + 5  # 2斗5升 = 25升

# Coefficients for the equations
# Equation 1: 5上禾 - 7下禾 = 11
# Equation 2: 7上禾 - 5下禾 = 25
coefficients = [
    [5, -7, eq1_constant],  # [5, -7, 11]
    [7, -5, eq2_constant],  # [7, -5, 25]
]

# Solve using elimination method
# Multiply the first equation by 7 and the second equation by 5 to align the coefficients of 上禾
eq1_scaled = [7 * x for x in coefficients[0]]  # [35, -49, 77]
eq2_scaled = [5 * x for x in coefficients[1]]  # [35, -25, 125]

# Subtract the first scaled equation from the second to eliminate 上禾
# (35上禾 - 35上禾) + (-25下禾 - -49下禾) = 125 - 77
# 24下禾 = 48
下禾_value = Fraction(125 - 77, -25 + 49)  # 下禾 = 48 / 24 = 2升

# Substitute 下禾_value back into the first equation to solve for 上禾
# 5上禾 - 7下禾 = 11
# 5上禾 - 7(2) = 11
# 5上禾 = 11 + 14
# 5上禾 = 25
上禾_value = Fraction(11 + 14, 5)  # 上禾 = 25 / 5 = 5升

# Results
a = 上禾_value  # 上禾一秉 = 5升
b = 下禾_value  # 下禾一秉 = 2升

# Output the results
print(f"上禾一秉 {a}升 ，下禾一秉 {b}升 。")


"""


### Explanation of the Code:
1. **Convert Units**: The constants in the equations are converted from 斗 and 升 to just 升 for consistency.
2. **Set Up Equations**: The coefficients of the equations are represented as lists.
3. **Elimination Method**: The equations are solved using the elimination method, as described in the "方程術".
4. **Fraction Class**: The `Fraction` class ensures that all calculations are exact and results are in fractional form if necessary.
5. **Results**: The values of `上禾` and `下禾` per 秉 are calculated and displayed.

### Answer:
```
上禾一秉 5升 ，下禾一秉 2升 。
```
"""


"""
"""
