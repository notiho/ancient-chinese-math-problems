"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
This problem involves solving a system of equations using ancient Chinese mathematical methods, specifically the "fangcheng" (方程) method, which is an early form of solving linear equations. Below is the Python implementation of the procedure described in the problem.


"""


from fractions import Fraction

# Given data
甲禾秉數 = 2  # Two bundles of Jia grain
乙禾秉數 = 3  # Three bundles of Yi grain
丙禾秉數 = 4  # Four bundles of Bing grain

# Weight relationships
# 甲二重如乙一 (Two Jia weights equal one Yi weight)
甲重 = Fraction(1, 2)  # Weight of one Jia bundle in terms of Yi
# 乙三重如丙一 (Three Yi weights equal one Bing weight)
乙重 = Fraction(1, 3)  # Weight of one Yi bundle in terms of Bing
# 丙四重如甲一 (Four Bing weights equal one Jia weight)
丙重 = Fraction(1, 4)  # Weight of one Bing bundle in terms of Jia

# Total weight exceeds one shi (石), which is 39 dou (斗)
總重 = 39  # Total weight in dou

# Step 1: Express the weights of Jia, Yi, and Bing in terms of a common unit
# Let the weight of one Bing bundle be x
丙禾一秉重 = 1  # Assume Bing is the base unit (x = 1)
乙禾一秉重 = 丙重 * 丙禾一秉重  # Yi weight in terms of Bing
甲禾一秉重 = 乙重 * 乙禾一秉重  # Jia weight in terms of Bing

# Step 2: Set up the equation for the total weight
# Total weight = (甲禾秉數 * 甲禾一秉重) + (乙禾秉數 * 乙禾一秉重) + (丙禾秉數 * 丙禾一秉重)
總重方程 = (
    甲禾秉數 * 甲禾一秉重
    + 乙禾秉數 * 乙禾一秉重
    + 丙禾秉數 * 丙禾一秉重
)

# Step 3: Solve for the weight of one Bing bundle
丙禾一秉重 = Fraction(總重, 總重方程)

# Step 4: Calculate the weights of one Jia and one Yi bundle
乙禾一秉重 = 丙重 * 丙禾一秉重
甲禾一秉重 = 乙重 * 乙禾一秉重

# Convert weights to shi (1 shi = 10 dou)
a = Fraction(甲禾一秉重, 10)
b = Fraction(乙禾一秉重, 10)
c = Fraction(丙禾一秉重, 10)

# Final answer
print(f"甲禾一秉重: {a} 石")
print(f"乙禾一秉重: {b} 石")
print(f"丙禾一秉重: {c} 石")


"""


### Explanation of the Code:
1. **Weight Relationships**: The relationships between the weights of Jia, Yi, and Bing grains are converted into fractions.
2. **Common Unit**: The weight of one Bing bundle is assumed to be the base unit (`1`), and the weights of Jia and Yi bundles are expressed in terms of Bing.
3. **Total Weight Equation**: The total weight of all bundles is expressed as a linear equation.
4. **Solve for Bing Weight**: The weight of one Bing bundle is calculated by dividing the total weight by the total weight equation.
5. **Calculate Jia and Yi Weights**: Using the relationships, the weights of one Jia and one Yi bundle are calculated.
6. **Convert to Shi**: The weights are converted from dou to shi for the final answer.

### Final Answer:
The weights of one bundle of Jia, Yi, and Bing grains are given in terms of shi:
- 甲禾一秉重: `a` 石
- 乙禾一秉重: `b` 石
- 丙禾一秉重: `c` 石
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 39/590
Variable 'b' has wrong value. Expected: 11/23, Actual: 117/590
Variable 'c' has wrong value. Expected: 10/23, Actual: 234/295"""
