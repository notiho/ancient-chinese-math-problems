"""
假令有粟二萬六千三百四十二石四斗，欲作方窖六、圓窖四，令口小底大，方面與圓徑等，其深亦同，令深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問上下方、深數各多少？
術曰：以四十二乘斛法，以乘粟，三百八十四而一，為方亭積尺。令方差自乘，三而一，為隅陽冪。以多乘之，以減積，余為實。以多乘差，加冪，為方法。又以多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：方窖上方 a尺 ，下方 b丈 ，深 c丈 ，圓窖上下徑深與方窖同。
"""

"""
This is a complex ancient Chinese mathematical problem involving cubic measurements and solving for dimensions of square and circular silos. The problem requires solving for the dimensions of the upper side, lower side, and depth of the silos such that the total volume matches the given amount of millet. Below is the translation of the procedure into Python code.


"""


"""
Suppose there are 26,342 shi and 4 dou of millet, and it is desired to construct 6 square silos and 4 circular silos.
The silos are designed such that the top is smaller than the bottom, and the square silo's side length matches the diameter of the circular silo.
The depth is the same for both types of silos, and the depth is 7 chi less than the lower side and 14 chi more than the upper side.
The silos are filled completely, and the millet is used up exactly.
Question: What are the dimensions of the upper side, lower side, and depth?

The procedure says:
1. Multiply 42 by the hu divisor (斛法), then multiply by the millet amount. Divide by 384 to get the cubic chi for the square silo.
2. Let the difference between the upper and lower sides be the "difference" (差). Square the difference, divide by 3, and this gives the "corner increment" (隅陽冪).
3. Multiply the corner increment by the "excess" (多), subtract it from the cubic chi to get the "remainder" (實).
4. Multiply the excess by the difference, add the corner increment to get the "method for the square" (方法).
5. Add the excess to the difference to get the "method for the edge" (廉法).
6. Solve the cubic equation to find the upper side. Add the difference to the upper side to get the lower side. The depth is the excess.

Answer:
The square silo's upper side is *a* chi, the lower side is *b* chi, and the depth is *c* chi.
The circular silo's upper diameter, lower diameter, and depth are the same as the square silo.
"""
#ERR: misunderstood procedure
# 差, 多 are givens

from fractions import Fraction

# 粟二萬六千三百四十二石四斗
粟石 = 26342
粟斗 = 4
# Convert to dou (1 石 = 10 斗)
粟 = 10 * 粟石 + 粟斗

# 方窖六、圓窖四
方窖數 = 6
圓窖數 = 4

# 以四十二乘斛法
斛法 = 42

# 粟乘斛法
粟積 = 粟 * 斛法

# 三百八十四而一，為方亭積尺
方亭積尺 = Fraction(粟積, 384)

# 令深少於下方七尺，多於上方一丈四尺
深差下 = 7  # chi
深差上 = 14  # chi

# Initialize variables for solving
差 = None  # Difference between upper and lower sides
多 = None  # Depth (excess)
上方 = None  # Upper side
下方 = None  # Lower side
深 = None  # Depth

# Solve iteratively
for 差 in range(1, 100):  # Test differences (chi)
    for 多 in range(1, 100):  # Test depths (chi)
        # 令方差自乘，三而一，為隅陽冪
        隅陽冪 = Fraction(差**2, 3)

        # 以多乘之，以減積，余為實
        實 = 方亭積尺 - 多 * 隅陽冪

        # 以多乘差，加冪，為方法
        方法 = 多 * 差 + 隅陽冪

        # 又以多加差，為廉法
        廉法 = 多 + 差

        # Solve cubic equation: 上方^3 + 方法 * 上方 - 實 * 廉法 = 0
        for 上方 in range(1, 100):  # Test upper side (chi)
            if 上方**3 + 方法 * 上方 == 實 * 廉法:
                # Calculate 下方 and 深
                下方 = 上方 + 差
                深 = 多

                # Verify the depth conditions
                if 深 == 下方 - 深差下 and 深 == 上方 + 深差上:
                    a = 上方
                    b = 下方
                    c = 深
                    break

# Answer
print(f"方窖上方 {a} 尺，下方 {b} 尺，深 {c} 尺，圓窖上下徑深與方窖同。")


"""


This code systematically follows the ancient procedure to solve for the dimensions of the silos. It uses iterative testing to find the correct values for the upper side, lower side, and depth that satisfy the given conditions.
"""


"""
Timed out"""
