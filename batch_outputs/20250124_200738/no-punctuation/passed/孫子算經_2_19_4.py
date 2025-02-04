"""
今有積三萬五千步問為圓幾何
術曰置積三萬五千步以一十二乘之得四十二萬為實次借一算為下法步之超一位至百而止上商置六百于實之上副置六萬于實之下下法之上名為方法命上商六百除實除訖倍方法方法一退下法再退復置上商四十以次前商副置四百于方法之下下法之上名為廉法方廉各命上商四十以除實除訖倍廉法從方法方法一退下法再退復置上商八次前商副置八于方法之下下法之上名為隅法方廉隅各命上商八以除實除訖倍隅法從方法上商得六百四十八下法得一千二百九十六不盡九十六是為方六百四十八步一千二百九十六分步之九十六
答曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 35,000 bu. Question: what is the diameter of the circle?

The procedure says: Place the area of 35,000 bu. Multiply it by 12, obtaining 420,000 as the dividend.
Next, borrow one counting rod as the divisor. Shift the divisor one place to the left until it reaches the hundreds place.
The first quotient is 600. Place 600 above the dividend. Place 60,000 below the dividend as the auxiliary.
The divisor above is called the "method divisor."
Use the first quotient, 600, to divide the dividend. After division, double the method divisor.
Shift the method divisor one place to the right, and shift the divisor two places to the right.
Next, place the second quotient, 40, above. Place 400 below the method divisor as the auxiliary.
The divisor above is called the "edge divisor."
Use the second quotient, 40, to divide the dividend. After division, double the edge divisor.
Shift the method divisor one place to the right, and shift the divisor two places to the right.
Next, place the third quotient, 8, above. Place 8 below the method divisor as the auxiliary.
The divisor above is called the "corner divisor."
Use the third quotient, 8, to divide the dividend. After division, double the corner divisor.
The final quotient is 648, and the divisor is 1,296. The remainder is 96.
Thus, the diameter is 648 bu and 96/1,296 bu.

Answer: *a* bu.
"""

from fractions import Fraction

# 置積三萬五千步
積 = 35000

# 以一十二乘之，得四十二萬為實
實 = 積 * 12

# 初始下法步之超一位至百而止
下法 = 100

# 上商置六百
上商1 = 600

# 副置六萬于實之下
副1 = 60000

# 方法命上商六百除實，除訖倍方法
方法 = 下法 * 上商1
實 -= 方法
方法 *= 2

# 方法一退，下法再退
方法 //= 10
下法 //= 100

# 上商置四十
上商2 = 40

# 副置四百于方法之下
副2 = 400

# 廉法命上商四十除實，除訖倍廉法
廉法 = 下法 * 上商2
實 -= 廉法
廉法 *= 2

# 方法一退，下法再退
方法 //= 10
下法 //= 100

# 上商置八
上商3 = 8

# 副置八于方法之下
副3 = 8

# 隅法命上商八除實，除訖倍隅法
隅法 = 下法 * 上商3
實 -= 隅法
隅法 *= 2

# 上商得六百四十八
上商 = 600 + 40 + 8

# 下法得一千二百九十六
下法 = 1296

# 不盡九十六
餘數 = 96

# 是為方六百四十八步一千二百九十六分步之九十六
a = Fraction(上商 * 下法 + 餘數, 下法)
#----- content ends here -----

"""
"""
