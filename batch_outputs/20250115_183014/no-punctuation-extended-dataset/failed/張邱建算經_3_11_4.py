"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰上錦 a疋 直絹 b疋 中錦 c疋 直絹 d疋 下錦 e疋 直絹 f疋
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text as "方程術" (method of solving simultaneous equations). Below is the Python implementation of the problem using the described procedure.


"""


from fractions import Fraction

# 上錦、中錦、下錦的疋數和直絹的疋數
# 第一條方程
上1, 中1, 下1, 直絹1 = 3, 2, 1, 45
# 第二條方程
上2, 中2, 下2, 直絹2 = 2, 3, 1, 43
# 第三條方程
上3, 中3, 下3, 直絹3 = 1, 2, 3, 35

# 方程術解法
# Step 1: 消去下錦 (Eliminate 下錦)
# Multiply the first equation by 下2 and the second equation by 下1, then subtract
法1 = 下2 * 直絹1 - 下1 * 直絹2
上法1 = 下2 * 上1 - 下1 * 上2
中法1 = 下2 * 中1 - 下1 * 中2

# Multiply the second equation by 下3 and the third equation by 下2, then subtract
法2 = 下3 * 直絹2 - 下2 * 直絹3
上法2 = 下3 * 上2 - 下2 * 上3
中法2 = 下3 * 中2 - 下2 * 中3

# Step 2: 消去中錦 (Eliminate 中錦)
# Multiply the first reduced equation by 中法2 and the second reduced equation by 中法1, then subtract
法3 = 中法2 * 法1 - 中法1 * 法2
上法3 = 中法2 * 上法1 - 中法1 * 上法2

# Solve for 上錦
上錦 = Fraction(法3, 上法3)

# Step 3: 求中錦 (Solve for 中錦)
中錦 = Fraction(法1 - 上法1 * 上錦, 中法1)

# Step 4: 求下錦 (Solve for 下錦)
下錦 = Fraction(直絹1 - 上1 * 上錦 - 中1 * 中錦, 下1)

# Step 5: 計算直絹 (Calculate the corresponding 直絹 values)
a = 上錦
b = Fraction(直絹1 - 中1 * 中錦 - 下1 * 下錦, 上1)
c = 中錦
d = Fraction(直絹2 - 上2 * 上錦 - 下2 * 下錦, 中2)
e = 下錦
f = Fraction(直絹3 - 上3 * 上錦 - 中3 * 中錦, 下3)

# Output the results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Input Equations**: The problem provides three equations based on the number of bolts of 上錦 (upper brocade), 中錦 (middle brocade), 下錦 (lower brocade), and the corresponding bolts of 直絹 (plain silk).
2. **Elimination Process**: The procedure eliminates one variable at a time (starting with 下錦, then 中錦) by multiplying and subtracting equations, as described in the "方程術".
3. **Back Substitution**: After reducing the system to one variable, the values of the other variables are calculated by substitution.
4. **Output**: The solution gives the number of bolts of 上錦, 中錦, 下錦, and their corresponding bolts of 直絹.

### Final Answer:
The values of `a`, `b`, `c`, `d`, `e`, and `f` represent the number of bolts of 上錦, 直絹 for 上錦, 中錦, 直絹 for 中錦, 下錦, and 直絹 for 下錦, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 9
Variable 'c' has wrong value. Expected: 1, Actual: 7
Variable 'e' has wrong value. Expected: 1, Actual: 4"""
