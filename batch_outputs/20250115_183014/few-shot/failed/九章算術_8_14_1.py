"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This problem involves solving a system of equations based on the relationships between the weights of three types of grain bundles (甲禾, 乙禾, 丙禾). The solution uses ancient Chinese "方程術" (method of solving systems of linear equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Given data
甲禾秉數 = 2  # 甲禾 has 2 bundles
乙禾秉數 = 3  # 乙禾 has 3 bundles
丙禾秉數 = 4  # 丙禾 has 4 bundles
總重 = 39  # Total weight in dou (斗)

# Weight relationships
# 甲禾 2重如乙禾 1
甲重 = Fraction(2, 1)  # Weight of 甲禾 relative to 乙禾
# 乙禾 3重如丙禾 1
乙重 = Fraction(3, 1)  # Weight of 乙禾 relative to 丙禾
# 丙禾 4重如甲禾 1
丙重 = Fraction(4, 1)  # Weight of 丙禾 relative to 甲禾

# Step 1: Normalize weights
# Let 丙禾 = 1 unit of weight
丙禾單位重 = 1
乙禾單位重 = 丙禾單位重 * 丙重  # 乙禾 = 丙禾 * 4
甲禾單位重 = 乙禾單位重 * 乙重  # 甲禾 = 乙禾 * 3 = 丙禾 * 4 * 3 = 丙禾 * 12

# Step 2: Calculate total weight in terms of 丙禾
總重丙禾單位 = (甲禾秉數 * 甲禾單位重) + (乙禾秉數 * 乙禾單位重) + (丙禾秉數 * 丙禾單位重)

# Step 3: Solve for 丙禾 weight
丙禾每秉重 = Fraction(總重, 總重丙禾單位)

# Step 4: Solve for 乙禾 and 甲禾 weights
乙禾每秉重 = 丙禾每秉重 * 丙重
甲禾每秉重 = 乙禾每秉重 * 乙重

# Step 5: Calculate total weights for each type of grain
甲禾總重 = 甲禾秉數 * 甲禾每秉重
乙禾總重 = 乙禾秉數 * 乙禾每秉重
丙禾總重 = 丙禾秉數 * 丙禾每秉重

# Final results
a = 甲禾秉數
b = 甲禾每秉重
c = 乙禾秉數
d = 乙禾每秉重
e = 丙禾秉數
f = 丙禾每秉重

print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


### Explanation of the Code:
1. **Normalize Weights**: The relationships between the weights of the grains are used to express all weights in terms of a single unit (丙禾). This simplifies the calculations.
2. **Calculate Total Weight in Terms of 丙禾**: The total weight of all bundles is expressed in terms of the weight of 丙禾.
3. **Solve for 丙禾 Weight**: Using the total weight, the weight of one bundle of 丙禾 is calculated.
4. **Solve for 乙禾 and 甲禾 Weights**: Using the relationships, the weights of one bundle of 乙禾 and 甲禾 are calculated.
5. **Calculate Total Weights**: The total weights for each type of grain are calculated by multiplying the weight of one bundle by the number of bundles.

### Final Answer:
The program will output the weights of each type of grain bundle in terms of 石 (shi).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 117/10
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 39/10
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 39/40"""
