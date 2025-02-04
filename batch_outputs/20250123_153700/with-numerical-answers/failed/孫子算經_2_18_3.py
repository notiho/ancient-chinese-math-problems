"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
術曰：置積二十三萬四千五百六十七步，為實，次借一算為下法，步之超一位至百而止。上商置四百于實之上，副置四萬于實之下。下法之商，名為方法；命上商四百除實，除訖，倍方法，方法一退，下法再退，復置上商八十以次前商，副置八百于方法之下。下法之上，名為廉法；方廉各命上商八十以除實，除訖，倍廉法，從方法，方法一退，下法再退，復置上商四以次前，副置四于方法之下。下法之上，名曰隅法；方廉隅各命上商四以除實，除訖，倍隅法，從方法，上商得四百八十四，下法得九百六十八，不盡三百一十一，是為方四百八十四步九百六十八分步之三百一十一。
答曰： a(=468823/968)步 。
"""

"""
Suppose there is a volume of 234567 bu. Question: what is the side length of the square?

The procedure says: Place the volume 234567 bu as the dividend. Next, borrow one counter as the divisor. Shift the digits of the volume one place to the left until reaching the hundreds place. Place the first quotient, 400, above the dividend, and place the square of 400, 40000, below the dividend. The quotient of the divisor is called the "method of the square." Divide the dividend by the first quotient, 400. After completing the division, double the method of the square. The method of the square is shifted one place to the left, and the divisor is shifted two places to the left. Place the next quotient, 80, above the previous quotient, and place the square of 80, 6400, below the method of the square. The divisor above is called the "method of the edge." Divide the dividend by the second quotient, 80. After completing the division, double the method of the edge and add it to the method of the square. The method of the square is shifted one place to the left, and the divisor is shifted two places to the left. Place the next quotient, 4, above the previous quotient, and place the square of 4, 16, below the method of the edge. The divisor above is called the "method of the corner." Divide the dividend by the third quotient, 4. After completing the division, double the method of the corner and add it to the method of the edge and the method of the square. The final quotient is 484, and the divisor is 968. The remainder is 311. Thus, the side length is 484 bu and 311/968 bu.

Answer: *a*(=468823/968) bu.
"""

from fractions import Fraction

# 積二十三萬四千五百六十七步
積 = 234567

# 方法
方法 = 0

# 下法
下法 = 0

# 上商置四百于實之上
上商1 = 400
方法 += 上商1

# 副置四萬于實之下
副1 = 上商1 ** 2
積 -= 副1

# 倍方法
方法 *= 2

# 方法一退，下法再退
方法 *= 10
下法 *= 100

# 復置上商八十以次前商
上商2 = 80
方法 += 上商2

# 副置八百于方法之下
副2 = 上商2 ** 2
積 -= 副2

# 倍廉法，從方法
方法 *= 2

# 方法一退，下法再退
方法 *= 10
下法 *= 100

# 復置上商四以次前
上商3 = 4
方法 += 上商3

# 副置四于方法之下
副3 = 上商3 ** 2
積 -= 副3

# 最終結果
a = Fraction(方法 * 1000 + 積, 下法 + 1000)  # 468823/968
"""
Variable 'a' has wrong value. Expected: 468823/968, Actual: 161672151/1000"""
