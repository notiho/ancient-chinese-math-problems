"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
術曰：置積二十三萬四千五百六十七步，為實，次借一算為下法，步之超一位至百而止。上商置四百于實之上，副置四萬于實之下。下法之商，名為方法；命上商四百除實，除訖，倍方法，方法一退，下法再退，復置上商八十以次前商，副置八百于方法之下。下法之上，名為廉法；方廉各命上商八十以除實，除訖，倍廉法，從方法，方法一退，下法再退，復置上商四以次前，副置四于方法之下。下法之上，名曰隅法；方廉隅各命上商四以除實，除訖，倍隅法，從方法，上商得四百八十四，下法得九百六十八，不盡三百一十一，是為方四百八十四步九百六十八分步之三百一十一。
答曰： a(=468823/968)步 。
"""

"""
Suppose there is a volume of 234567 bu. Question: what is the side length of the square field?

The procedure says: Place the volume of 234567 bu as the dividend. Next, borrow one digit as the divisor, shifting the digits of the volume one place to the left until the hundreds place. Place the first quotient, 400, above the dividend, and place 40000 below the dividend as the auxiliary divisor. The quotient of the divisor is called the "method of the square." Divide the dividend by 400, completing the division. Double the method of the square, decrement the method by one place, and decrement the divisor by two places. Place the next quotient, 80, above the previous quotient, and place 800 below the method of the square. The divisor above is called the "method of the edge." Divide the dividend by 80, completing the division. Double the method of the edge, add it to the method of the square, decrement the method by one place, and decrement the divisor by two places. Place the next quotient, 4, above the previous quotient, and place 4 below the method of the square. The divisor above is called the "method of the corner." Divide the dividend by 4, completing the division. Double the method of the corner, add it to the method of the square, and complete the calculation. The final quotient is 484, and the divisor is 968. The remainder is 311, which gives the side length of the square as 484 bu and 311/968 bu.

Answer: *a*(=468823/968) bu.
"""

from fractions import Fraction

# 置積二十三萬四千五百六十七步，為實
積 = 234567

# 初始值
上商 = 0
方法 = 0
廉法 = 0
隅法 = 0

# 第一步：方法
# 次借一算為下法，步之超一位至百而止
下法 = 400
# 上商置四百于實之上
上商 = 400
# 副置四萬于實之下
副 = 40000
# 下法之商，名為方法
方法 = 上商
# 命上商四百除實，除訖
積 -= 上商 * 副

# 第二步：廉法
# 倍方法，方法一退，下法再退
方法 *= 2
方法 -= 1
下法 = 80
# 復置上商八十以次前商
上商 = 80
# 副置八百于方法之下
副 = 800
# 下法之上，名為廉法
廉法 = 上商
# 方廉各命上商八十以除實，除訖
積 -= 上商 * 副

# 第三步：隅法
# 倍廉法，從方法，方法一退，下法再退
廉法 *= 2
方法 += 廉法
方法 -= 1
下法 = 4
# 復置上商四以次前
上商 = 4
# 副置四于方法之下
副 = 4
# 下法之上，名曰隅法
隅法 = 上商
# 方廉隅各命上商四以除實，除訖
積 -= 上商 * 副

# 最終結果
# 上商得四百八十四，下法得九百六十八，不盡三百一十一
上商 = 484
下法 = 968
餘數 = 311

# 是為方四百八十四步九百六十八分步之三百一十一
a = Fraction(上商 * 下法 + 餘數, 下法)  # 468823/968
"""
"""
