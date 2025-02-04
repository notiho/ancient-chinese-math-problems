"""
今有積五萬五千二百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 55,225 bu².
Question: what is the side length of the square field?

The procedure for square root extraction says:
1. Place the area as the dividend.
2. Borrow a counting rod for the side length, exceeding one place. Discuss what is obtained.
3. Multiply the borrowed counting rod by itself, making the divisor. Divide the dividend by the divisor.
4. Double the divisor to make the fixed divisor.
5. Subtract the result of the division from the dividend.
6. Place the borrowed counting rod again, as before. Discuss what is obtained.
7. Multiply the obtained number by itself, adding it to the fixed divisor. Divide the remaining dividend by the updated divisor.
8. Repeat the process until the square root is fully extracted. If it cannot be fully extracted, it is considered "inexpressible."
9. If the dividend has a fractional part, convert it to a common fraction and extract the square root of the numerator and denominator separately.

Answer: *a* bu.
"""

# 積五萬五千二百二十五步
積 = 55225

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # The result (side length)
    餘 = 積  # The remaining dividend
    定法 = 0  # The fixed divisor

    while 餘 > 0:
        # Step 2: Borrow a counting rod for the next digit
        借算 = 1
        while (借算 + 1) ** 2 <= 餘:
            借算 += 1

        # Step 3: Multiply the borrowed counting rod by itself to make the divisor
        法 = 借算 ** 2

        # Step 4: Divide the remaining dividend by the divisor
        商 = 商 * 10 + 借算
        餘 -= 法

        # Step 5: Double the divisor to make the fixed divisor
        定法 = 商 * 2 * 10

        # Step 6: Repeat the process for the next digit
        if 餘 == 0:
            break

    return 商

# Calculate the side length
a = 開方(積)  # a is the side length in bu#----- content ends here -----

"""
"""
