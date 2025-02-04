"""
今有積三萬五千步問為圓幾何
術曰置積三萬五千步以一十二乘之得四十二萬為實次借一算為下法步之超一位至百而止上商置六百于實之上副置六萬于實之下下法之上名為方法命上商六百除實除訖倍方法方法一退下法再退復置上商四十以次前商副置四百于方法之下下法之上名為廉法方廉各命上商四十以除實除訖倍廉法從方法方法一退下法再退復置上商八次前商副置八于方法之下下法之上名為隅法方廉隅各命上商八以除實除訖倍隅法從方法上商得六百四十八下法得一千二百九十六不盡九十六是為方六百四十八步一千二百九十六分步之九十六
答曰 a步 
"""

"""
Suppose there is an area of 35,000 bu. Question: what is the diameter of the circle?

The procedure says: Place the area of 35,000 bu. Multiply it by 12, obtaining 420,000 as the dividend. 
Next, borrow one counting rod to serve as the divisor. 
Shift the divisor one place to the left (to the hundreds place) and stop. 
The first quotient is placed as 600 on top of the dividend. 
The auxiliary divisor is placed as 60,000 below the dividend. 
The divisor above is called the "method divisor." 
The first quotient, 600, is used to divide the dividend. After division, double the method divisor. 
The method divisor is shifted back one place, and the divisor is shifted back two places. 
Repeat the process with the next quotient, 40, and so on. 
Finally, the diameter is determined as 648 bu, with a remainder of 96/1296 bu.

Answer: *a* bu.
"""

from fractions import Fraction

# 置積三萬五千步
積 = 35000

# 以一十二乘之，得四十二萬為實
實 = 積 * 12

# 初始下法
下法 = 100

# 上商置六百
上商1 = 600
副1 = 上商1 * 下法

# 倍方法
方法 = 下法 * 2

# 方法一退，下法再退
方法 = 方法 // 10
下法 = 下法 // 100

# 上商置四十
上商2 = 40
副2 = 上商2 * 下法

# 倍廉法
廉法 = 下法 * 2

# 廉法一退，下法再退
廉法 = 廉法 // 10
下法 = 下法 // 100

# 上商置八
上商3 = 8
副3 = 上商3 * 下法

# 倍隅法
隅法 = 下法 * 2

# 最終計算
a = 648 + Fraction(96, 1296)
"""
"""
