"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：甲禾 a秉 重 b石 ，乙禾 c秉 重 d石 ，丙禾 e秉 重 f石 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, which is essentially a form of Gaussian elimination. Let's translate the procedure into Python code step by step.

### Problem Setup
- **Given:**  
  - `甲禾` has 2秉, `乙禾` has 3秉, `丙禾` has 4秉.
  - Relationships between weights:
    - `甲` 2重 = `乙` 1重
    - `乙` 3重 = `丙` 1重
    - `丙` 4重 = `甲` 1重
  - Total weight = 39斗.

We need to find the weight of 1秉 for each type of grain (`甲`, `乙`, `丙`).

---

### Code Implementation


"""


from fractions import Fraction

# Step 1: Define the relationships between the weights
# Let x = weight of 1秉 of 甲禾
# Let y = weight of 1秉 of 乙禾
# Let z = weight of 1秉 of 丙禾

# Relationships:
# 2x = y
# 3y = z
# 4z = x

# Step 2: Express the relationships in terms of one variable
# From 2x = y, we get y = 2x
# From 3y = z, we get z = 3y = 3(2x) = 6x
# From 4z = x, we get x = 4z = 4(6x) = 24x, which simplifies to x = 1/24

# Step 3: Solve for x, y, z
x = Fraction(1, 24)  # Weight of 1秉 of 甲禾
y = 2 * x            # Weight of 1秉 of 乙禾
z = 6 * x            # Weight of 1秉 of 丙禾

# Step 4: Calculate the total weight
# Total weight = 2秉 of 甲禾 + 3秉 of 乙禾 + 4秉 of 丙禾
total_weight = 2 * x + 3 * y + 4 * z

# Given total weight = 39斗, solve for the scaling factor
scaling_factor = Fraction(39, total_weight)

# Step 5: Scale the weights
a秉 = 2  # Number of 秉 for 甲禾
b石 = scaling_factor * x * a秉

c秉 = 3  # Number of 秉 for 乙禾
d石 = scaling_factor * y * c秉

e秉 = 4  # Number of 秉 for 丙禾
f石 = scaling_factor * z * e秉

# Final Results
a = a秉
b = b石
c = c秉
d = d石
e = e秉
f = f石

print(f"甲禾 {a}秉 重 {b}石")
print(f"乙禾 {c}秉 重 {d}石")
print(f"丙禾 {e}秉 重 {f}石")


"""


---

### Explanation of the Code
1. **Relationships Between Weights:**  
   The relationships between the weights are expressed as equations and solved in terms of one variable (`x`).

2. **Scaling Factor:**  
   The total weight of all grains is given as 39斗. The scaling factor is calculated to adjust the weights accordingly.

3. **Final Weights:**  
   The weights of 1秉 for each type of grain are scaled and multiplied by the number of 秉 for each type to get the final results.

---

### Output
The program will output the following:
```
甲禾 2秉 重 b石
乙禾 3秉 重 d石
丙禾 4秉 重 f石
```

Where `b`, `d`, and `f` are the respective weights in 石.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 17/23, Actual: 39/16
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 11/23, Actual: 117/16
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 10/23, Actual: 117/4"""
