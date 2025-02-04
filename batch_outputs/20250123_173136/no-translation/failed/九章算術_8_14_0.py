"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
To solve this problem, we will implement the described procedure using Python code. The problem involves a system of equations derived from the relationships between the weights of the bundles of grain (甲, 乙, 丙). The solution will follow the steps of the "方程術" as described.


"""


from fractions import Fraction

# Given data
甲秉數 = 2  # 甲禾二秉
乙秉數 = 3  # 乙禾三秉
丙秉數 = 4  # 丙禾四秉
總重 = 39  # 實三十九斗

# Relationships between weights
# 甲二重如乙一 -> 甲 = 1/2 乙
# 乙三重如丙一 -> 乙 = 1/3 丙
# 丙四重如甲一 -> 丙 = 1/4 甲

# Step 1: Express weights in terms of a single variable
# Let 丙 = x
丙重 = Fraction(1, 1)  # 丙 = x
乙重 = Fraction(1, 3) * 丙重  # 乙 = 1/3 丙
甲重 = Fraction(1, 2) * 乙重  # 甲 = 1/2 乙

# Step 2: Calculate total weight in terms of 丙
總重_方程 = (甲秉數 * 甲重) + (乙秉數 * 乙重) + (丙秉數 * 丙重)

# Step 3: Solve for 丙重
丙重 = Fraction(總重, 總重_方程.denominator)

# Step 4: Calculate 乙重 and 甲重
乙重 = Fraction(1, 3) * 丙重
甲重 = Fraction(1, 2) * 乙重

# Step 5: Convert weights to 石 (1 石 = 10 斗)
a = 甲重 / 10  # 甲禾一秉重
b = 乙重 / 10  # 乙禾一秉重
c = 丙重 / 10  # 丙禾一秉重

# Results
a, b, c


"""


### Explanation of the Code:
1. **Relationships Between Weights**: The relationships between the weights of 甲, 乙, and 丙 are expressed as fractions.
2. **Single Variable Representation**: All weights are expressed in terms of 丙 (denoted as `x`).
3. **Equation for Total Weight**: The total weight of all bundles is expressed as a single equation in terms of 丙.
4. **Solve for 丙**: The total weight equation is solved to find the weight of 丙.
5. **Calculate Other Weights**: Using the relationships, the weights of 甲 and 乙 are calculated.
6. **Convert to 石**: The weights are converted from 斗 to 石 (1 石 = 10 斗).

### Final Answer:
- 甲禾一秉重 `a` 石
- 乙禾一秉重 `b` 石
- 丙禾一秉重 `c` 石
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 13/60
Variable 'b' has wrong value. Expected: 11/23, Actual: 13/30
Variable 'c' has wrong value. Expected: 10/23, Actual: 13/10"""
