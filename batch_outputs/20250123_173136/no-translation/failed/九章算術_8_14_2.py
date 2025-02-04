"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
To solve this problem using the described method (方程術), we will translate the procedure into Python code step by step. The problem involves solving a system of linear equations using elimination and substitution, as described in the ancient Chinese mathematical text.

The relationships given are:
- \( \text{甲二重如乙一} \) → \( 2 \cdot \text{甲} = \text{乙} \)
- \( \text{乙三重如丙一} \) → \( 3 \cdot \text{乙} = \text{丙} \)
- \( \text{丙四重如甲一} \) → \( 4 \cdot \text{丙} = \text{甲} \)

The total weight of the grains is \( 39 \) 斗 (斗 is a unit of weight).

Let's encode this step by step:


"""


from fractions import Fraction

# Step 1: Define the relationships and total weight
甲秉數 = 2  # 甲禾二秉
乙秉數 = 3  # 乙禾三秉
丙秉數 = 4  # 丙禾四秉
總重量 = 39  # 總重量為39斗

# Step 2: Represent the relationships as equations
# Let x = weight of one 甲禾, y = weight of one 乙禾, z = weight of one 丙禾
# From the problem:
# 2x + 3y + 4z = 39 (total weight equation)
# 2x = y (relationship between 甲 and 乙)
# 3y = z (relationship between 乙 and 丙)

# Step 3: Substitute relationships into the total weight equation
# Substitute y = 2x into 3y = z to get z = 6x
# Substitute y = 2x and z = 6x into 2x + 3y + 4z = 39
# 2x + 3(2x) + 4(6x) = 39
# 2x + 6x + 24x = 39
# 32x = 39

# Step 4: Solve for x, y, and z
x = Fraction(39, 32)  # Weight of one 甲禾
y = 2 * x             # Weight of one 乙禾
z = 6 * x             # Weight of one 丙禾

# Step 5: Convert to 石 (1 石 = 10 斗)
a = x / 10  # 甲禾一秉重 in 石
b = y / 10  # 乙禾一秉重 in 石
c = z / 10  # 丙禾一秉重 in 石

# Output the results
a, b, c


"""


### Explanation:
1. **Relationships**: The relationships between the weights of the grains are translated into equations.
2. **Substitution**: The equations are substituted step by step to eliminate variables and solve for \( x \), \( y \), and \( z \).
3. **Conversion**: The final weights are converted from 斗 to 石 for the answer.

### Final Answer:
- \( a = \text{甲禾一秉重} = \frac{39}{320} \text{石} \)
- \( b = \text{乙禾一秉重} = \frac{78}{320} \text{石} \)
- \( c = \text{丙禾一秉重} = \frac{234}{320} \text{石} \)
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 39/320
Variable 'b' has wrong value. Expected: 11/23, Actual: 39/160
Variable 'c' has wrong value. Expected: 10/23, Actual: 117/160"""
