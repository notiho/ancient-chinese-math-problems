"""
又有積三十九億七千二百一十五萬六百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is a volume of 3,970,215,625 bu³.
Question: what is the side length of the square field?

The procedure for square root extraction says:
1. Place the volume as the dividend.
2. Borrow one counting rod for the side length, and determine its approximate value by considering the highest place value.
3. Multiply the borrowed counting rod by itself to form the divisor.
4. Divide the dividend by the divisor to get the quotient.
5. Double the divisor to form the "fixed divisor."
6. Subtract the product of the quotient and the fixed divisor from the dividend, and bring down the next digit.
7. Repeat the process by borrowing a new counting rod for the side length, and add it to the fixed divisor.
8. Continue until the square root is fully extracted.
9. If the square root cannot be fully extracted, the remainder is expressed as a fraction of the side length.
10. If the volume has fractional parts, convert them into a common denominator and include them in the calculation.

Answer: *a* bu.
"""

from fractions import Fraction

# 積三十九億七千二百一十五萬六百二十五步
積 = 3970215625

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # The side length (quotient)
    餘 = 積  # The remainder
    位 = len(str(積)) // 2  # Determine the number of digits in the square root

    for _ in range(位):
        # Step 1: Borrow one counting rod for the side length
        借 = 商 * 20  # Double the current 商 and shift left by one digit

        # Step 2: Determine the next digit of the 商
        for i in range(9, -1, -1):
            試 = 借 + i  # Add the trial digit to the borrowed value
            if 試 * i <= 餘:
                商 = 商 * 10 + i  # Update 商 with the new digit
                餘 -= 試 * i  # Update the remainder
                break

    # If there is a remainder, express it as a fraction
    if 餘 > 0:
        商 = Fraction(商) + Fraction(餘, 積)

    return 商

# Calculate the side length
a = 開方(積)

"""
Variable 'a' has wrong value. Expected: 63025, Actual: 79404312100103/794043125"""
