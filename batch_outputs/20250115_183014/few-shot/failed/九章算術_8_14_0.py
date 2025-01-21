"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This problem involves a system of equations to determine the weight of each type of grain bundle (甲禾, 乙禾, 丙禾). The procedure uses ancient Chinese "方程術" (method of solving systems of linear equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Given data:
# 甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石
甲禾秉數 = 2
乙禾秉數 = 3
丙禾秉數 = 4

# 重量 relationships:
# 甲二重如乙一，乙三重如丙一，丙四重如甲一
甲重 = Fraction(1, 2)  # 甲禾的重量相對於乙禾
乙重 = Fraction(1, 3)  # 乙禾的重量相對於丙禾
丙重 = Fraction(1, 4)  # 丙禾的重量相對於甲禾

# Total weight of all bundles is over 1 石 (assume 1 石 = 10 斗)
總重量 = 39  # in 斗

# Step 1: Set up the equations
# Let x = weight of 甲禾 per 秉
# Let y = weight of 乙禾 per 秉
# Let z = weight of 丙禾 per 秉
# Equations:
# 2x + 3y + 4z = 39
# 2x = y
# 3y = z

# Step 2: Solve the equations
# From 2x = y, we get y = 2x
# From 3y = z, we get z = 3y = 6x
# Substitute y and z into the first equation:
# 2x + 3(2x) + 4(6x) = 39
# 2x + 6x + 24x = 39
# 32x = 39
x = Fraction(39, 32)  # Weight of 甲禾 per 秉
y = 2 * x             # Weight of 乙禾 per 秉
z = 6 * x             # Weight of 丙禾 per 秉

# Step 3: Calculate the total weight for each type of grain
甲禾總重 = 甲禾秉數 * x
乙禾總重 = 乙禾秉數 * y
丙禾總重 = 丙禾秉數 * z

# Results:
a = 甲禾秉數
b = 甲禾總重
c = 乙禾秉數
d = 乙禾總重
e = 丙禾秉數
f = 丙禾總重

# Output the results
print(f"甲禾 {a} 秉 重 {b} 石")
print(f"乙禾 {c} 秉 重 {d} 石")
print(f"丙禾 {e} 秉 重 {f} 石")


"""


### Explanation of the Solution:
1. **Set up the equations**: The relationships between the weights of the grains are translated into equations. The total weight is given as 39 斗.
2. **Substitute and simplify**: Using the relationships between the weights, substitute variables to reduce the system to one equation.
3. **Solve for x**: Solve for the weight of 甲禾 per 秉, then calculate the weights of 乙禾 and 丙禾 per 秉.
4. **Calculate total weights**: Multiply the weight per 秉 by the number of 秉 for each type of grain to get the total weight.

### Final Answer:
- 甲禾 2 秉 重 \( \frac{39}{16} \) 石
- 乙禾 3 秉 重 \( \frac{39}{8} \) 石
- 丙禾 4 秉 重 \( \frac{117}{16} \) 石
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 39/16
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 117/16
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 117/4"""
