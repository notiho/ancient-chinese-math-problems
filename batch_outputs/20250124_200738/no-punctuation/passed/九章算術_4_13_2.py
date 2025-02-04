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
1. Place the area as the dividend.
2. Borrow one counting rod to estimate the square root, starting with the highest place value.
3. Multiply the estimated value by itself to form the divisor.
4. Divide the dividend by the divisor to obtain the quotient.
5. Double the divisor to form the "fixed divisor."
6. Subtract the product of the quotient and the fixed divisor from the dividend.
7. Repeat the process for the next place value, treating the remainder as the new dividend.
8. If the square root cannot be extracted exactly, the result is expressed as a fractional side length.
9. If the area has fractions, adjust the area to a common denominator and proceed with the extraction.

Answer: the side length is *a* bu.
"""

from fractions import Fraction

# 積七萬一千八百二十四步
積 = 71824

# Initialize variables
實 = 積  # Dividend
商 = 0  # Quotient (the side length being calculated)
位 = 1  # Place value for the current digit of the square root

# 開方術
while 實 > 0:
    # Step 1: Estimate the next digit of the square root
    while (商 + 位) ** 2 <= 積:
        商 += 位
    位 //= 10  # Move to the next place value

    # Step 2: Subtract the square of the current estimate from the dividend
    實 -= 商 ** 2

    # Step 3: Double the current estimate to form the fixed divisor
    定法 = 2 * 商

    # Step 4: Repeat for the next place value
    位 *= 10

# Final result
a = Fraction(商)  # The side length of the square field#----- content ends here -----

"""
"""
