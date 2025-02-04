"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
術曰：置積二十三萬四千五百六十七步，為實，次借一算為下法，步之超一位至百而止。上商置四百于實之上，副置四萬于實之下。下法之商，名為方法；命上商四百除實，除訖，倍方法，方法一退，下法再退，復置上商八十以次前商，副置八百于方法之下。下法之上，名為廉法；方廉各命上商八十以除實，除訖，倍廉法，從方法，方法一退，下法再退，復置上商四以次前，副置四于方法之下。下法之上，名曰隅法；方廉隅各命上商四以除實，除訖，倍隅法，從方法，上商得四百八十四，下法得九百六十八，不盡三百一十一，是為方四百八十四步九百六十八分步之三百一十一。
答曰： a(=468823/968)步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 234567 bu. 
Question: what is the side length of the square?

The procedure says: Place the volume of 234567 bu as the dividend. 
Next, borrow a counter as the divisor, shifting the digits of the volume one place to the left until stopping at the hundreds place. 
Place the first quotient, 400, above the dividend, and place 40000 below the dividend as the auxiliary. 
The quotient of the divisor is called the side length. 
Divide the dividend by the first quotient, completing the division. 
Double the side length, decrement the side length by one place, and decrement the divisor by two places. 
Place the next quotient, 80, next to the previous quotient, and place 800 below the side length as the auxiliary. 
The divisor above is called the edge divisor. 
Divide the dividend by the next quotient, completing the division. 
Double the edge divisor, combine it with the side length, decrement the side length by one place, and decrement the divisor by two places. 
Place the next quotient, 4, next to the previous quotient, and place 4 below the side length as the auxiliary. 
The divisor above is called the corner divisor. 
Divide the dividend by the next quotient, completing the division. 
The final quotient is 484, and the divisor is 968. The remainder is 311. 
This gives the side length as 484 bu, with a fractional part of 311/968.

Answer: *a*(=468823/968) bu.
"""

from fractions import Fraction

# 置積二十三萬四千五百六十七步，為實
積 = 234567

# 初始方法
方法 = 0

# 初始下法
下法 = 0

# 上商置四百于實之上
上商1 = 400

# 副置四萬于實之下
副1 = 40000

# 方法更新
方法 += 上商1

# 下法更新
下法 += 副1

# 命上商四百除實，除訖
積 -= 上商1 * 副1

# 倍方法，方法一退，下法再退
方法 *= 2
方法 //= 10
下法 //= 100

# 復置上商八十以次前商
上商2 = 80

# 副置八百于方法之下
副2 = 800

# 方法更新
方法 += 上商2

# 下法更新
下法 += 副2

# 方廉各命上商八十以除實，除訖
積 -= 上商2 * 副2

# 倍廉法，從方法，方法一退，下法再退
方法 *= 2
方法 //= 10
下法 //= 100

# 復置上商四以次前
上商3 = 4

# 副置四于方法之下
副3 = 4

# 方法更新
方法 += 上商3

# 下法更新
下法 += 副3

# 方廉隅各命上商四以除實，除訖
積 -= 上商3 * 副3

# 最終結果
a = Fraction(方法 * 下法 + 積, 下法)  # 468823/968#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 468823/968, Actual: -15828873/16"""
