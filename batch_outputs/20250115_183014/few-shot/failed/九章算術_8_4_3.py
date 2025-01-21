"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾六秉正，下禾一十秉負，損實一斗八升正。次置上禾五秉負，下禾一十五秉正，損實五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
This problem involves solving a system of equations to determine the yield per bundle of "upper millet" (上禾) and "lower millet" (下禾). The procedure described is essentially an ancient Chinese method for solving simultaneous linear equations, which can be translated into Python code.

### Problem Breakdown:
- **Given**:
  - 6 bundles of upper millet lose 1 dou 8 sheng of grain, equivalent to 18 sheng, and correspond to 10 bundles of lower millet.
  - 15 bundles of lower millet lose 5 sheng of grain and correspond to 5 bundles of upper millet.
- **Question**:
  - What is the yield per bundle of upper millet and lower millet?

### Procedure:
The procedure involves setting up two equations based on the given relationships and solving them using elimination or substitution.

---


"""


from fractions import Fraction

# 上禾六秉正，下禾一十秉負，損實一斗八升正
# Equation 1: 6 * 上禾 - 10 * 下禾 = 18 (1斗8升 = 18升)
eq1_upper = 6
eq1_lower = -10
eq1_result = 18

# 上禾五秉負，下禾一十五秉正，損實五升正
# Equation 2: -5 * 上禾 + 15 * 下禾 = 5
eq2_upper = -5
eq2_lower = 15
eq2_result = 5

# Solve using elimination:
# Multiply Equation 1 by 5 and Equation 2 by 6 to align coefficients of 上禾
eq1_upper_scaled = eq1_upper * 5
eq1_lower_scaled = eq1_lower * 5
eq1_result_scaled = eq1_result * 5

eq2_upper_scaled = eq2_upper * 6
eq2_lower_scaled = eq2_lower * 6
eq2_result_scaled = eq2_result * 6

# Eliminate 上禾 by adding the two equations
combined_lower = eq1_lower_scaled + eq2_lower_scaled
combined_result = eq1_result_scaled + eq2_result_scaled

# Solve for 下禾
下禾 = Fraction(combined_result, combined_lower)

# Substitute 下禾 back into Equation 1 to solve for 上禾
上禾 = Fraction(eq1_result - (eq1_lower * 下禾), eq1_upper)

# Convert results to sheng per bundle
a = 上禾.numerator  # Upper millet yield numerator
b = 上禾.denominator  # Upper millet yield denominator
c = 下禾.numerator  # Lower millet yield numerator
d = 下禾.denominator  # Lower millet yield denominator

# Answer
print(f"上禾每秉實 {a}/{b} 升")
print(f"下禾每秉實 {c}/{d} 升")


"""


---

### Explanation of the Code:
1. **Equations Setup**:
   - The two equations are derived from the problem statement:
     - \( 6 \cdot 上禾 - 10 \cdot 下禾 = 18 \)
     - \( -5 \cdot 上禾 + 15 \cdot 下禾 = 5 \)

2. **Elimination**:
   - The coefficients of \( 上禾 \) are aligned by multiplying the first equation by 5 and the second by 6.
   - Adding the scaled equations eliminates \( 上禾 \), leaving an equation with only \( 下禾 \).

3. **Substitution**:
   - The value of \( 下禾 \) is substituted back into the first equation to solve for \( 上禾 \).

4. **Fraction Representation**:
   - The results are expressed as fractions to maintain precision, as required by the problem.

5. **Output**:
   - The yield per bundle of upper millet and lower millet is printed as fractions of sheng.

### Final Answer:
The yield per bundle of upper millet and lower millet is expressed in terms of \( a \), \( b \), \( c \), and \( d \), where:
- \( a/b \) is the yield of upper millet in sheng per bundle.
- \( c/d \) is the yield of lower millet in sheng per bundle.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 8
Variable 'b' has wrong value. Expected: 8, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 3, Actual: 1"""
