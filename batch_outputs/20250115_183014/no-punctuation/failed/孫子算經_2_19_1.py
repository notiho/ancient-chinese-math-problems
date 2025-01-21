"""
今有積三萬五千步問為圓幾何
術曰置積三萬五千步以一十二乘之得四十二萬為實次借一算為下法步之超一位至百而止上商置六百于實之上副置六萬于實之下下法之上名為方法命上商六百除實除訖倍方法方法一退下法再退復置上商四十以次前商副置四百于方法之下下法之上名為廉法方廉各命上商四十以除實除訖倍廉法從方法方法一退下法再退復置上商八次前商副置八于方法之下下法之上名為隅法方廉隅各命上商八以除實除訖倍隅法從方法上商得六百四十八下法得一千二百九十六不盡九十六是為方六百四十八步一千二百九十六分步之九十六
答曰 a步 
"""

"""
Suppose there is an area of 35,000 bu. Question: what is the diameter of the circle?

The procedure says: Place the area of 35,000 bu. Multiply it by 12, obtaining 420,000 as the dividend. 
Next, borrow one counting rod to form the divisor. The divisor starts from 100 and increases by one place value.
Take the quotient and place 600 above the dividend. Place 60,000 below the dividend as the auxiliary.
The divisor above is called the "method divisor."
Command the quotient 600 to divide the dividend. After completing the division, double the method divisor.
The method divisor retreats one place, and the divisor retreats two places.
Repeat the process with the next quotient (40), and so on, until the calculation is complete.

The answer says: the diameter is *a* bu.
"""

from fractions import Fraction

# 積三萬五千步
積 = 35000

# 以一十二乘之，得四十二萬為實
實 = 12 * 積

# 初始下法步之超一位至百而止
下法 = 100

# 上商置六百
上商1 = 600

# 副置六萬于實之下
副1 = 60000

# 倍方法
方法1 = 上商1 * 下法

# 方法一退，下法再退
方法1退 = 方法1 // 10
下法退1 = 下法 * 10

# 上商置四十
上商2 = 40

# 副置四百于方法之下
副2 = 400

# 倍廉法
廉法 = 上商2 * 下法退1

# 廉法一退，下法再退
廉法退 = 廉法 // 10
下法退2 = 下法退1 * 10

# 上商置八
上商3 = 8

# 副置八于方法之下
副3 = 8

# 倍隅法
隅法 = 上商3 * 下法退2

# 最終計算
方 = 上商1 + 上商2 + 上商3
分子 = 隅法 % 下法退2
分母 = 下法退2

# 結果
a = Fraction(方) + Fraction(分子, 分母)
"""
Variable 'a' has wrong value. Expected: 17498/27, Actual: 648"""
