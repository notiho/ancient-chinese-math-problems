"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a(=9/25)斗 ，中禾一秉實 b(=7/25)斗 ，下禾一秉實 c(=4/25)斗 。
"""

"""
Suppose there are 2 bundles of upper-grade grain, 3 bundles of middle-grade grain, and 4 bundles of lower-grade grain, but none of them are full dou.
If one bundle of upper-grade grain is taken from the middle-grade grain, one bundle of middle-grade grain is taken from the lower-grade grain, and one bundle of lower-grade grain is taken from the upper-grade grain, then the total becomes a full dou.
Question: how much does one bundle of upper-grade, middle-grade, and lower-grade grain weigh respectively?

The procedure says: Treat this as a system of equations. For each, place what is taken and use the positive-negative method to solve.
The positive-negative method says: When the names are the same, divide. When the names are different, add. If there is no positive, subtract the negative. If there is no negative, subtract the positive.
When the names are different, divide. When the names are the same, add. If there is no positive, add the positive. If there is no negative, add the negative.

The system of equations method says: Place 3 bundles of upper-grade grain, 2 bundles of middle-grade grain, and 1 bundle of lower-grade grain, with a total of 39/25 dou, on the right-hand side.
The middle and left grains are arranged similarly to the right-hand side.
Multiply the upper-grade grain row by the middle-grade grain row and divide directly. Then multiply the next row and divide directly again.
Then, multiply the middle-grade grain row by the lower-grade grain row and divide directly.
For the lower-grade grain row, if it is not exact, take the upper-grade grain as the divisor and the lower-grade grain as the dividend. The result is the actual value of the lower-grade grain.
To find the middle-grade grain, multiply the divisor by the middle-grade grain row and divide by the actual value of the lower-grade grain. The remainder, divided by the number of middle-grade grain bundles plus one, gives the actual value of the middle-grade grain.
To find the upper-grade grain, multiply the divisor by the upper-grade grain row and divide by the actual values of the lower-grade and middle-grade grains. The remainder, divided by the number of upper-grade grain bundles plus one, gives the actual value of the upper-grade grain.
The actual values are all as per the procedure.

Answer: One bundle of upper-grade grain weighs *a*(=9/25) dou, one bundle of middle-grade grain weighs *b*(=7/25) dou, and one bundle of lower-grade grain weighs *c*(=4/25) dou.
"""

from fractions import Fraction

# 上禾、 中禾、 下禾的秉數
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 總實滿斗
總實 = Fraction(1)  # 1斗 = 25/25斗

# 方程式
# 2 * 上禾 + 1 * 中禾 = 1斗
# 1 * 上禾 + 3 * 中禾 + 1 * 下禾 = 1斗
# 4 * 下禾 + 1 * 上禾 = 1斗

# 設置方程式矩陣
# | 2  1  0 |   | 上禾 |   = | 25/25 |
# | 1  3  1 | * | 中禾 |   = | 25/25 |
# | 1  0  4 |   | 下禾 |   = | 25/25 |

# 消元法求解
# 1. 消去第一列的下禾
# 2. 消去第二列的上禾
# 3. 求解下禾、中禾、上禾

# 初始矩陣
矩陣 = [
    [2, 1, 0, Fraction(25, 25)],  # 2 * 上禾 + 1 * 中禾 = 1斗
    [1, 3, 1, Fraction(25, 25)],  # 1 * 上禾 + 3 * 中禾 + 1 * 下禾 = 1斗
    [1, 0, 4, Fraction(25, 25)],  # 1 * 上禾 + 4 * 下禾 = 1斗
]

# 消元法
# 步驟 1: 消去第一列的下禾
矩陣[1] = [
    矩陣[1][i] - 矩陣[0][i] * Fraction(1, 2) for i in range(4)
]  # 第二行 - (第一行 * 1/2)
矩陣[2] = [
    矩陣[2][i] - 矩陣[0][i] * Fraction(1, 2) for i in range(4)
]  # 第三行 - (第一行 * 1/2)

# 步驟 2: 消去第二列的上禾
矩陣[2] = [
    矩陣[2][i] - 矩陣[1][i] * Fraction(1, 3) for i in range(4)
]  # 第三行 - (第二行 * 1/3)

# 步驟 3: 求解下禾
下禾 = 矩陣[2][3] / 矩陣[2][2]

# 步驟 4: 求解中禾
中禾 = (矩陣[1][3] - 矩陣[1][2] * 下禾) / 矩陣[1][1]

# 步驟 5: 求解上禾
上禾 = (矩陣[0][3] - 矩陣[0][1] * 中禾 - 矩陣[0][2] * 下禾) / 矩陣[0][0]

# 答案
a = 上禾  # 9/25斗
b = 中禾  # 7/25斗
c = 下禾  # 4/25斗
"""
Variable 'a' has wrong value. Expected: 9/25, Actual: 23/55
Variable 'b' has wrong value. Expected: 7/25, Actual: 9/55
Variable 'c' has wrong value. Expected: 4/25, Actual: 1/11"""
