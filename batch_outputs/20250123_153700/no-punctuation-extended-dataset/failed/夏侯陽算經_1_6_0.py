"""
今有田二十一頃七十八畞一百八十步問為方幾何
術曰先置頃畞於上以二百四十步乗之得五十二萬二千七百二十步内零一百八十步以開方除之借一算為下法步之超一位至百止萬上置上商七百下亦置七萬於實位之下下法之上命上商除實訖倍方為一十四萬方法一退下法再退又置上商二十於前商後又置二百於方法之下下法之上名曰隅法以方隅二法皆命上商以除實訖倍隅法為四百從上方法一退下法再退又置上商三扵前商二十之後又置三步於方法之下下法之上名曰隅法以方隅二法皆命上商除實訖倍隅法得六從上方法得一千四百四十六即是上方得七百二十三步奇一百七十一步
答曰 a步 奇 b步
"""

"""
Suppose there is a field of 21 qing, 78 mu, and 180 bu.
Question: what is the side length of a square field with the same area?

The procedure says: First, place the qing and mu on top, and multiply by 240 bu to convert them into bu.
Add the remaining 180 bu to the total.
Use square root extraction to find the side length.
Borrow one digit for the divisor (lower method), and proceed step by step, placing the quotient (upper method) and refining the divisor (corner method) until the calculation is complete.

Answer: the side length is *a* bu, with a remainder of *b* bu.
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
# 初始值
實 = 總步數
上商 = 0
方法 = 0

# 第一步：至百位，商7
上商 = 7
方法 = 上商 * 上商
實 -= 方法 * 10000  # 方法超一位至百位

# 第二步：至十位，商2
方法 = 2 * 上商 * 100 + 200  # 倍方 + 隅法
上商 = 7 * 10 + 2
實 -= 方法 * 100

# 第三步：至個位，商3
方法 = 2 * 上商 * 10 + 3  # 倍方 + 隅法
上商 = 723
實 -= 方法

# 結果
a = 723  # 方步
b = 實  # 奇步
"""
Variable 'b' has wrong value. Expected: 171, Actual: -128543"""
