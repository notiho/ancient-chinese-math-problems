"""
今有田二十一頃七十八畞一百八十步問為方幾何
術曰先置頃畞於上以二百四十步乗之得五十二萬二千七百二十步内零一百八十步以開方除之借一算為下法步之超一位至百止萬上置上商七百下亦置七萬於實位之下下法之上命上商除實訖倍方為一十四萬方法一退下法再退又置上商二十於前商後又置二百於方法之下下法之上名曰隅法以方隅二法皆命上商以除實訖倍隅法為四百從上方法一退下法再退又置上商三扵前商二十之後又置三步於方法之下下法之上名曰隅法以方隅二法皆命上商除實訖倍隅法得六從上方法得一千四百四十六即是上方得七百二十三步奇一百七十一步
答曰 a步 奇 b步
"""

#----- content starts here -----
"""
Suppose there is a field of 21 qing, 78 mu, and 180 bu.
Question: what is the side length of the square field?

The procedure says:
First, place the qing and mu above. Multiply by 240 bu to convert to bu, obtaining 522,720 bu. Add the remaining 180 bu.
Perform square root extraction by division. Borrow one digit for the divisor, shifting one place to the left until reaching the hundreds place.
Place the quotient (商) above and the divisor (法) below. Multiply the divisor by the quotient and subtract from the dividend.
Double the current divisor to form the new divisor (方法). Repeat the process for each digit, adjusting the divisor and quotient as necessary.
Continue until the square root is fully extracted.

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

# 加上剩餘的一百八十步
總步數 += 步

# 開方計算
# 初始值
實 = 總步數
商 = 0
方法 = 0

# 第一位
上商 = 7
方法 = 2 * 上商 * 10**5
實 -= (上商 * 10**2)**2
商 += 上商 * 10**2

# 第二位
上商 = 2
方法 = (方法 + 上商 * 10**3) * 2
實 -= (商 + 上商 * 10)**2 - 商**2
商 += 上商 * 10

# 第三位
上商 = 3
方法 = (方法 + 上商 * 10**2) * 2
實 -= (商 + 上商)**2 - 商**2
商 += 上商

# 結果
a = 商
b = 實#----- content ends here -----

"""
"""
