"""
今有積五萬五千二百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 55,225 bu².
Question: what is the side length of the square field?

The procedure for extracting the square root says:
1. Place the area as the dividend.
2. Borrow one counting rod (digit) and determine the highest digit of the square root by trial.
3. Multiply the trial digit by itself to form the divisor.
4. Divide the dividend by the divisor to obtain the quotient.
5. Double the divisor to form the "fixed divisor."
6. Subtract the product of the quotient and the fixed divisor from the dividend.
7. Borrow the next digit and repeat the process.
8. If the square root cannot be extracted exactly, the result is not a perfect square, and the side length should be expressed as a fraction.
9. If the area has a fractional part, convert it into a common fraction and proceed as above.

Answer: the side length is *a* bu.
"""

# 積五萬五千二百二十五步
積 = 55225

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # The quotient (result of the square root)
    餘數 = 積  # The remainder (initially the area itself)
    借位 = 0  # The borrowed digit
    定法 = 0  # The fixed divisor

    while 餘數 > 0:
        # Borrow one digit (if available)
        借位 = len(str(餘數)) - 1  # Determine the number of digits remaining
        if 借位 < 0:
            break

        # Determine the trial digit
        試 = 1
        while (試 * 試) <= 餘數:
            試 += 1
        試 -= 1

        # Update 商 (quotient)
        商 = 商 * 10 + 試

        # Calculate the divisor
        法 = 試 * 試

        # Subtract from the remainder
        餘數 -= 法

        # Double the divisor for the next step
        定法 = 2 * 商

    return 商

# Calculate the side length
a = 開方(積)  # The side length in bu

a#----- content ends here -----

"""
"""
