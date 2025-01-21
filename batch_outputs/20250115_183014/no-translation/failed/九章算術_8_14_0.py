"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
To solve this problem, we will implement the described procedure using Python code. The problem involves a system of equations derived from the relationships between the weights of the bundles of grain (甲, 乙, 丙). The solution will follow the steps of the "方程術" as described.


"""


from fractions import Fraction

# Given data
甲秉數 = 2
乙秉數 = 3
丙秉數 = 4

# Relationships between weights
甲重比 = Fraction(1, 2)  # 甲二重如乙一
乙重比 = Fraction(1, 3)  # 乙三重如丙一
丙重比 = Fraction(1, 4)  # 丙四重如甲一

# Total weight in 石 (converted to 斗, as 1 石 = 10 斗)
總重 = 39  # in 斗

# Step 1: Set up the equations
# Let x = weight of 甲禾 (per 秉), y = weight of 乙禾 (per 秉), z = weight of 丙禾 (per 秉)
# Equations:
# 2x + 3y + 4z = 39
# x = 2y
# y = 3z

# Step 2: Solve for z (weight of 丙禾 per 秉)
# Substitute y = 3z into x = 2y
# x = 2(3z) = 6z
# Substitute x = 6z and y = 3z into the total weight equation:
# 2(6z) + 3(3z) + 4z = 39
# 12z + 9z + 4z = 39
# 25z = 39
z = Fraction(39, 25)

# Step 3: Solve for y (weight of 乙禾 per 秉)
y = 3 * z

# Step 4: Solve for x (weight of 甲禾 per 秉)
x = 6 * z

# Step 5: Calculate total weights for each type of grain
甲總重 = 甲秉數 * x
乙總重 = 乙秉數 * y
丙總重 = 丙秉數 * z

# Convert weights to 石 (1 石 = 10 斗)
甲總重_石 = 甲總重 / 10
乙總重_石 = 乙總重 / 10
丙總重_石 = 丙總重 / 10

# Results
a = 甲秉數
b = 甲總重_石
c = 乙秉數
d = 乙總重_石
e = 丙秉數
f = 丙總重_石

# Output
print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


### Explanation of the Code:
1. **Input Data**: The number of bundles (秉數) for each type of grain and their weight relationships are given.
2. **Equations**: The relationships between weights are translated into equations.
3. **Solution**: The equations are solved step-by-step using substitution to find the weight per bundle for each type of grain.
4. **Total Weights**: The total weight for each type of grain is calculated by multiplying the weight per bundle by the number of bundles.
5. **Conversion**: The weights are converted from 斗 to 石 for the final answer.

### Final Answer:
The output will provide the number of bundles and total weight in 石 for 甲, 乙, and 丙 grains.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 234/125
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 351/250
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 78/125"""
