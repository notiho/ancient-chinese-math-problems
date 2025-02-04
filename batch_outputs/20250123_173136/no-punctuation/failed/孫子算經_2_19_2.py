"""
今有積三萬五千步問為圓幾何
術曰置積三萬五千步以一十二乘之得四十二萬為實次借一算為下法步之超一位至百而止上商置六百于實之上副置六萬于實之下下法之上名為方法命上商六百除實除訖倍方法方法一退下法再退復置上商四十以次前商副置四百于方法之下下法之上名為廉法方廉各命上商四十以除實除訖倍廉法從方法方法一退下法再退復置上商八次前商副置八于方法之下下法之上名為隅法方廉隅各命上商八以除實除訖倍隅法從方法上商得六百四十八下法得一千二百九十六不盡九十六是為方六百四十八步一千二百九十六分步之九十六
答曰 a步 
"""

"""
Suppose there is an area of 35,000 bu. Question: what is the diameter of the circle?

The procedure says:
1. Place the area of 35,000 bu and multiply it by 12, obtaining 420,000 as the dividend.
2. Borrow one counting rod to serve as the divisor. Shift the divisor one place to the left (to the hundreds place) and stop.
3. Divide the dividend by the divisor, obtaining the quotient 600. Place 600 above the dividend as the quotient, and place 60,000 below the dividend as the auxiliary.
4. Subtract the auxiliary from the dividend, leaving the remainder. Double the divisor (method divisor), and shift the divisor one place to the right.
5. Repeat the process by placing the next quotient (40) and continue dividing, updating the divisor (lian divisor).
6. Continue the process with the next quotient (8), updating the divisor (yu divisor).
7. After completing the division, the final quotient is 648, and the remainder is 96. The divisor is 1,296.

The answer says: the diameter is *a* bu, with a fractional remainder of 96/1,296 bu.
"""

from fractions import Fraction

# 積三萬五千步
積 = 35000

# 以一十二乘之，得四十二萬為實
實 = 積 * 12

# 初始下法
下法 = 100  # Shift divisor to the hundreds place

# 上商置六百
上商1 = 600
副1 = 上商1 * 下法  # 副置六萬于實之下
實 -= 副1  # Subtract auxiliary from dividend

# 倍方法，方法一退，下法再退
方法 = 下法 * 2
下法 //= 10

# 上商置四十
上商2 = 40
副2 = 上商2 * 方法  # 副置四百于方法之下
實 -= 副2  # Subtract auxiliary from dividend

# 倍廉法，方法一退，下法再退
廉法 = 方法 * 2
方法 //= 10
下法 //= 10

# 上商置八
上商3 = 8
副3 = 上商3 * 廉法  # 副置八于方法之下
實 -= 副3  # Subtract auxiliary from dividend

# 倍隅法
隅法 = 廉法 * 2

# 最終結果
a = 648 + Fraction(實, 隅法)  # Diameter = 648 + remainder/divisor
"""
Variable 'a' has wrong value. Expected: 17498/27, Actual: 1084"""
