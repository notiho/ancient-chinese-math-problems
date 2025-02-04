"""
又有積七萬一千八百二十四步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 71824 bu². 
Question: what is the side length of the square field?

The procedure for extracting the square root says:
Place the area as the dividend. Borrow one counting rod for the side length, exceeding one place value. 
Estimate the result. Multiply the estimate by 1, and use it as the divisor. Divide the dividend by this divisor. 
Double the divisor to obtain the fixed divisor. Continue dividing. Subtract the divisor and place the remainder below. 
Borrow another counting rod for the side length as before. Repeat the estimation and multiplication. Add the result to the fixed divisor. 
Divide again. Repeat the process as before. If the square root cannot be extracted exactly, it is considered unsolvable, and the side length should be expressed as a fraction. 
If the dividend has a fractional part, convert it to a common fraction and proceed with the extraction. 
After completing the extraction, divide the numerator by the denominator. If the denominator cannot be extracted, multiply the numerator by the denominator and proceed with the extraction. 
Finally, express the result as a fraction.

Answer: *a* bu.
"""

# 置積為實
實 = 71824

# Initialize variables
商 = 0  # The quotient (side length)
餘 = 實  # The remainder
位 = 0  # The current place value

# 開方術
while 餘 > 0:
    # 借一算步之超一等
    位 += 1
    借算 = 10 ** (位 - 1)

    # 議所得
    所得 = 0
    while (所得 + 1) * (所得 + 1) * 借算 * 借算 <= 餘:
        所得 += 1

    # 以一乘所借一算為法
    法 = 所得 * 借算

    # 而以除
    商 += 所得 * 借算
    餘 -= 法 * 所得

    # 已倍法為定法
    定法 = 2 * 商

    # 若餘為零，停止
    if 餘 == 0:
        break

# 若開之不盡者，為不可開
if 餘 > 0:
    # 當以面命之 (express as a fraction)
    a = Fraction(實, 商)
else:
    # 完全開方
    a = 商

a
"""
"""
