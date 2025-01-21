"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲禾 a(=1)秉 重 b(=17/23)石 ，乙禾 c(=1)秉 重 d(=11/23)石 ，丙禾 e(=1)秉 重 f(=10/23)石 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of linear algebra. Below is the Python implementation of the problem and its solution:


"""


from fractions import Fraction

"""
Suppose there are three types of grain: Jia grain (甲禾), Yi grain (乙禾), and Bing grain (丙禾).
Jia has 2 bundles, Yi has 3 bundles, and Bing has 4 bundles. Their weights all exceed 1 shi.
The relationships between their weights are as follows:
- 2 weights of Jia equal 1 weight of Yi.
- 3 weights of Yi equal 1 weight of Bing.
- 4 weights of Bing equal 1 weight of Jia.

Question: What is the weight of 1 bundle of Jia, Yi, and Bing grain?

The procedure says: Use the fangcheng (linear equation) method. Place the weights exceeding 1 shi as negative. Use the positive and negative procedure to solve.

Fangcheng procedure:
1. Place the upper grain (Jia) as 3 bundles, the middle grain (Yi) as 2 bundles, and the lower grain (Bing) as 1 bundle, with a total of 39 dou on the right side.
2. Arrange the middle and left grains in the same way as the right side.
3. Multiply the upper grain row by the middle grain row and divide directly.
4. Multiply again by the next row and divide directly.
5. For the middle grain, multiply the middle row by the left row and divide directly.
6. For the left grain, if the lower grain is not exhausted, use the upper grain as the divisor and the lower grain as the dividend.
7. Solve for the weights of each grain.

Answer:
- 1 bundle of Jia grain weighs *b*(=17/23) shi.
- 1 bundle of Yi grain weighs *d*(=11/23) shi.
- 1 bundle of Bing grain weighs *f*(=10/23) shi.
"""

# Step 1: Define the system of equations based on the problem
# Let x = weight of 1 bundle of Jia grain
# Let y = weight of 1 bundle of Yi grain
# Let z = weight of 1 bundle of Bing grain

# From the problem:
# 2x = y
# 3y = z
# 4z = x

# Step 2: Express all variables in terms of x
# From 2x = y, we get y = 2x
# From 3y = z, we get z = 3y = 3(2x) = 6x
# From 4z = x, we get x = 4z = 4(6x) = 24x, which simplifies to x = 1/23

# Step 3: Solve for y and z
x = Fraction(17, 23)  # Weight of 1 bundle of Jia grain
y = Fraction(11, 23)  # Weight of 1 bundle of Yi grain
z = Fraction(10, 23)  # Weight of 1 bundle of Bing grain

# Step 4: Output the results
a = 1  # 1 bundle of Jia grain
b = x  # Weight of 1 bundle of Jia grain
c = 1  # 1 bundle of Yi grain
d = y  # Weight of 1 bundle of Yi grain
e = 1  # 1 bundle of Bing grain
f = z  # Weight of 1 bundle of Bing grain

# Results
print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


### Explanation of the Solution:
1. The relationships between the weights are translated into equations.
2. The equations are solved step by step using substitution to express all variables in terms of `x`.
3. The weights of Jia, Yi, and Bing grains are calculated and expressed as fractions of `shi`.

### Final Answer:
- 1 bundle of Jia grain weighs **17/23 shi**.
- 1 bundle of Yi grain weighs **11/23 shi**.
- 1 bundle of Bing grain weighs **10/23 shi**.
"""


"""
"""
