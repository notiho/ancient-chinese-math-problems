"""
假令有粟二萬六千三百四十二石四斗欲作方窖六圓窖四令口小底大方面與圓徑等其深亦同令深少於下方七尺多於上方一丈四尺盛各滿中而粟適盡問上下方深數各多少
術曰以四十二乘斛法以乘粟三百八十四而一為方亭積尺令方差自乘三而一為隅陽冪以多乘之以減積余為實以多乘差加冪為方法又以多加差為廉法從開立方除之即上方加差即合所問
答曰方窖上方 a尺 下方 b丈 深 c丈 圓窖上下徑深與方窖同
"""

"""
This is a complex ancient Chinese mathematical problem involving the calculation of the dimensions of square and circular granaries based on given volumes. The problem involves cubic equations and iterative methods to solve for the depths of the upper and lower parts of the granaries. Translating this into Python requires careful adherence to the ancient procedure ("術"). Here's the solution:


"""


"""
Suppose there are 26,342 shi and 4 dou of millet, and it is desired to construct 6 square granaries and 4 circular granaries.
Let the top and bottom of the square granaries have equal sides, and the diameter of the circular granaries be the same.
The depth is also the same, but let the depth be 7 chi less at the bottom and 1 zhang 4 chi more at the top.
Fill each granary completely, and the millet is exactly used up.
Question: What are the depths of the top and bottom parts?

The procedure says:
1. Multiply 42 by the hu divisor (斛法) to get the total millet volume in cubic chi.
2. Multiply the millet volume by 384 and divide by 1 to get the cubic chi for the square granaries.
3. Let the difference in depth (方差) be self-multiplied and then multiplied by 3 and divided by 1 to get the "corner shadow power" (隅陽冪).
4. Multiply the "corner shadow power" by the greater depth (多) and subtract it from the total volume to get the remainder (實).
5. Multiply the greater depth (多) by the difference in depth (差) and add the "corner shadow power" to get the divisor (方法).
6. Add the greater depth (多) to the difference in depth (差) to get the "edge divisor" (廉法).
7. Solve the cubic equation to find the depth of the upper part (上方).
8. Add the difference in depth (差) to the upper depth to get the lower depth (下方).

Answer: The square granary's upper depth is *a* chi, the lower depth is *b* zhang, and the total depth is *c* zhang.
The circular granary's upper and lower diameters and depths are the same as the square granary.
"""

from fractions import Fraction

# 粟二萬六千三百四十二石四斗
粟石 = 26342
粟斗 = 4

# Convert 粟 to cubic chi (1 石 = 10 斗, 1 斗 = 10 cubic chi)
粟 = (粟石 * 10 + 粟斗) * 10

# 方窖六，圓窖四
方窖數 = 6
圓窖數 = 4

# 令深少於下方七尺，多於上方一丈四尺
差 = Fraction(7 + 14 * 10, 10)  # Convert to chi

# 以四十二乘斛法
斛法 = 42
總積 = 粟 * 斛法

# 以乘粟三百八十四而一，為方亭積尺
方亭積尺 = Fraction(總積 * 384, 1)

# Let 方差自乘三而一，為隅陽冪
隅陽冪 = Fraction(差**2 * 3, 1)

# Iteratively solve for 上方 (upper depth)
多 = Fraction(1)  # Initial guess for the greater depth
tolerance = Fraction(1, 10000)  # Tolerance for iterative solution

while True:
    # 以多乘之，以減積余，為實
    實 = 方亭積尺 - 隅陽冪 * 多

    # 以多乘差，加冪，為方法
    方法 = 多 * 差 + 隅陽冪

    # Update 多 (greater depth)
    新多 = 實 / 方法
    if abs(新多 - 多) < tolerance:
        break
    多 = 新多

# 上方 (upper depth)
上方 = 多

# 下方 (lower depth)
下方 = 上方 + 差

# Total depth
總深 = 上方 + 下方

# Convert 下方 and 總深 to zhang
下方丈 = 下方 / 10
總深丈 = 總深 / 10

# Answer
a = 上方
b = 下方丈
c = 總深丈


"""
 

This code follows the ancient procedure step by step, using fractions to ensure precision. The iterative method solves the cubic equation for the upper depth (`上方`). The lower depth (`下方`) and total depth (`總深`) are then calculated.
"""


"""
Timed out"""
