"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "正負術" (positive-negative method) and "方程術" (method of simultaneous equations). Below is the Python implementation of the procedure:


"""


from fractions import Fraction

# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗，但總實滿斗
總實 = 1  # 1斗

# 方程術：設置未知數
# 設置上禾一秉實為 x，中禾一秉實為 y，下禾一秉實為 z
# 根據題意，建立方程組：
# 2x + y = 1
# x + 3y + z = 1
# y + 4z = 1

# 將方程組轉換為矩陣形式：
# [ 2  1  0 ] [x]   [1]
# [ 1  3  1 ] [y] = [1]
# [ 0  1  4 ] [z]   [1]

# 使用消元法求解
# Step 1: 消去第一列的非主元
a11, a12, a13, b1 = 2, 1, 0, 1
a21, a22, a23, b2 = 1, 3, 1, 1
a31, a32, a33, b3 = 0, 1, 4, 1

# 將第二行減去 (1/2) * 第一行
factor = Fraction(a21, a11)
a21 -= factor * a11
a22 -= factor * a12
a23 -= factor * a13
b2 -= factor * b1

# 更新矩陣
a21, a22, a23, b2 = 0, Fraction(5, 2), 1, Fraction(1, 2)

# Step 2: 消去第三列的非主元
factor = Fraction(a32, a22)
a32 -= factor * a22
a33 -= factor * a23
b3 -= factor * b2

# 更新矩陣
a32, a33, b3 = 0, Fraction(7, 2), Fraction(1, 2)

# Step 3: 回代求解
# 求 z
z = b3 / a33

# 求 y
y = (b2 - a23 * z) / a22

# 求 x
x = (b1 - a12 * y - a13 * z) / a11

# 結果
a = x
b = y
c = z

print(f"上禾一秉實 {a}斗，中禾一秉實 {b}斗，下禾一秉實 {c}斗。")


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is translated into a system of linear equations, represented as a matrix.
2. **Gaussian Elimination**: The elimination method is used to solve the system step by step:
   - Eliminate the first column's non-pivot elements.
   - Eliminate the second column's non-pivot elements.
   - Use back substitution to solve for the variables.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the problem involves rational numbers.

### Final Answer:
The values of `a`, `b`, and `c` represent the amount of斗 (volume) for one秉 of上禾,中禾, and下禾 respectively.
"""


"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 3/7
Variable 'b' has wrong value. Expected: 7/25, Actual: 1/7
Variable 'c' has wrong value. Expected: 4/25, Actual: 1/7"""
