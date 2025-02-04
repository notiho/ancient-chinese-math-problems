"""
今有積五萬五千二百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an area of 55,225 bu. 
Question: what is the side length of the square field?

The procedure for extracting the square root says:
Place the area as the dividend. Borrow one counting rod for the side length, exceeding one place value. 
Estimate the result. Multiply the estimate by 1, and use it as the divisor. Divide the dividend by this divisor. 
Double the divisor to form the fixed divisor. 
Continue dividing, adjusting the divisor as necessary. Place the borrowed counting rod for the side length as before. 
Estimate again, multiply the estimate by 1, and add it to the fixed divisor. Divide again. 
Repeat this process until the square root is fully extracted. 
If the square root cannot be fully extracted, it is considered "inextractable" and the result is expressed in terms of the area. 
If the dividend has a fraction, convert it to a common fraction and proceed with the extraction. 
If the denominator cannot be extracted, multiply the denominator by the dividend and proceed with the extraction.

Answer: *a* bu.
"""

# 積五萬五千二百二十五步
積 = 55225

# 開方術
# Initialize variables
實 = 積
定法 = 0
a = 0  # The side length (result)

# Step-by-step extraction
while True:
    # Borrow one counting rod for the side length
    借算 = 1

    # Estimate the result
    議 = 1

    # Multiply the estimate by 1 to form the divisor
    法 = 議 * 借算

    # Divide the dividend by the divisor
    商 = 實 // 法

    # Double the divisor to form the fixed divisor
    定法 = 2 * 法

    # Check if the square root is fully extracted
    if 商 * 商 == 積:
        a = 商
        break
    else:
        # Adjust the divisor and continue
        實 = 積 - 商 * 商
        if 實 == 0:
            a = 商
            break#----- content ends here -----

"""
Code error: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit"""
