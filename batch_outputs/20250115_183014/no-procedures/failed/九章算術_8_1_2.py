"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b斗 ，下禾 c秉 實 d斗 。
"""

"""
This is a classic system of equations problem from ancient Chinese mathematics. Let's solve it step by step and translate it into Python code.

### Problem Breakdown:
1. There are two types of grain: **upper grain (上禾)** and **lower grain (下禾)**.
2. Seven bundles (秉) of upper grain lose 1 dou (斗) of grain, but when 2 bundles of lower grain are added, the total becomes 10 dou.
   - Equation 1: \( 7x - 1 + 2y = 10 \)
3. Eight bundles of lower grain gain 1 dou of grain, but when 2 bundles of upper grain are added, the total becomes 10 dou.
   - Equation 2: \( 8y + 1 + 2x = 10 \)
4. Solve for \( x \) (grain per bundle of upper grain) and \( y \) (grain per bundle of lower grain).

---

### Python Code:


"""


from fractions import Fraction

# Let x = grain per bundle of upper grain (上禾實一秉)
# Let y = grain per bundle of lower grain (下禾實一秉)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Rearrange equations:
# 7x + 2y = 11  (from Equation 1)
# 2x + 8y = 9   (from Equation 2)

# Solve for x and y using substitution or elimination
# Multiply Equation 1 by 4 to align coefficients of y:
# 28x + 8y = 44
# Subtract Equation 2:
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)

# Substitute x into Equation 1 to solve for y:
# 7x + 2y = 11
# 7(Fraction(35, 26)) + 2y = 11
# Fraction(245, 26) + 2y = 11
# 2y = 11 - Fraction(245, 26)
# 2y = Fraction(286, 26) - Fraction(245, 26)
# 2y = Fraction(41, 26)
y = Fraction(41, 52)

# Results:
a = 7  # Upper grain bundles
b = x  # Grain per bundle of upper grain
c = 8  # Lower grain bundles
d = y  # Grain per bundle of lower grain

print(f"上禾 {a}秉 實 {b}斗 ，下禾 {c}秉 實 {d}斗 。")


"""


---

### Explanation of Results:
- \( x = \frac{35}{26} \): Grain per bundle of upper grain.
- \( y = \frac{41}{52} \): Grain per bundle of lower grain.
- Substituting these values back into the equations confirms the solution is correct.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
