"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰馬價 a錢 牛價 b錢 
"""

"""
Suppose there are two horses and one ox, and their total price exceeds 10,000 qian.
If the price of half a horse is added to the price of one horse and two oxen, the total price is less than 10,000 qian.
If the price of half an ox is added, what are the prices of the ox and the horse?

The procedure says: Solve using the method of simultaneous equations and the method of balancing losses and gains.

The procedure for simultaneous equations says:
1. Place the coefficients of the unknowns (upper, middle, and lower grains) and the constants on the right-hand side.
2. Multiply the upper row by the middle row, dividing by the diagonal coefficient, and repeat for the next row.
3. For the middle row, multiply by the lower row, dividing by the diagonal coefficient.
4. Use the results to back-substitute and solve for the unknowns.

The answer says: the price of a horse is *a* qian, and the price of an ox is *b* qian.
"""

# Define the coefficients and constants for the equations
# Equation 1: 2馬 + 1牛 = 10000
# Equation 2: 1.5馬 + 2牛 = 10000

# Coefficients for the equations
上禾 = [2, 1]  # Coefficients for the first equation
中禾 = [1.5, 2]  # Coefficients for the second equation
下禾 = [0, 0]  # Placeholder for the third row (not used here)

# Constants (right-hand side values)
實 = [10000, 10000]

# Step 1: Normalize the first row
法 = 上禾[0]  # Diagonal coefficient for the first row
上禾 = [Fraction(x, 法) for x in 上禾]
實[0] = Fraction(實[0], 法)

# Step 2: Eliminate the first variable from the second row
法 = 中禾[0]  # Coefficient of the first variable in the second row
中禾 = [中禾[i] - 法 * 上禾[i] for i in range(len(上禾))]
實[1] = 實[1] - 法 * 實[0]

# Step 3: Solve for the second variable
法 = 中禾[1]  # Diagonal coefficient for the second row
中禾 = [Fraction(x, 法) for x in 中禾]
實[1] = Fraction(實[1], 法)

# Step 4: Back-substitute to solve for the first variable
實[0] = 實[0] - 上禾[1] * 實[1]

# Assign the results
a = 實[0]  # Price of a horse
b = 實[1]  # Price of an ox
"""
Code error: both arguments should be Rational instances"""
