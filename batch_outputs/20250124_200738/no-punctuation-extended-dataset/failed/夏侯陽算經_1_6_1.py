"""
今有田二十一頃七十八畞一百八十步問為方幾何
術曰先置頃畞於上以二百四十步乗之得五十二萬二千七百二十步内零一百八十步以開方除之借一算為下法步之超一位至百止萬上置上商七百下亦置七萬於實位之下下法之上命上商除實訖倍方為一十四萬方法一退下法再退又置上商二十於前商後又置二百於方法之下下法之上名曰隅法以方隅二法皆命上商以除實訖倍隅法為四百從上方法一退下法再退又置上商三扵前商二十之後又置三步於方法之下下法之上名曰隅法以方隅二法皆命上商除實訖倍隅法得六從上方法得一千四百四十六即是上方得七百二十三步奇一百七十一步
答曰 a步 奇 b步
"""

#----- content starts here -----
"""
Suppose there is a field of 21 qing, 78 mu, and 180 bu.
Question: what is the side length of the square field (in bu)?

The procedure says:
First, place the qing and mu on top. Multiply by 240 bu, obtaining 522,720 bu. Add the remaining 180 bu.
Perform square root extraction by division. Borrow one digit for the divisor, moving one place to the left until reaching the hundreds place.
Place the quotient (商) on top, starting with 700. Place 70,000 below the dividend (實) and subtract.
Double the current square root (方法) to form the divisor (方法). Subtract and repeat the process, moving to the next digit.
Continue until the square root is fully extracted.

Answer: the side length is *a* bu, with a remainder of *b* bu.
"""

from fractions import Fraction

# 田二十一頃七十八畞一百八十步
頃 = 21
畝 = 78
步 = 180

# 1頃 = 100畝, 1畝 = 240步
總步數 = (頃 * 100 + 畝) * 240 + 步

# 開方術
# Initialize variables
實 = 總步數  # Dividend
方法 = 0  # Current divisor (square root approximation)
上商 = 0  # Quotient (商)

# Step 1: Extract the first digit group (hundreds place)
while 實 >= (方法 + 1) ** 2:
    方法 += 1
    上商 = 方法

# Subtract the square of the current divisor
實 -= 方法 ** 2

# Step 2: Continue extracting digits
for _ in range(2):  # Repeat for two more digits
    方法 *= 2  # Double the current divisor
    next_digit = 0
    while 實 >= (方法 * 10 + next_digit) * next_digit:
        next_digit += 1
    next_digit -= 1
    方法 = 方法 * 10 + next_digit
    上商 = 上商 * 10 + next_digit
    實 -= (方法 * next_digit)

# Final result
a = 上商  # Side length in bu
b = 實  # Remainder in bu

#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 723, Actual: 72300"""
