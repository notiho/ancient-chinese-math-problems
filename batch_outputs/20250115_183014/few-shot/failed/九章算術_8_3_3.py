"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
術曰：如方程，置上禾五秉正，下禾七秉負，損實一斗一升正。次置上禾七秉正，下禾五秉負，損實二斗五升正。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese "fangcheng" (matrix-like) methods. Let's break it down step by step and encode it into Python.

The problem involves two equations derived from the given conditions:

1. \( 5x - 7y = 1斗1升 \)  
2. \( 7x - 5y = 2斗5升 \)

Where:
- \( x \) is the amount of grain per秉 (sheaf) for the "上禾" (upper grain).
- \( y \) is the amount of grain per秉 (sheaf) for the "下禾" (lower grain).

The solution involves using the "正負術" (positive-negative method), which is equivalent to solving a system of linear equations. Let's implement this step by step.

---


"""


from fractions import Fraction

# Convert given quantities into fractions of dou (1斗 = 10升)
損實1 = Fraction(1, 1) + Fraction(1, 10)  # 1斗1升
損實2 = Fraction(2, 1) + Fraction(5, 10)  # 2斗5升

# Coefficients for the equations
# Equation 1: 5x - 7y = 損實1
上禾1 = 5
下禾1 = -7
實1 = 損實1

# Equation 2: 7x - 5y = 損實2
上禾2 = 7
下禾2 = -5
實2 = 損實2

# Step 1: Eliminate one variable (y) using the 正負術
# Multiply the first equation by 7 (coefficient of x in the second equation)
# Multiply the second equation by 5 (coefficient of x in the first equation)
# Subtract to eliminate x
上禾法 = 上禾1 * 下禾2 - 上禾2 * 下禾1  # Coefficient for y
下禾法 = 實1 * 下禾2 - 實2 * 下禾1       # Resulting constant term

# Solve for y (下禾 per 秉)
下禾實 = Fraction(下禾法, 上禾法)

# Step 2: Solve for x (上禾 per 秉) using one of the original equations
# Use the first equation: 5x - 7y = 損實1
上禾實 = Fraction(實1 - 下禾1 * 下禾實, 上禾1)

# Convert results into斗 and升
a斗 = 上禾實.numerator // 上禾實.denominator  # Whole斗 for 上禾
a升 = (上禾實 - a斗).numerator * 10 // 上禾實.denominator  # Remaining升 for 上禾

c斗 = 下禾實.numerator // 下禾實.denominator  # Whole斗 for 下禾
c升 = (下禾實 - c斗).numerator * 10 // 下禾實.denominator  # Remaining升 for 下禾

# Final answer
a = a斗
b = a升
c = c斗
d = c升

print(f"上禾實: {a}斗 {b}升")
print(f"下禾實: {c}斗 {d}升")


"""


---

### Explanation of the Code:

1. **Input Conversion**: The given quantities (1斗1升 and 2斗5升) are converted into fractions for precise calculations.
2. **Elimination**: The "正負術" is used to eliminate one variable (y) by multiplying and subtracting the equations.
3. **Back Substitution**: After solving for \( y \), substitute it back into one of the original equations to solve for \( x \).
4. **Conversion to斗 and升**: The results are converted back into the traditional units of斗 and升 for the final answer.

### Final Answer:
The program will output the values of \( x \) (上禾實) and \( y \) (下禾實) in斗 and升.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'b' has wrong value. Expected: 5, Actual: 9
Variable 'c' has wrong value. Expected: 1, Actual: 0
Variable 'd' has wrong value. Expected: 2, Actual: 5"""
