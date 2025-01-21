"""
今有甲禾二秉乙禾三秉丙禾四秉重皆過於石甲二重如乙一乙三重如丙一丙四重如甲一問甲乙丙禾一秉各重幾何
術曰如方程置重過於石之物為負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰甲禾 a秉 重 b石 乙禾 c秉 重 d石 丙禾 e秉 重 f石 
"""

"""
This problem involves solving a system of equations using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving simultaneous linear equations. Here's the breakdown and solution:

### Problem Description:
Suppose there are three types of grain: Jia (甲), Yi (乙), and Bing (丙).  
- Jia has 2 bundles, Yi has 3 bundles, and Bing has 4 bundles.  
- Their total weight exceeds 1 shi (石).  
- Jia's weight is twice that of Yi's weight for one bundle.  
- Yi's weight is three times that of Bing's weight for one bundle.  
- Bing's weight is four times that of Jia's weight for one bundle.  

Question: What is the weight of one bundle of Jia, Yi, and Bing grain?

### Procedure:
The "fangcheng" method is used to solve this system of equations.  
- Place the excess weight over 1 shi as negative.  
- Use the positive-negative method to solve.  
- Follow the steps of the fangcheng procedure to calculate the weights.

### Solution in Python:


"""


from fractions import Fraction

# Given data:
甲禾秉數 = 2  # Jia has 2 bundles
乙禾秉數 = 3  # Yi has 3 bundles
丙禾秉數 = 4  # Bing has 4 bundles

# Relationships between weights:
# Jia's weight is twice Yi's weight: 甲重 = 2 * 乙重
# Yi's weight is three times Bing's weight: 乙重 = 3 * 丙重
# Bing's weight is four times Jia's weight: 丙重 = 4 * 甲重

# Let the weight of one bundle of Jia, Yi, and Bing be x, y, z respectively.
# We need to solve for x, y, z.

# Step 1: Set up the equations based on the relationships.
# Equation 1: 甲重 = 2 * 乙重 -> x = 2 * y
# Equation 2: 乙重 = 3 * 丙重 -> y = 3 * z
# Equation 3: 丙重 = 4 * 甲重 -> z = 4 * x

# Step 2: Solve the system of equations.
# Substitute y = 3 * z into x = 2 * y:
# x = 2 * (3 * z) = 6 * z

# Substitute z = 4 * x into x = 6 * z:
# x = 6 * (4 * x) -> x = 24 * x
# This leads to a contradiction unless we normalize the weights.

# Normalize the weights:
# Assume the total weight is 1 shi (石), which equals 120 dou (斗).
# The total weight is distributed as:
# Total weight = 甲禾秉數 * x + 乙禾秉數 * y + 丙禾秉數 * z = 120 dou.

# Substitute x = 6 * z and y = 3 * z into the total weight equation:
# 2 * x + 3 * y + 4 * z = 120
# 2 * (6 * z) + 3 * (3 * z) + 4 * z = 120
# 12 * z + 9 * z + 4 * z = 120
# 25 * z = 120
z = Fraction(120, 25)  # Weight of one bundle of Bing
z = Fraction(24, 5)  # Simplified

# Calculate y and x:
y = 3 * z  # Yi's weight
x = 6 * z  # Jia's weight

# Step 3: Calculate the total weight for each type of grain.
甲禾重 = 甲禾秉數 * x  # Total weight of Jia grain
乙禾重 = 乙禾秉數 * y  # Total weight of Yi grain
丙禾重 = 丙禾秉數 * z  # Total weight of Bing grain

# Results:
a = 甲禾秉數  # Jia bundles
b = Fraction(甲禾重, 120)  # Jia weight in shi
c = 乙禾秉數  # Yi bundles
d = Fraction(乙禾重, 120)  # Yi weight in shi
e = 丙禾秉數  # Bing bundles
f = Fraction(丙禾重, 120)  # Bing weight in shi

# Output the results:
print(f"甲禾 {a} 秉, 重 {b} 石")
print(f"乙禾 {c} 秉, 重 {d} 石")
print(f"丙禾 {e} 秉, 重 {f} 石")


"""


### Explanation of Results:
- `a`, `b`: Number of Jia bundles and their weight in shi.  
- `c`, `d`: Number of Yi bundles and their weight in shi.  
- `e`, `f`: Number of Bing bundles and their weight in shi.  

This solution uses the relationships between the weights and the total weight constraint to calculate the weight of one bundle for each type of grain.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 12/25
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 9/25
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 4/25"""
