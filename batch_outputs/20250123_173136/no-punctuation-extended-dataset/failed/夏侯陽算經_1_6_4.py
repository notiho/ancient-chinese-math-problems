"""
今有田二十一頃七十八畞一百八十步問為方幾何
術曰先置頃畞於上以二百四十步乗之得五十二萬二千七百二十步内零一百八十步以開方除之借一算為下法步之超一位至百止萬上置上商七百下亦置七萬於實位之下下法之上命上商除實訖倍方為一十四萬方法一退下法再退又置上商二十於前商後又置二百於方法之下下法之上名曰隅法以方隅二法皆命上商以除實訖倍隅法為四百從上方法一退下法再退又置上商三扵前商二十之後又置三步於方法之下下法之上名曰隅法以方隅二法皆命上商除實訖倍隅法得六從上方法得一千四百四十六即是上方得七百二十三步奇一百七十一步
答曰 a步 奇 b步
"""

"""
Suppose there is a field of 21 qing, 78 mu, and 180 bu.
Question: what is the side length of the square field?

The procedure says:
First, place the qing and mu on top. Multiply by 240 bu to convert to total bu, obtaining 522,720 bu.
Add the remaining 180 bu to this total.
Perform square root extraction by division:
1. Borrow one digit for the divisor, and place it below. Start with the highest place value (hundreds) and proceed.
2. Place the quotient (商) above and multiply it back to subtract from the dividend.
3. Double the current divisor (方法) and adjust for the next digit.
4. Continue this process until the square root is fully extracted.

The answer says: the side length is *a* bu, with a remainder of *b* bu.
"""

from fractions import Fraction

# 田二十一頃七十八畞一百八十步
頃 = 21
畝 = 78
步 = 180

# 每畝240步
畝法 = 240

# 先置頃畝於上，以二百四十步乘之
總步數 = (頃 * 100 + 畝) * 畝法

# 得五十二萬二千七百二十步，內零一百八十步
總步數 += 步

# 開方計算
實 = 總步數
商 = 0
方法 = 0
位 = 100000  # Start with the highest place value for 商

while 位 > 0:
    # 借一算為下法步之超一位至百止萬
    下法 = 方法 * 2 * 位

    # 上置上商
    for 上商 in range(9, -1, -1):  # Try 商 from 9 to 0
        if (下法 + 上商 * 位) * 上商 <= 實:
            break

    # 更新商
    商 += 上商 * 位

    # 更新實
    實 -= (下法 + 上商 * 位) * 上商

    # 倍方為一，更新方法
    方法 = 方法 * 10 + 上商

    # 位退一位
    位 //= 10

# 商為整數部分，實為餘數
a = 商
b = 實
"""
Variable 'a' has wrong value. Expected: 723, Actual: 220000
Variable 'b' has wrong value. Expected: 171, Actual: 2900"""
