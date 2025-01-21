"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
術曰：如方程。損之曰益，益之曰損。損實一斗者，其實過一十斗也。益實一斗者，其實不滿一十斗也。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese procedure into Python code step by step. The solution involves solving a system of linear equations based on the relationships provided in the problem.

### Problem Setup:
- **Equation 1**: Seven "上禾" (upper grain bundles) lose 1斗 (dou), and adding 2 "下禾" (lower grain bundles) results in 10斗.
- **Equation 2**: Eight "下禾" gain 1斗, and adding 2 "上禾" results in 10斗.

We need to find the actual yield of one "上禾" and one "下禾".

---

### Python Code:


"""


from fractions import Fraction

# Define the equations based on the problem:
# Let x = yield of one "上禾" (upper grain bundle)
# Let y = yield of one "下禾" (lower grain bundle)

# Equation 1: 7x - 1 + 2y = 10
# Simplify: 7x + 2y = 11
# Equation 2: 2x + 8y + 1 = 10
# Simplify: 2x + 8y = 9

# Coefficients for the equations:
# 7x + 2y = 11
# 2x + 8y = 9

# Solve using elimination:
# Multiply the first equation by 4 and the second equation by 1 to align coefficients of y:
# 28x + 8y = 44
# 2x + 8y = 9

# Subtract the second equation from the first:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)  # Yield of one "上禾"

# Substitute x into the first equation to solve for y:
# 7x + 2y = 11
# 2y = 11 - 7x
# y = (11 - 7x) / 2
y = Fraction(11 - 7 * x, 2)  # Yield of one "下禾"

# Results:
a = 7  # Number of "上禾" bundles
b = x  # Yield of one "上禾" bundle
c = 8  # Number of "下禾" bundles
d = y  # Yield of one "下禾" bundle

# Output:
print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


---

### Explanation of the Code:
1. **Define Variables**:
   - `x` represents the yield of one "上禾".
   - `y` represents the yield of one "下禾".

2. **Set Up Equations**:
   - The problem gives two equations based on the relationships between "上禾" and "下禾".

3. **Solve the System of Equations**:
   - Use the elimination method to solve for `x` (yield of "上禾").
   - Substitute `x` into one of the equations to solve for `y` (yield of "下禾").

4. **Output Results**:
   - The results are expressed in terms of the number of bundles and the yield per bundle.

---

### Final Answer:
The yield of one "上禾" and one "下禾" is expressed as fractions of a "斗". The code calculates and outputs these values.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
