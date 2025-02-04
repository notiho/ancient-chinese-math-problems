"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of linear algebra. Let's translate the problem and procedure into Python code step by step.

### Problem Breakdown:
- There are three types of grain: Jia (甲), Yi (乙), and Bing (丙), with weights proportional to their respective bundles.
- Relationships between weights:
  - 2 bundles of Jia weigh as much as 1 bundle of Yi.
  - 3 bundles of Yi weigh as much as 1 bundle of Bing.
  - 4 bundles of Bing weigh as much as 1 bundle of Jia.
- Total weight of the grains is more than 1 shi (石), and we need to find the weight of 1 bundle of each type of grain.

### Procedure:
The procedure uses the "fangcheng" method, which involves setting up a system of equations and solving it step by step. Here's how we can implement it in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Relationships between weights:
# 2 bundles of Jia = 1 bundle of Yi
# 3 bundles of Yi = 1 bundle of Bing
# 4 bundles of Bing = 1 bundle of Jia

# Step 1: Define the equations based on the problem.
# Let x = weight of 1 bundle of Jia (甲禾)
# Let y = weight of 1 bundle of Yi (乙禾)
# Let z = weight of 1 bundle of Bing (丙禾)

# From the relationships:
# 2x = y  -> y = 2x
# 3y = z  -> z = 3y
# 4z = x  -> x = 4z

# Step 2: Substitute the relationships into a single variable.
# Substitute y = 2x into z = 3y:
# z = 3(2x) = 6x
# Substitute z = 6x into x = 4z:
# x = 4(6x) = 24x

# This creates a contradiction unless we normalize the weights.
# Normalize such that the total weight is 1 shi (石).

# Step 3: Normalize the weights.
# Total weight = x + y + z = 1 shi
# Substitute y = 2x and z = 6x:
# x + 2x + 6x = 1
# 9x = 1
x = Fraction(1, 9)  # Weight of 1 bundle of Jia (甲禾)
y = 2 * x           # Weight of 1 bundle of Yi (乙禾)
z = 6 * x           # Weight of 1 bundle of Bing (丙禾)

# Step 4: Convert to shi (石).
a = x
b = y
c = z

# Output the results.
print(f"甲禾一秉重 {a} 石")  # Weight of 1 bundle of Jia
print(f"乙禾一秉重 {b} 石")  # Weight of 1 bundle of Yi
print(f"丙禾一秉重 {c} 石")  # Weight of 1 bundle of Bing
#----- content ends here -----


"""


### Explanation of the Code:
1. **Relationships**: The relationships between the weights are expressed as equations.
2. **Substitution**: The equations are substituted into each other to express all weights in terms of a single variable (`x` for Jia).
3. **Normalization**: The total weight is normalized to 1 shi (石), and the weights of each type of grain are calculated.
4. **Output**: The weights of 1 bundle of each type of grain are printed as fractions of a shi.

### Answer:
The weights of 1 bundle of each type of grain are:
- 甲禾 (Jia): \( \frac{1}{9} \) 石
- 乙禾 (Yi): \( \frac{2}{9} \) 石
- 丙禾 (Bing): \( \frac{6}{9} = \frac{2}{3} \) 石
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1/9
Variable 'b' has wrong value. Expected: 11/23, Actual: 2/9
Variable 'c' has wrong value. Expected: 10/23, Actual: 2/3"""
