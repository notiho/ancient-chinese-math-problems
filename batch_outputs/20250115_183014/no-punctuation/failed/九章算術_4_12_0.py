"""
又有積二萬五千二百八十一步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 25,280 square bu.
Question: what is the side length of the square field?

The procedure for extracting the square root says:
Place the area as the dividend. Borrow one counting rod for the side length, exceeding one place value.
Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide.
Double the divisor to form the fixed divisor. Continue dividing, adjusting the divisor as necessary.
If the division cannot be completed exactly, the square root cannot be extracted, and the side length is expressed as a fraction.
If the area has a fractional part, convert it to a common fraction and proceed with the extraction.
Once the extraction is complete, report the result.

Answer: *a* bu.
"""

# 積二萬五千二百八十一步
積 = 25280

# 開方術
def 開方(積):
    # Initialize variables
    定法 = 0  # Fixed divisor
    復 = 0    # Adjustment
    借算步 = 0  # Borrowed counting rod (initial guess)
    
    while True:
        # Increment the borrowed counting rod
        借算步 += 1
        
        # Calculate the divisor (法)
        法 = 借算步 * 借算步
        
        # If the divisor exceeds the area, stop
        if 法 > 積:
            借算步 -= 1
            break
        
        # Update the fixed divisor
        定法 = 2 * 借算步
    
    # Calculate the remaining area
    剩餘 = 積 - 借算步 * 借算步
    
    # If there is no remainder, return the result
    if 剩餘 == 0:
        return 借算步
    
    # Otherwise, express the result as a fraction
    return Fraction(積, 借算步 * 2)

# Calculate the side length
a = 開方(積)
"""
Variable 'a' has wrong value. Expected: 159, Actual: 80"""
