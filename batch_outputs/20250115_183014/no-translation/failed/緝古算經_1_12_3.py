"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
術曰：以四十二乘斛法，以乘粟，七十五而一，為方亭積。令方差自乘，三而一，為隅陽冪，以截多乘之，減積，余為實。以多乘差，加冪，為方法。多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This problem is quite complex and involves ancient Chinese mathematical techniques for solving cubic equations. I'll translate the procedure into Python code step by step, adhering to the structure of the procedure ("術") provided.


"""


from fractions import Fraction
from math import isqrt

# 粟五千一百四十石
粟 = 5140

# 以四十二乘斛法
斛法 = 42

# 以乘粟，七十五而一，為方亭積
方亭積 = Fraction(斛法 * 粟, 75)

# 深少於下方七尺，多於上方一丈四尺
深差 = Fraction(7, 10)  # 7尺 = 7/10丈
深多 = Fraction(14, 10)  # 1丈4尺 = 14/10丈

# 令方差自乘，三而一，為隅陽冪
方差 = Fraction(1, 1)  # Placeholder for 方差 (to be solved later)
隅陽冪 = Fraction(方差**2, 3)

# 以截多乘之，減積，余為實
截多 = 深多 - 深差
實 = 方亭積 - 截多 * 隅陽冪

# 以多乘差，加冪，為方法
方法 = 截多 * 方差 + 隅陽冪

# 多加差，為廉法
廉法 = 截多 + 方差

# 從。開立方除之，即上方
上方 = (實 / 方法) ** Fraction(1, 3)

# 加差，即合所問
下方 = 上方 + 方差
深 = 上方 + 深差

# Convert results to simpler forms
a = 上方
b = 下方
c = 深

# Output results
print(f"上方徑各 {a} 尺")
print(f"下方徑各 {b} 丈")
print(f"深各 {c} 丈")


"""


This code follows the ancient procedure step by step, using Python's `Fraction` class to handle precise arithmetic and avoid floating-point errors. Note that some parts of the problem require solving for unknowns (e.g., 方差), which would typically involve iterative or algebraic methods. If you have specific values for these unknowns or additional details, they can be incorporated into the solution.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 14.069926649316885
Variable 'b' has wrong value. Expected: 14/5, Actual: 15.069926649316885
Variable 'c' has wrong value. Expected: 21/10, Actual: 14.769926649316885"""
