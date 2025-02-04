"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of matrix manipulation. Below is the solution translated into Python code:


"""


from fractions import Fraction

# 武馬一匹, 中馬二匹, 下馬三匹
武馬 = 1
中馬 = 2
下馬 = 3

# 每匹馬載 40 石，皆不能上
載重 = 40

# 借力關係：
# 武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，皆能上
# 方程術：設武馬、中馬、下馬的力分別為 x, y, z

# 方程組：
# 1. 武馬 + 中馬 = 40
# 2. 中馬 + 下馬 = 40
# 3. 下馬 + 武馬 = 40

# 將方程組轉換為矩陣形式：
# x + y       = 40
#     y + z   = 40
# z     + x   = 40

# 初始化矩陣
# [ 1  1  0 | 40 ]
# [ 0  1  1 | 40 ]
# [ 1  0  1 | 40 ]
矩陣 = [
    [1, 1, 0, 40],  # 武馬 + 中馬 = 40
    [0, 1, 1, 40],  # 中馬 + 下馬 = 40
    [1, 0, 1, 40],  # 下馬 + 武馬 = 40
]

# 方程術：消元法
# Step 1: 消去第一列以下的第一個變量
for i in range(1, 3):
    倍數 = Fraction(矩陣[i][0], 矩陣[0][0])
    for j in range(4):
        矩陣[i][j] -= 倍數 * 矩陣[0][j]

# Step 2: 消去第三列的第二個變量
倍數 = Fraction(矩陣[2][1], 矩陣[1][1])
for j in range(4):
    矩陣[2][j] -= 倍數 * 矩陣[1][j]

# Step 3: 回代求解
z = Fraction(矩陣[2][3], 矩陣[2][2])  # 下馬的力
y = Fraction(矩陣[1][3] - 矩陣[1][2] * z, 矩陣[1][1])  # 中馬的力
x = Fraction(矩陣[0][3] - 矩陣[0][1] * y, 矩陣[0][0])  # 武馬的力

# 結果
a = x
b = y
c = z

# 答案
print(f"武馬一匹力引 {a} 石，中馬一匹力引 {b} 石，下馬一匹力引 {c} 石。")


"""


### Explanation of the Code:
1. **Matrix Initialization**: The equations are represented as a matrix, where each row corresponds to an equation.
2. **Elimination**: The first variable (`x`) is eliminated from the second and third rows, and then the second variable (`y`) is eliminated from the third row.
3. **Back Substitution**: The values of `z`, `y`, and `x` are calculated by substituting back into the equations.
4. **Result**: The values of `x`, `y`, and `z` represent the pulling force of 武馬 (a), 中馬 (b), and 下馬 (c), respectively.

### Final Answer:
武馬一匹力引 `a` 石，中馬一匹力引 `b` 石，下馬一匹力引 `c` 石.
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
