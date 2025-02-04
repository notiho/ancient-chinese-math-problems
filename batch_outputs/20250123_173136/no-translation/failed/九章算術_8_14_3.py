"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese method of solving simultaneous equations (方程術) into Python code. The problem involves three types of grain (甲, 乙, 丙) with specific relationships between their weights. Here's the step-by-step solution:


"""


from fractions import Fraction

# Given data
甲禾秉數 = 2  # 甲禾二秉
乙禾秉數 = 3  # 乙禾三秉
丙禾秉數 = 4  # 丙禾四秉
總重 = 39  # 實三十九斗

# Weight relationships:
# 甲二重如乙一 -> 甲 = 1/2 乙
# 乙三重如丙一 -> 乙 = 1/3 丙
# 丙四重如甲一 -> 丙 = 1/4 甲

# Step 1: Express all weights in terms of 丙
甲 = Fraction(1, 4) * 丙禾秉數
乙 = Fraction(1, 3) * 丙禾秉數

# Step 2: Write the total weight equation
# 2甲 + 3乙 + 4丙 = 39
total_weight = 甲禾秉數 * 甲 + 乙禾秉數 * 乙 + 丙禾秉數 * 丙

# Step 3: Solve for 丙
丙 = Fraction(總重, total_weight)

# Step 4: Solve for 甲 and 乙
甲 = Fraction(1, 4) * 丙
乙 = Fraction(1, 3) * 丙

# Convert to 石 (1 石 = 10 斗)
a = 甲 / 10
b = 乙 / 10
c = 丙 / 10

# Results
print(f"甲禾一秉重 {a} 石")
print(f"乙禾一秉重 {b} 石")
print(f"丙禾一秉重 {c} 石")


"""


### Explanation:
1. **Relationships**: The relationships between the weights of 甲, 乙, and 丙 are expressed as fractions.
2. **Total Weight Equation**: The total weight of all grains is given as 39 斗, which is used to form the equation.
3. **Solve for 丙**: Using the total weight equation, we solve for 丙 in terms of the total weight.
4. **Back-substitution**: Using the value of 丙, we calculate the weights of 甲 and 乙.
5. **Convert to 石**: Since the result is required in 石, we divide the斗 weights by 10.

This code will compute the weights of 甲, 乙, and 丙 in 石.
"""


"""
Code error: name '丙' is not defined"""
