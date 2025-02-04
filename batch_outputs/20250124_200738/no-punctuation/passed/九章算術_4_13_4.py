"""
又有積七萬一千八百二十四步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 71824 bu².
Question: what is the side length of the square field?

The procedure for square root extraction says:
1. Place the area as the dividend (實).
2. Borrow one counting rod (算) to determine the approximate side length (步) by finding the largest number whose square does not exceed the area.
3. Multiply the borrowed number by itself to form the divisor (法), and divide the area by this divisor.
4. Double the divisor to form the new fixed divisor (定法).
5. Subtract the square of the borrowed number from the area, leaving the remainder.
6. Borrow another counting rod to refine the side length, and repeat the process:
   - Multiply the borrowed number by the fixed divisor, add it to the previous divisor, and divide the remainder.
   - Continue until the remainder is zero or cannot be further divided.
7. If the square root cannot be fully extracted, express the result as a fraction or mixed number.
8. If the area has a fractional part, convert it to a common fraction and proceed as above.

The answer says: *a* bu.
"""

from fractions import Fraction

# 置積為實
積 = 71824

# 開方術
def 開方(積):
    # Initialize variables
    定法 = 0  # Fixed divisor
    商 = 0    # Quotient (side length)
    餘 = 積   # Remainder

    while True:
        # Borrow one counting rod and determine the largest number whose square does not exceed the remainder
        借算 = 0
        while (定法 + 借算) * 借算 <= 餘:
            借算 += 1
        借算 -= 1

        # If no valid 借算 can be found, stop
        if 借算 == 0:
            break

        # Update 商 (side length)
        商 = 商 * 10 + 借算

        # Update 定法 (fixed divisor)
        定法 = 定法 * 10 + 2 * 商

        # Update 餘 (remainder)
        餘 -= (定法 - 借算) * 借算

        # If 餘 is zero, the square root is exact
        if 餘 == 0:
            break

    # If 餘 is not zero, express the result as a fraction
    if 餘 != 0:
        商 = Fraction(積, 商)

    return 商

# Calculate the side length
a = 開方(積)
#----- content ends here -----

"""
"""
