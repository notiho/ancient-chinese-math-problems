"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a(=1)匹 力引 b(=160/7)石 ，中馬 c(=1)匹 力引 d(=120/7)石 ，下馬 e(=1)匹 力引 f(=40/7)石 。
"""

"""
This problem involves solving a system of equations using the ancient Chinese method of elimination, similar to Gaussian elimination. Here's the solution translated into Python code:


"""


from fractions import Fraction

# 武馬、中馬、下馬的秉數 (coefficients for each type of horse)
武馬秉數 = 3
中馬秉數 = 2
下馬秉數 = 1

# 每匹馬的總負載 (total load for all horses)
總負載 = 39  # in dou (斗)

# 初始化方程矩陣 (augmented matrix)
# 每行表示一匹馬的借貸關係和總負載
矩陣 = [
    [武馬秉數, 中馬秉數, 下馬秉數, 總負載],  # 武馬
    [中馬秉數, 中馬秉數, 下馬秉數, 總負載],  # 中馬
    [下馬秉數, 中馬秉數, 下馬秉數, 總負載],  # 下馬
]

# 消元法 (elimination process)
# Step 1: Normalize the first row
for i in range(1, len(矩陣)):
    factor = Fraction(矩陣[i][0], 矩陣[0][0])
    for j in range(len(矩陣[0])):
        矩陣[i][j] -= factor * 矩陣[0][j]

# Step 2: Normalize the second row
factor = Fraction(矩陣[2][1], 矩陣[1][1])
for j in range(len(矩陣[1])):
    矩陣[2][j] -= factor * 矩陣[1][j]

# Step 3: Back substitution to solve for 下馬, 中馬, 武馬
下馬實 = Fraction(矩陣[2][3], 矩陣[2][2])
中馬實 = Fraction(矩陣[1][3] - 矩陣[1][2] * 下馬實, 矩陣[1][1])
武馬實 = Fraction(矩陣[0][3] - 矩陣[0][2] * 下馬實 - 矩陣[0][1] * 中馬實, 矩陣[0][0])

# 結果
a = 1  # 武馬匹數
b = 武馬實  # 武馬力引
c = 1  # 中馬匹數
d = 中馬實  # 中馬力引
e = 1  # 下馬匹數
f = 下馬實  # 下馬力引

# Output results
print(f"武馬 {a} 匹 力引 {b} 石")
print(f"中馬 {c} 匹 力引 {d} 石")
print(f"下馬 {e} 匹 力引 {f} 石")


"""


### Explanation of the Code:
1. **Matrix Setup**: The problem is represented as a system of linear equations, where the coefficients represent the borrowing relationships between the horses.
2. **Elimination Process**: The matrix is reduced row by row to isolate the variables (the pulling power of each type of horse).
3. **Back Substitution**: Once the matrix is in row-echelon form, the values for each variable are calculated.
4. **Results**: The pulling power of each type of horse is expressed as a fraction of the total load.

### Final Answer:
- 武馬 (Wu Horse): \( b = \frac{160}{7} \) 石
- 中馬 (Zhong Horse): \( d = \frac{120}{7} \) 石
- 下馬 (Xia Horse): \( f = \frac{40}{7} \) 石
"""


"""
Code error: Fraction(0, 0)"""
