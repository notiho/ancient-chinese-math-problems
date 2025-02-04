"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""

"""


from fractions import Fraction
from math import sqrt

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 從、橫不出相乘
積 = 橫不出 * 從不出

# 倍
積倍 = 2 * 積

# 開方除之
開方結果 = sqrt(積倍)

# 所得加從不出即戶廣
戶廣 = 開方結果 + 從不出

# 所得加橫不出即戶高
戶高 = 開方結果 + 橫不出

# 兩不出加之，得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤_丈 = Fraction(戶袤, 10)

# Final results
a = Fraction(戶廣)
b = Fraction(戶高)
c = Fraction(戶袤_丈)


"""

"""


"""
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
