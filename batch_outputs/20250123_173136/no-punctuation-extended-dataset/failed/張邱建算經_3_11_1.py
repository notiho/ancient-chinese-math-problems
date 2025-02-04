"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰上錦一疋直絹 a疋 中錦一疋直絹 b疋 下錦一疋直絹 c疋
"""

"""
This problem is a classic system of linear equations, solved using the ancient Chinese method of elimination, as described in the "方程術" (method of solving linear equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# 上錦、中錦、下錦的系數和直絹的數據
# 第一組數據
上1, 中1, 下1, 直絹1 = 3, 2, 1, 45
# 第二組數據
上2, 中2, 下2, 直絹2 = 2, 3, 1, 43
# 第三組數據
上3, 中3, 下3, 直絹3 = 1, 2, 3, 35

# 按照方程術進行消元法求解
# Step 1: 消去下錦 (下禾)
# 用第一行的下錦系數消去第二行和第三行的下錦
因數2 = Fraction(下2, 下1)
因數3 = Fraction(下3, 下1)

# 更新第二行
上2 -= 因數2 * 上1
中2 -= 因數2 * 中1
下2 -= 因數2 * 下1
直絹2 -= 因數2 * 直絹1

# 更新第三行
上3 -= 因數3 * 上1
中3 -= 因數3 * 中1
下3 -= 因數3 * 下1
直絹3 -= 因數3 * 直絹1

# Step 2: 消去中錦 (中禾)
# 用第二行的中錦系數消去第三行的中錦
因數3_2 = Fraction(中3, 中2)

# 更新第三行
上3 -= 因數3_2 * 上2
中3 -= 因數3_2 * 中2
直絹3 -= 因數3_2 * 直絹2

# Step 3: 求解下錦、中錦、上錦的價值
# 求下錦的價值
c = Fraction(直絹3, 下3)

# 求中錦的價值
b = Fraction(直絹2 - 下2 * c, 中2)

# 求上錦的價值
a = Fraction(直絹1 - 中1 * b - 下1 * c, 上1)

# 答案
print(f"上錦一疋直絹 {a} 疋")
print(f"中錦一疋直絹 {b} 疋")
print(f"下錦一疋直絹 {c} 疋")


"""


### Explanation of the Code:
1. **Input Data**: The coefficients of the equations are taken from the problem statement. Each equation corresponds to the relationship between the quantities of 上錦, 中錦, 下錦, and the total number of 直絹.
2. **Elimination**: Following the ancient Chinese elimination method, we first eliminate the coefficients of 下錦 (下禾) from the second and third equations, then eliminate 中錦 (中禾) from the third equation.
3. **Back Substitution**: After elimination, we solve for 下錦 (c), then use it to solve for 中錦 (b), and finally solve for 上錦 (a).
4. **Output**: The values of `a`, `b`, and `c` represent the number of 直絹 corresponding to one unit of 上錦, 中錦, and 下錦, respectively.

### Answer:
The values of `a`, `b`, and `c` will be printed as fractions, representing the exact solution to the problem.
"""


"""
Code error: Fraction(-108, 0)"""
