"""
又有積五十六萬四千七百五十二步四分步之一問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 564,752 and 1/4 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says:
1. Place the area as the dividend.
2. Borrow one counting rod for the side length, and determine its approximate value by finding the largest number whose square does not exceed the area.
3. Multiply this approximate value by 1, and use it as the divisor.
4. Divide the area by this divisor to get the quotient. Double the divisor to form the new divisor.
5. Subtract the product of the quotient and the divisor from the area, and bring down the next digit (if any) to continue.
6. Repeat the process by borrowing another counting rod, and continue as before.
7. If the square root cannot be exact, the result is considered "inexact" and should be expressed as a side length with a remainder.
8. If the area includes fractions, convert the entire area into a single fraction and proceed with the square root extraction.
9. If the denominator of the fraction cannot be square-rooted, multiply the numerator by the denominator and proceed with the square root extraction, adjusting the result accordingly.

Answer: *a* bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 通分內子為定實
定實 = 積

# 開方術
def 開方(實):
    # Initialize variables
    商 = 0  # Quotient (side length)
    餘 = 實  # Remainder (remaining area)
    借算 = 1  # Borrowed counting rod (place value)
    
    while 餘 > 0:
        # Find the largest number whose square does not exceed the remainder
        for i in range(9, -1, -1):
            if (商 * 20 + i) * i <= 餘:
                商 = 商 * 10 + i
                餘 -= (商 * 20 + i) * i
                break
        
        # Bring down the next digit (if any)
        餘 *= 100  # Simulate bringing down two digits (or fraction parts)
    
    return 商

# 開方
a = 開方(定實)
"""
Timed out"""
