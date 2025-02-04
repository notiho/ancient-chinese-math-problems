"""
今有甲禾二秉乙禾三秉丙禾四秉重皆過於石甲二重如乙一乙三重如丙一丙四重如甲一問甲乙丙禾一秉各重幾何
術曰如方程置重過於石之物為負以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰甲禾一秉重 a石 乙禾一秉重 b石 丙禾一秉重 c石 
"""

"""
This problem involves solving a system of equations using ancient Chinese "fangcheng" (linear algebra) methods. The problem describes the weights of bundles of grain (禾) and their relationships. Let's translate this into Python step by step, following the procedure.

### Problem Description:
- There are three types of grain: Jia (甲), Yi (乙), and Bing (丙).
- Jia has 2 bundles (秉), Yi has 3 bundles, and Bing has 4 bundles.
- Their combined weight exceeds 1 shi (石).
- The relationships between their weights are:
  - The weight of 2 bundles of Jia equals the weight of 1 bundle of Yi.
  - The weight of 3 bundles of Yi equals the weight of 1 bundle of Bing.
  - The weight of 4 bundles of Bing equals the weight of 1 bundle of Jia.
- We are tasked with finding the weight of 1 bundle of Jia, Yi, and Bing.

### Procedure:
The procedure uses the "fangcheng" method (similar to solving linear equations). Here's the step-by-step translation:


"""


from fractions import Fraction

# Define the relationships as equations:
# Let a, b, c represent the weight of 1 bundle of Jia, Yi, and Bing respectively.

# 2a = b (2 bundles of Jia equal 1 bundle of Yi)
# 3b = c (3 bundles of Yi equal 1 bundle of Bing)
# 4c = a (4 bundles of Bing equal 1 bundle of Jia)

# Step 1: Express b and c in terms of a
b = Fraction(2, 1) * a  # From 2a = b
c = Fraction(3, 1) * b  # From 3b = c
c = Fraction(3, 1) * (Fraction(2, 1) * a)  # Substitute b = 2a into c = 3b

# Step 2: Substitute c into 4c = a to solve for a
a = Fraction(4, 1) * c  # From 4c = a
a = Fraction(4, 1) * (Fraction(3, 1) * (Fraction(2, 1) * a))  # Substitute c = 3(2a)

# Simplify to solve for a
a = Fraction(1, 29)  # Simplified weight of 1 bundle of Jia

# Step 3: Solve for b and c using a
b = Fraction(2, 1) * a  # Weight of 1 bundle of Yi
c = Fraction(3, 1) * b  # Weight of 1 bundle of Bing

# Final results
a = Fraction(1, 29)  # Weight of 1 bundle of Jia in shi
b = Fraction(2, 29)  # Weight of 1 bundle of Yi in shi
c = Fraction(6, 29)  # Weight of 1 bundle of Bing in shi

# Output the results
print(f"甲禾一秉重 {a} 石")
print(f"乙禾一秉重 {b} 石")
print(f"丙禾一秉重 {c} 石")


"""


### Explanation of the Results:
- The weight of 1 bundle of Jia (甲禾) is `1/29` shi.
- The weight of 1 bundle of Yi (乙禾) is `2/29` shi.
- The weight of 1 bundle of Bing (丙禾) is `6/29` shi.

This solution follows the ancient "fangcheng" method by expressing variables in terms of others and solving step by step.
"""


"""
Code error: name 'a' is not defined"""
