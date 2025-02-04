"""
今有田二十一頃七十八畞一百八十步問為方幾何
術曰先置頃畞於上以二百四十步乗之得五十二萬二千七百二十步内零一百八十步以開方除之借一算為下法步之超一位至百止萬上置上商七百下亦置七萬於實位之下下法之上命上商除實訖倍方為一十四萬方法一退下法再退又置上商二十於前商後又置二百於方法之下下法之上名曰隅法以方隅二法皆命上商以除實訖倍隅法為四百從上方法一退下法再退又置上商三扵前商二十之後又置三步於方法之下下法之上名曰隅法以方隅二法皆命上商除實訖倍隅法得六從上方法得一千四百四十六即是上方得七百二十三步奇一百七十一步
答曰 a步 奇 b步
"""

"""
Suppose there is a field of 21 qing, 78 mu, and 180 bu.
Question: what is the side length of the square field?

The procedure says:
First, place the qing and mu above. Multiply by 240 bu to convert to bu, obtaining 522,720 bu. Add the remaining 180 bu.
Perform square root extraction by division. Borrow one digit for the divisor. The divisor starts at the hundred's place and proceeds to the ten-thousand's place.
Place the first quotient (7) above, and place 70,000 below in the result's position.
Subtract and continue the process, doubling the divisor and appending the next quotient to form the new divisor.
Repeat the process until the square root is fully extracted.

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

# 內零一百八十步
總步數 += 步

# 開方計算
# 初始值
實 = 總步數
方法 = 0
上商 = 0
下法 = 0

# 第一步：至百止，萬上置上商7
上商 = 7
方法 = 上商 * 2 * 10**5  # 方法 = 2 * 商 * 位值
下法 = 上商 * 10**5       # 下法 = 商 * 位值
實 -= 上商 * 下法         # 實 = 實 - 商 * 下法

# 第二步：再退，置上商2
上商 = 72
方法 += 上商 * 2 * 10**3  # 方法 = 方法 + 2 * 商 * 位值
下法 += 上商 * 10**3       # 下法 = 下法 + 商 * 位值
實 -= 上商 * 下法         # 實 = 實 - 商 * 下法

# 第三步：再退，置上商3
上商 = 723
方法 += 上商 * 2 * 10     # 方法 = 方法 + 2 * 商 * 位值
下法 += 上商 * 10         # 下法 = 下法 + 商 * 位值
實 -= 上商 * 下法         # 實 = 實 - 商 * 下法

# 最終結果
a = 723  # 方步數
b = 實   # 餘步數
"""
Variable 'b' has wrong value. Expected: 171, Actual: -623344390"""
