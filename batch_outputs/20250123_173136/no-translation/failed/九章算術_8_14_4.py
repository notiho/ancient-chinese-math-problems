"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem essentially involves solving a system of equations using the described method, which is similar to Gaussian elimination. Here's the Python implementation:


"""


from fractions import Fraction

# Given data
甲禾秉數 = 2
乙禾秉數 = 3
丙禾秉數 = 4

# Relationships between weights
甲重比乙 = Fraction(2, 1)  # 甲二重如乙一
乙重比丙 = Fraction(3, 1)  # 乙三重如丙一
丙重比甲 = Fraction(4, 1)  # 丙四重如甲一

# Total weight in 石 (converted to 斗, as 1 石 = 10 斗)
總重 = 39  # in 斗

# Step 1: Set up the equations
# Let x = 甲禾一秉重, y = 乙禾一秉重, z = 丙禾一秉重
# From the problem, we have:
# 2x + 3y + 4z = 39
# x = 2y
# y = 3z

# Step 2: Substitute the relationships into the first equation
# Substitute x = 2y and y = 3z into 2x + 3y + 4z = 39
# 2(2y) + 3y + 4z = 39
# 4y + 3y + 4z = 39
# 7y + 4z = 39
# Substitute y = 3z into 7y + 4z = 39
# 7(3z) + 4z = 39
# 21z + 4z = 39
# 25z = 39
z = Fraction(39, 25)

# Step 3: Solve for y and x
y = 3 * z
x = 2 * y

# Convert to 石 (since 1 石 = 10 斗)
a = x / 10  # 甲禾一秉重 in 石
b = y / 10  # 乙禾一秉重 in 石
c = z / 10  # 丙禾一秉重 in 石

# Results
print(f"甲禾一秉重: {a} 石")
print(f"乙禾一秉重: {b} 石")
print(f"丙禾一秉重: {c} 石")


"""


### Explanation of the Code:
1. **Relationships**: The relationships between the weights of the grains are translated into equations.
2. **Substitution**: The relationships are substituted into the main equation to reduce the number of variables.
3. **Solve for Variables**: The reduced equation is solved step by step to find the weight of one 秉 (bundle) for each type of grain.
4. **Conversion**: The weights are converted from 斗 to 石 for the final answer.

### Final Answer:
- 甲禾一秉重: \( a = \frac{234}{250} = 0.936 \) 石
- 乙禾一秉重: \( b = \frac{117}{250} = 0.468 \) 石
- 丙禾一秉重: \( c = \frac{39}{250} = 0.156 \) 石
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 117/125
Variable 'b' has wrong value. Expected: 11/23, Actual: 117/250
Variable 'c' has wrong value. Expected: 10/23, Actual: 39/250"""
