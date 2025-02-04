"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 邪之適出
# 術曰：從、橫不出相乘，倍
積 = 從不出 * 橫不出 * 2

# 而開方除之
開方結果 = math.sqrt(積)

# 所得加從不出即戶廣
戶廣 = 開方結果 + 從不出

# 所得加橫不出即戶高
戶高 = 開方結果 + 橫不出

# 兩不出加之，得戶袤
戶袤 = 從不出 + 橫不出

# Convert 戶袤 to 丈 (1 丈 = 10 尺)
戶袤_丈 = Fraction(戶袤, 10)

# Results
a = 戶廣
b = 戶高
c = 戶袤_丈
#----- content ends here -----


"""

"""


"""
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
