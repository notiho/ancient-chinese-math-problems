"""
又有積三十九億七千二百一十五萬六百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a volume of 3,970,215,625 bu³.
Question: what is the side length of the square field (in bu)?

The procedure for square root extraction says: Place the volume as the dividend. Borrow one counting rod for the side length, exceeding one digit. Discuss the result obtained. Multiply the borrowed counting rod by itself to form the divisor, and divide. Double the divisor to form the fixed divisor. Subtract and continue dividing using the reduced divisor. Place the borrowed counting rod again as before. Discuss the result obtained. Multiply it by itself, add it to the fixed divisor, and divide. Continue this process. If the square root cannot be fully extracted, it is not a perfect square, and the result should be expressed in terms of the side length. If the dividend has fractions, convert them to a common denominator and extract the square root of the numerator. If the denominator cannot be extracted, multiply the denominator by the numerator and extract the square root. The result should be expressed as a fraction.

Answer: *a* bu.
"""

# 積三十九億七千二百一十五萬六百二十五步
積 = 3970215625

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # The result (side length)
    餘 = 積  # The remaining part of the volume
    借算步 = 1  # The borrowed counting rod (initially 1)
    
    while 餘 > 0:
        # 議所得: Find the largest 借算步 such that (商 * 2 + 借算步) * 借算步 <= 餘
        while (商 * 2 + 借算步) * 借算步 > 餘:
            借算步 -= 1
        
        # Update 商 (side length)
        商 = 商 * 10 + 借算步
        
        # Update 餘 (remaining volume)
        餘 -= (商 * 2 - 借算步) * 借算步
        
        # Move to the next digit
        餘 *= 100  # Shift two decimal places
        借算步 = 1  # Reset 借算步 for the next iteration
    
    return 商

# Calculate the side length
a = 開方(積)
a#----- content ends here -----

"""
Timed out"""
