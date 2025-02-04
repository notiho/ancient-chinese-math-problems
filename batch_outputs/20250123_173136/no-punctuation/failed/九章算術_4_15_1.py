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
2. Borrow one counting rod column (shift one place to the left) to determine the number of digits in the square root.
3. Estimate the first digit of the square root. Multiply it by itself to form the divisor.
4. Divide the dividend by the divisor to get the first digit of the square root.
5. Double the divisor to form the "fixed divisor."
6. Subtract the product of the divisor and the quotient from the dividend, and bring down the next digit.
7. Repeat the process: use the current square root digits to form a new divisor, estimate the next digit, and continue dividing.
8. If the square root cannot be exact, express the result as a fraction or as an approximate value.

Answer: *a* bu.
"""

# 置積為實
實 = 3970215625

# 開方術
def 開方(實):
    # Initialize variables
    商 = 0  # The square root result
    餘數 = 0  # The remainder
    借算 = 0  # Borrowed column for estimation
    定法 = 0  # Fixed divisor

    # Step 1: Determine the number of digits in the square root
    位數 = len(str(實))
    位數 = (位數 + 1) // 2  # Half the number of digits, rounded up

    # Step 2: Iteratively calculate each digit of the square root
    for i in range(位數):
        # Bring down the next two digits
        餘數 = 餘數 * 100 + (實 // (10 ** (2 * (位數 - i - 1))) % 100)

        # Estimate the next digit
        for x in range(10):
            if (定法 * 10 + x) * x > 餘數:
                商位 = x - 1
                break
        else:
            商位 = 9

        # Update 商 and 定法
        商 = 商 * 10 + 商位
        減數 = (定法 * 10 + 商位) * 商位
        餘數 -= 減數
        定法 = 定法 * 10 + 2 * 商位

    return 商

# 計算方步數
a = 開方(實)
"""
Variable 'a' has wrong value. Expected: 63025, Actual: 63009"""
