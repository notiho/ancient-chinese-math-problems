"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of linear algebra. Let's translate the problem and the solution into Python code.

### Problem Description:
There are three types of grain bundles: Jia (甲), Yi (乙), and Bing (丙).  
- Jia has 2 bundles, Yi has 3 bundles, and Bing has 4 bundles, and their total weight exceeds 1 shi (石).  
- The weight relationships are as follows:  
  - 2 weights of Jia equal 1 weight of Yi.  
  - 3 weights of Yi equal 1 weight of Bing.  
  - 4 weights of Bing equal 1 weight of Jia.  

The goal is to find the weight of 1 bundle of Jia, Yi, and Bing.

### Procedure:
The procedure involves setting up and solving a system of equations using the "fangcheng" method. Here's the step-by-step solution:

---


"""


from fractions import Fraction

# Step 1: Define the given relationships and quantities
# Jia (甲), Yi (乙), Bing (丙) bundle counts
甲_秉數 = 2
乙_秉數 = 3
丙_秉數 = 4

# Weight relationships:
# 2 weights of Jia = 1 weight of Yi
# 3 weights of Yi = 1 weight of Bing
# 4 weights of Bing = 1 weight of Jia
# These relationships can be expressed as:
# 甲重 = 1/2 * 乙重
# 乙重 = 1/3 * 丙重
# 丙重 = 1/4 * 甲重

# Step 2: Express the equations in terms of a common variable
# Let 丙重 = 1 unit (as a reference weight)
丙重 = 1
乙重 = Fraction(1, 3) * 丙重
甲重 = Fraction(1, 2) * 乙重

# Step 3: Calculate the weight of 1 bundle of each type
a = 甲重
b = 乙重
c = 丙重

# Step 4: Convert weights to shi (石) if necessary
# (In this case, the weights are already normalized to a common unit)

# Output the results
print(f"甲禾一秉重 {a} 石")
print(f"乙禾一秉重 {b} 石")
print(f"丙禾一秉重 {c} 石")


"""


### Explanation of the Code:
1. **Weight Relationships**: The relationships between the weights of Jia, Yi, and Bing are expressed as fractions. For example, `甲重 = 1/2 * 乙重` means that the weight of Jia is half the weight of Yi.
2. **Common Variable**: The weight of Bing (`丙重`) is chosen as the reference weight (1 unit), and the weights of Jia and Yi are calculated relative to Bing.
3. **Output**: The weights of 1 bundle of Jia, Yi, and Bing are printed in terms of shi (石).

### Answer:
- 甲禾一秉重 \( a = \frac{1}{6} \) 石  
- 乙禾一秉重 \( b = \frac{1}{3} \) 石  
- 丙禾一秉重 \( c = 1 \) 石
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1/6
Variable 'b' has wrong value. Expected: 11/23, Actual: 1/3
Variable 'c' has wrong value. Expected: 10/23, Actual: 1"""
