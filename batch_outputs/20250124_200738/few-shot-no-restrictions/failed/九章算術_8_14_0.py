"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
This is a classic ancient Chinese problem involving simultaneous equations, solved using the "fangcheng" (方程) method, which is an early form of linear algebra. The problem involves determining the weight of one bundle of three types of grain (甲禾, 乙禾, 丙禾) based on their relationships and total weight.

### Problem Breakdown:
1. **Given:**
   - 甲禾: 2 bundles
   - 乙禾: 3 bundles
   - 丙禾: 4 bundles
   - Total weight: 39 dou (斗).
   - Weight relationships:
     - 2 weights of 甲 = 1 weight of 乙.
     - 3 weights of 乙 = 1 weight of 丙.
     - 4 weights of 丙 = 1 weight of 甲.

2. **Goal:**
   - Find the weight of 1 bundle of 甲禾, 乙禾, and 丙禾.

3. **Method:**
   - Use the relationships to set up equations and solve them using the fangcheng method.

---

### Step-by-Step Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Define the variables:
# Let x = weight of 1 bundle of 甲禾 (in dou)
# Let y = weight of 1 bundle of 乙禾 (in dou)
# Let z = weight of 1 bundle of 丙禾 (in dou)

# Relationships:
# 2x = y  --> y = 2x
# 3y = z  --> z = 3y
# 4z = x  --> x = 4z

# Total weight equation:
# 2 bundles of 甲禾 + 3 bundles of 乙禾 + 4 bundles of 丙禾 = 39 dou
# 2x + 3y + 4z = 39

# Substitute y and z in terms of x:
# y = 2x
# z = 3y = 3(2x) = 6x
# Substitute into the total weight equation:
# 2x + 3(2x) + 4(6x) = 39
# 2x + 6x + 24x = 39
# 32x = 39
# x = 39 / 32

# Solve for y and z:
x = Fraction(39, 32)  # Weight of 1 bundle of 甲禾
y = 2 * x             # Weight of 1 bundle of 乙禾
z = 6 * x             # Weight of 1 bundle of 丙禾

# Convert to 石 (1 石 = 10 斗):
a = x / 10  # Weight of 1 bundle of 甲禾 in 石
b = y / 10  # Weight of 1 bundle of 乙禾 in 石
c = z / 10  # Weight of 1 bundle of 丙禾 in 石

# Output the results:
print(f"甲禾一秉重 {a} 石")
print(f"乙禾一秉重 {b} 石")
print(f"丙禾一秉重 {c} 石")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Relationships:** The weight relationships are used to express `y` and `z` in terms of `x`.
2. **Substitution:** These expressions are substituted into the total weight equation to solve for `x`.
3. **Conversion to 石:** Since the problem asks for the weight in 石, we divide the results (in 斗) by 10.

---

### Final Answer:
- 甲禾一秉重 \( a = \frac{39}{320} \) 石.
- 乙禾一秉重 \( b = \frac{78}{320} \) 石.
- 丙禾一秉重 \( c = \frac{234}{320} \) 石.
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 39/320
Variable 'b' has wrong value. Expected: 11/23, Actual: 39/160
Variable 'c' has wrong value. Expected: 10/23, Actual: 117/160"""
