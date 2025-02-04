"""
今有甲乙二人持錢不知其數。甲得乙半而錢五十，乙得甲太半而亦錢五十。問︰甲、乙持錢各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲持 a錢 ，乙持 b錢 。
"""

"""
This problem involves solving a system of equations based on the given conditions. Let's break it down and solve it step by step using Python.

### Problem Explanation:
1. **Given Conditions**:
   - If **甲** (Person A) takes half of **乙**'s (Person B's) money, **甲** will have 50 coins.
   - If **乙** takes more than half of **甲**'s money, **乙** will also have 50 coins.

2. **Goal**:
   - Find how much money **甲** and **乙** each have.

3. **Mathematical Representation**:
   Let:
   - `x` = money held by **甲** (Person A),
   - `y` = money held by **乙** (Person B).

   From the problem:
   - Equation 1: \( x + \frac{y}{2} = 50 \)
   - Equation 2: \( y + \frac{3x}{2} = 50 \)

   We solve this system of equations to find `x` and `y`.

---

### Python Code Solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations:
# x + y/2 = 50
# y + 3x/2 = 50

# Solve for x and y:
# From the first equation: y = 2(50 - x)
# Substitute into the second equation:
# 2(50 - x) + 3x/2 = 50

# Step 1: Simplify the second equation
# 100 - 2x + 3x/2 = 50
# Multiply through by 2 to eliminate fractions:
# 200 - 4x + 3x = 100
# -x = -100
# x = 100

# Step 2: Solve for y using the first equation:
# y = 2(50 - x)
# y = 2(50 - 100)
# y = 100

# Final Answer:
a = 100  # Money held by 甲
b = 0    # Money held by 乙

print(f"甲持 {a} 錢，乙持 {b} 錢。")
#----- content ends here -----


"""


---

### Explanation of the Solution:
1. From the first equation, we express `y` in terms of `x` as \( y = 2(50 - x) \).
2. Substitute this expression for `y` into the second equation and solve for `x`.
3. Once `x` is found, substitute it back into the first equation to find `y`.

---

### Final Answer:
- **甲持 a = 100 錢**.
- **乙持 b = 0 錢**.
"""


"""
Variable 'a' has wrong value. Expected: 75/2, Actual: 100
Variable 'b' has wrong value. Expected: 25, Actual: 0"""
