"""
今有甲乙二人持錢不知其數甲得乙半而錢五十乙得甲太半而亦錢五十問甲乙持錢各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲持 a錢 乙持 b錢 
"""

"""
Suppose there are two people, Jia and Yi, holding an unknown amount of money.
Jia takes half of Yi's money and has 50 qian.
Yi takes more than half of Jia's money and also has 50 qian.
Question: how much money do Jia and Yi each hold?

The procedure says: Use the method of simultaneous equations ("fangcheng") to solve this.

The method of simultaneous equations says:
1. Place the coefficients of the unknowns (referred to as "he" or "wheat bundles") in rows, with the constants on the right side.
2. Multiply the top row by the coefficients of the middle row, and divide by the diagonal coefficient.
3. Continue this process for the next rows, reducing the system step by step.
4. Solve for the unknowns by back-substitution.

Answer: Jia holds *a* qian, and Yi holds *b* qian.
"""

# Define the coefficients and constants for the simultaneous equations
# Equation 1: Jia + (1/2)Yi = 50
# Equation 2: Yi + (3/2)Jia = 50

# Coefficients for Jia and Yi
coefficients = [
    [1, Fraction(1, 2)],  # Coefficients for the first equation
    [Fraction(3, 2), 1]   # Coefficients for the second equation
]

# Constants on the right-hand side
constants = [50, 50]

# Step 1: Eliminate Jia from the second equation
# Multiply the first equation by 3/2 (to match the coefficient of Jia in the second equation)
row1_scaled = [coefficients[0][0] * Fraction(3, 2), coefficients[0][1] * Fraction(3, 2)]
constant1_scaled = constants[0] * Fraction(3, 2)

# Subtract the scaled first equation from the second equation
row2_new = [coefficients[1][0] - row1_scaled[0], coefficients[1][1] - row1_scaled[1]]
constant2_new = constants[1] - constant1_scaled

# Step 2: Solve for Yi
# The second equation now only involves Yi
Yi = Fraction(constant2_new, row2_new[1])

# Step 3: Solve for Jia
# Substitute Yi back into the first equation
Jia = Fraction(constants[0] - coefficients[0][1] * Yi, coefficients[0][0])

# Final results
a = Jia
b = Yi
"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: -100"""
