"""
今有上禾五秉損實一斗一升當下禾七秉上禾七秉損實二斗五升當下禾五秉問上下禾實一秉各幾何
術曰如方程置上禾五秉正下禾七秉負損實一斗一升正次置上禾七秉正下禾五秉負損實二斗五升正以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰上禾一秉 a升 下禾一秉 b升 
"""

#----- content starts here -----
"""
Suppose there are 5 bundles of upper millet, which lose 1 dou and 1 sheng in weight. 
This corresponds to 7 bundles of lower millet. 
Then, there are 7 bundles of upper millet, which lose 2 dou and 5 sheng in weight. 
This corresponds to 5 bundles of lower millet.
Question: how much does one bundle of upper millet and one bundle of lower millet weigh?

The procedure says: Treat it as a system of linear equations. 
Set 5 bundles of upper millet as positive, 7 bundles of lower millet as negative, and the loss of 1 dou and 1 sheng as positive. 
Next, set 7 bundles of upper millet as positive, 5 bundles of lower millet as negative, and the loss of 2 dou and 5 sheng as positive. 
Use the positive-negative method to solve.

The method for solving systems of equations says: Place the coefficients of the upper millet, middle millet, and lower millet, along with the total weight, on the right side. 
Arrange the left side similarly. 
Use the right row to multiply the upper millet row, dividing directly. 
Repeat for the next row, dividing directly again. 
For the middle millet row, multiply by the left row and divide directly. 
For the lower millet row, if there is a remainder, use the upper millet as the divisor and the lower millet as the dividend. 
The result is the weight of the lower millet. 
To find the middle millet, multiply the middle row by the divisor and divide by the lower millet's weight. 
The remainder corresponds to the middle millet's weight. 
To find the upper millet, multiply the right row by the divisor and divide by the weights of the lower and middle millet. 
The remainder corresponds to the upper millet's weight. 
The results are obtained as described, and each is 1 dou.

Answer: one bundle of upper millet weighs *a* sheng, and one bundle of lower millet weighs *b* sheng.
"""

# Convert dou and sheng to a consistent unit (sheng)
# 1 dou = 10 sheng

# First equation: 5 bundles of upper millet, 7 bundles of lower millet, loss of 1 dou 1 sheng
上禾1 = 5
下禾1 = -7
損實1 = 1 * 10 + 1  # Convert to sheng

# Second equation: 7 bundles of upper millet, 5 bundles of lower millet, loss of 2 dou 5 sheng
上禾2 = 7
下禾2 = -5
損實2 = 2 * 10 + 5  # Convert to sheng

# Solve using elimination
# Multiply the first equation by 7 and the second equation by 5 to align the coefficients of 上禾
eq1 = (上禾1 * 7, 下禾1 * 7, 損實1 * 7)
eq2 = (上禾2 * 5, 下禾2 * 5, 損實2 * 5)

# Subtract the second equation from the first to eliminate 上禾
下禾系數 = eq1[1] - eq2[1]
損實差 = eq1[2] - eq2[2]

# Solve for 下禾 (one bundle of lower millet)
b = Fraction(損實差, 下禾系數)

# Substitute b back into the first equation to solve for 上禾 (one bundle of upper millet)
損實1_adjusted = 損實1 - (下禾1 * b)
a = Fraction(損實1_adjusted, 上禾1)

# Results
a  # Weight of one bundle of upper millet in sheng
b  # Weight of one bundle of lower millet in sheng#----- content ends here -----

"""
"""
