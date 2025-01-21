"""
今有麻九斗麥七斗菽三斗答二斗黍五斗直錢一百四十麻七斗麥六斗菽四斗答五斗黍三斗直錢一百二十八麻三斗麥五斗菽七斗答六斗黍四斗直錢一百一十六麻二斗麥五斗菽三斗答九斗黍四斗直錢一百一十二麻一斗麥三斗菽二斗答八斗黍五斗直錢九十五問一斗直幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰麻 a斗 b錢 麥 c斗 d錢 菽 e斗 f錢 答 g斗 h錢 黍 i斗 j錢 
"""

"""
This is a complex problem involving a system of linear equations, which is solved using the ancient Chinese method of elimination, known as the "fangcheng" (方程) method. Below is the step-by-step Python implementation of the procedure:


"""


from fractions import Fraction

# Input the coefficients of the equations
# 麻 (ma), 麥 (mai), 菽 (shu), 答 (da), 黍 (shu), and the total value in 錢 (qian)
equations = [
    [9, 7, 3, 2, 5, 140],  # 麻9斗, 麥7斗, 菽3斗, 答2斗, 黍5斗, 直錢140
    [7, 6, 4, 5, 3, 128],  # 麻7斗, 麥6斗, 菽4斗, 答5斗, 黍3斗, 直錢128
    [3, 5, 7, 6, 4, 116],  # 麻3斗, 麥5斗, 菽7斗, 答6斗, 黍4斗, 直錢116
    [2, 5, 3, 9, 4, 112],  # 麻2斗, 麥5斗, 菽3斗, 答9斗, 黍4斗, 直錢112
    [1, 3, 2, 8, 5, 95],   # 麻1斗, 麥3斗, 菽2斗, 答8斗, 黍5斗, 直錢95
]

# Step 1: Normalize the equations by dividing each row by the coefficient of the first variable (麻)
for i in range(len(equations)):
    divisor = equations[i][0]
    equations[i] = [Fraction(x, divisor) for x in equations[i]]

# Step 2: Eliminate the first variable (麻) from all rows except the first
for i in range(1, len(equations)):
    multiplier = equations[i][0]
    equations[i] = [equations[i][j] - multiplier * equations[0][j] for j in range(len(equations[i]))]

# Step 3: Eliminate the second variable (麥) from all rows except the first two
for i in range(2, len(equations)):
    multiplier = equations[i][1]
    equations[i] = [equations[i][j] - multiplier * equations[1][j] for j in range(len(equations[i]))]

# Step 4: Eliminate the third variable (菽) from all rows except the first three
for i in range(3, len(equations)):
    multiplier = equations[i][2]
    equations[i] = [equations[i][j] - multiplier * equations[2][j] for j in range(len(equations[i]))]

# Step 5: Eliminate the fourth variable (答) from all rows except the first four
for i in range(4, len(equations)):
    multiplier = equations[i][3]
    equations[i] = [equations[i][j] - multiplier * equations[3][j] for j in range(len(equations[i]))]

# Step 6: Back-substitute to solve for each variable
# Start with the last variable (黍)
黍 = equations[4][5] / equations[4][4]
答 = (equations[3][5] - equations[3][4] * 黍) / equations[3][3]
菽 = (equations[2][5] - equations[2][4] * 黍 - equations[2][3] * 答) / equations[2][2]
麥 = (equations[1][5] - equations[1][4] * 黍 - equations[1][3] * 答 - equations[1][2] * 菽) / equations[1][1]
麻 = (equations[0][5] - equations[0][4] * 黍 - equations[0][3] * 答 - equations[0][2] * 菽 - equations[0][1] * 麥) / equations[0][0]

# Convert the results to 鬥 and 錢
麻_斗 = int(麻)
麻_錢 = (麻 - 麻_斗) * 100

麥_斗 = int(麥)
麥_錢 = (麥 - 麥_斗) * 100

菽_斗 = int(菽)
菽_錢 = (菽 - 菽_斗) * 100

答_斗 = int(答)
答_錢 = (答 - 答_斗) * 100

黍_斗 = int(黍)
黍_錢 = (黍 - 黍_斗) * 100

# Output the results
a, b = 麻_斗, 麻_錢
c, d = 麥_斗, 麥_錢
e, f = 菽_斗, 菽_錢
g, h = 答_斗, 答_錢
i, j = 黍_斗, 黍_錢

print(f"麻 {a}斗 {b}錢")
print(f"麥 {c}斗 {d}錢")
print(f"菽 {e}斗 {f}錢")
print(f"答 {g}斗 {h}錢")
print(f"黍 {i}斗 {j}錢")


"""


This Python code implements the ancient Chinese "fangcheng" method to solve the system of linear equations. Each variable (麻, 麥, 菽, 答, 黍) is solved step by step, and the results are expressed in terms of 鬥 (dou) and 錢 (qian).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -119
Variable 'b' has wrong value. Expected: 7, Actual: -351160017874479820/5590603819401341
Variable 'c' has wrong value. Expected: 1, Actual: 149
Variable 'd' has wrong value. Expected: 4, Actual: 111834538017409190/5590603819401341
Variable 'e' has wrong value. Expected: 1, Actual: -2
Variable 'f' has wrong value. Expected: 3, Actual: -36145424917962350/5590603819401341
Variable 'g' has wrong value. Expected: 1, Actual: -7
Variable 'h' has wrong value. Expected: 5, Actual: -1752250505208700/33080495972789
Variable 'i' has wrong value. Expected: 1, Actual: 38
Variable 'j' has wrong value. Expected: 6, Actual: 223977331900/3194022977"""
