"""
又有積七萬一千八百二十四步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 71824 bu².
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod for the side length, exceeding one rank. Discuss the result obtained. Multiply it by 1, and the borrowed counting rod becomes the divisor. Divide by it. Double the divisor to become the fixed divisor. Continue dividing, adjusting the divisor, and proceed as before. If the square root cannot be fully extracted, it is considered unsolvable, and the side length is expressed as a fraction. If the area has a fractional part, convert it to a common fraction and proceed as before. After completing the square root extraction, divide the numerator by the denominator. If the denominator cannot be extracted, multiply it by the fixed divisor and proceed as before.

Answer: *a* bu.
"""

# 積七萬一千八百二十四步
積 = 71824

# 開方術
def 開方(積):
    # Initialize variables
    實 = 積  # Dividend
    定法 = 0  # Fixed divisor
    借算步 = 0  # Borrowed counting rod (side length)
    
    while 實 > 0:
        # Borrow one counting rod for the side length
        借算步 = 借算步 * 10
        
        # Find the largest digit that works
        for i in range(9, -1, -1):
            試 = 借算步 + i
            法 = 試 * 試
            if 法 <= 實:
                借算步 = 試
                break
        
        # Subtract the square of the current side length
        實 -= 借算步 * 借算步
        
        # Double the divisor to become the fixed divisor
        定法 = 2 * 借算步
    
    return 借算步

# Calculate the side length
a = 開方(積)
"""
Variable 'a' has wrong value. Expected: 268, Actual: 990"""
