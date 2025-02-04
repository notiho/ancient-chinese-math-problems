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
邪之適出 = math.sqrt(橫不出**2 + 從不出**2)

# 術曰：從、橫不出相乘，倍
相乘倍 = 2 * 橫不出 * 從不出

# 而開方除之
開方值 = math.sqrt相乘倍

# 所得加從不出即戶廣
戶廣 = 開方值 + 橫不出#----- content ends here -----


"""

"""


"""
Code error: module 'math' has no attribute 'sqrt相乘倍'"""
