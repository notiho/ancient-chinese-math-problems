"""
今有上禾六秉損實一斗八升當下禾一十秉下禾十五秉損實五升當上禾五秉問上下禾實一秉各幾何
術曰如方程置上禾六秉正下禾一十秉負損實一斗八升正次置上禾五秉負下禾一十五秉正損實五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉實 a升 下禾一秉實 b升 
"""

#----- content starts here -----
"""
Suppose there are 6 sheaves of superior grain, with a loss of 1 dou and 8 sheng in total. 
This corresponds to 10 sheaves of inferior grain. 
There are also 15 sheaves of inferior grain, with a loss of 5 sheng in total. 
This corresponds to 5 sheaves of superior grain. 
Question: what is the yield per sheaf of superior grain and inferior grain?

The procedure says: Treat it as a system of equations. 
Set 6 sheaves of superior grain as positive, and 10 sheaves of inferior grain as negative, with the loss of 1 dou and 8 sheng as positive. 
Next, set 5 sheaves of superior grain as negative, and 15 sheaves of inferior grain as positive, with the loss of 5 sheng as positive. 
Use the method of positive and negative to solve.

The method for solving systems of equations says: 
Set 3 sheaves of superior grain, 2 sheaves of middle grain, and 1 sheaf of inferior grain, with a total yield of 39 dou on the right side. 
Arrange the left side as the right side. 
Use the right row to multiply the superior grain row, and divide directly. 
Then multiply the next row and also divide directly. 
For the middle row, multiply the middle grain row by the left row and divide directly. 
For the left side, if the inferior grain row is not exhausted, use the superior grain as the divisor and the inferior grain as the dividend. 
The result is the yield of the inferior grain. 
To find the middle grain, multiply the middle row by the divisor and divide by the inferior grain yield. 
The remainder corresponds to the middle grain sheaf count plus one. 
To find the superior grain, multiply the right row by the divisor and divide by the yields of the inferior and middle grains. 
The remainder corresponds to the superior grain sheaf count plus one. 
The yields are obtained according to the method, each yielding 1 dou.

Answer: the yield per sheaf of superior grain is *a* sheng, and the yield per sheaf of inferior grain is *b* sheng.
"""

# 上禾六秉損實一斗八升
上禾_秉1 = 6
上禾_損實1 = 1 * 10 + 8  # Convert 1 dou 8 sheng to sheng

# 下禾一十秉
下禾_秉1 = 10

# 下禾十五秉損實五升
下禾_秉2 = 15
下禾_損實2 = 5  # Already in sheng

# 上禾五秉
上禾_秉2 = 5

# Solve using the system of equations:
# Equation 1: 6 * 上禾 - 10 * 下禾 = 1斗8升
# Equation 2: -5 * 上禾 + 15 * 下禾 = 5升

# Step 1: Eliminate one variable (e.g., 上禾)
# Multiply Equation 1 by 5 and Equation 2 by 6 to align coefficients of 上禾
eq1_multiplied = (5 * 上禾_秉1, -5 * 下禾_秉1, 5 * 上禾_損實1)
eq2_multiplied = (-6 * 上禾_秉2, 6 * 下禾_秉2, 6 * 下禾_損實2)

# Add the two equations to eliminate 上禾
combined_秉 = eq1_multiplied[1] + eq2_multiplied[1]
combined_損實 = eq1_multiplied[2] + eq2_multiplied[2]

# Solve for 下禾
下禾 = Fraction(combined_損實, combined_秉)

# Substitute 下禾 back into one of the original equations to solve for 上禾
上禾 = Fraction(上禾_損實1 + 下禾_秉1 * 下禾, 上禾_秉1)

# Convert yields to sheng
a = 上禾  # Yield per sheaf of superior grain in sheng
b = 下禾  # Yield per sheaf of inferior grain in sheng#----- content ends here -----

"""
"""
