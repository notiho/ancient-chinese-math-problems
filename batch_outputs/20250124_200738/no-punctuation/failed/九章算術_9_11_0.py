"""
今有戶不知高廣竿不知長短橫之不出四尺從之不出二尺邪之適出問戶高廣袤各幾何
術曰從橫不出相乘倍而開方除之所得加從不出即戶廣加橫不出即戶高兩不出加之得戶袤
荅曰廣 a尺 高 b尺 袤 c丈 
"""

#----- content starts here -----
"""
Suppose there is a door of unknown height and width, and a pole of unknown length.
When placed horizontally, it does not extend beyond the door by 4 chi.
When placed vertically, it does not extend beyond the door by 2 chi.
When placed diagonally, it just fits.
Question: what are the width, height, and diagonal length of the door?

The procedure says: Multiply the horizontal and vertical "does not extend" values together, double the result, and take the square root.
Divide the square root by 1.
Add the vertical "does not extend" value to the result to obtain the door's width.
Add the horizontal "does not extend" value to the result to obtain the door's height.
Add both "does not extend" values together to obtain the diagonal length of the door.

Answer: the width is *a* chi, the height is *b* chi, and the diagonal length is *c* zhang.
"""

from fractions import Fraction
import math

# 橫之不出四尺
橫不出 = 4

# 從之不出二尺
從不出 = 2

# 橫不出相乘倍
相乘倍 = 2 * (橫不出 * 從不出)

# 開方
平方根 = math.sqrt(float(Fraction(相乘倍)))

# 所得加從不出即戶廣
戶廣 = 平方根 + 從不出

# 加橫不出即戶高
戶高 = 平方根 + 橫不出

# 兩不出加之得戶袤
戶袤 = 橫不出 + 從不出

# Convert 戶袤 from chi to zhang (1 zhang = 10 chi)
戶袤 = Fraction(戶袤, 10)

a = Fraction(戶廣)
b = Fraction(戶高)
c = Fraction(戶袤)#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
