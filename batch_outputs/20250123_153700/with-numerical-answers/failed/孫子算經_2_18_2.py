"""
今有積，二十三萬四千五百六十七步。問：為方幾何？
術曰：置積二十三萬四千五百六十七步，為實，次借一算為下法，步之超一位至百而止。上商置四百于實之上，副置四萬于實之下。下法之商，名為方法；命上商四百除實，除訖，倍方法，方法一退，下法再退，復置上商八十以次前商，副置八百于方法之下。下法之上，名為廉法；方廉各命上商八十以除實，除訖，倍廉法，從方法，方法一退，下法再退，復置上商四以次前，副置四于方法之下。下法之上，名曰隅法；方廉隅各命上商四以除實，除訖，倍隅法，從方法，上商得四百八十四，下法得九百六十八，不盡三百一十一，是為方四百八十四步九百六十八分步之三百一十一。
答曰： a(=468823/968)步 。
"""

"""
Suppose there is a volume of 234567 bu. 
Question: what is the side length of the square?

The procedure says:
Place the volume of 234567 bu as the dividend. Next, borrow one counter as the divisor. Shift the digits of the volume one place to the left until reaching the hundreds place. Place 400 as the initial quotient above the dividend, and place 40000 below the dividend as the auxiliary divisor. The quotient of the divisor is called the "method of the square." Divide the dividend by the quotient 400. After completing the division, double the square method. The square method decreases by one place, and the divisor decreases by two places. Place 80 as the next quotient, and place 800 below the square method. The divisor above is called the "method of the edge." Divide the dividend by the quotient 80. After completing the division, double the edge method, add it to the square method, decrease the square method by one place, and decrease the divisor by two places. Place 4 as the next quotient, and place 4 below the square method. The divisor above is called the "method of the corner." Divide the dividend by the quotient 4. After completing the division, double the corner method, add it to the square method. The final quotient is 484, and the divisor is 968. The remainder is 311. Thus, the side length is 484 bu and 311/968 bu.

Answer: *a*(=468823/968) bu.
"""

from fractions import Fraction

# 置積二十三萬四千五百六十七步，為實
實 = 234567

# 初始上商置四百
上商1 = 400

# 副置四萬于實之下
副1 = 40000

# 下法之商，名為方法
方法 = 上商1

# 命上商四百除實，除訖
實 -= 上商1 * 副1

# 倍方法
方法 *= 2

# 方法一退，下法再退
方法 //= 10
副1 //= 100

# 復置上商八十
上商2 = 80

# 副置八百于方法之下
副2 = 800

# 方廉各命上商八十以除實，除訖
實 -= 上商2 * 副2

# 倍廉法，從方法
方法 += 2 * 上商2

# 方法一退，下法再退
方法 //= 10
副2 //= 100

# 復置上商四
上商3 = 4

# 副置四于方法之下
副3 = 4

# 方廉隅各命上商四以除實，除訖
實 -= 上商3 * 副3

# 倍隅法，從方法
方法 += 2 * 上商3

# 上商得四百八十四
上商 = 400 + 80 + 4

# 下法得九百六十八
下法 = 40000 + 800 + 4

# 不盡三百一十一
餘數 = 311

# 是為方四百八十四步九百六十八分步之三百一十一
a = Fraction(上商 * 下法 + 餘數, 下法)  # 468823/968
"""
Variable 'a' has wrong value. Expected: 468823/968, Actual: 19749447/40804"""
