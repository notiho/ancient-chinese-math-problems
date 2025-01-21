"""
今有積五萬五千二百二十五步問為方幾何
開方術曰置積為實借一算步之超一等議所得以一乘所借一算為法而以除除已倍法為定法其復除折法而下復置借算步之如初以復議一乘之所得副以加定法以除以所得副從定法復除折下如前若開之不盡者為不可開當以面命之若實有分者通分內子為定實乃開之訖開其母報除若母不可開者又以母乘定實乃開之訖令如母而一
荅曰 a步 
"""

"""
Suppose there is an area of 55,225 bu. 
Question: what is the side length of the square field?

The procedure for extracting the square root says: Place the area as the dividend. Borrow one counting rod column for the side length, exceeding one place. Discuss the result obtained. Multiply the result by 1, and this becomes the divisor. Divide. Double the divisor to establish the fixed divisor. Continue dividing, adjusting the divisor, and proceed as before. If the square root cannot be fully extracted, it is considered unsolvable and should be expressed in terms of the side length. If the dividend has fractions, convert them into a common fraction and proceed as before. Extract the square root of the numerator. If the denominator cannot be extracted, multiply the denominator by the fixed dividend and proceed as before.

Answer: *a* bu.
"""

# 積五萬五千二百二十五步
積 = 55225

# Initialize variables
實 = 積
定法 = 0
借算步 = 0
所得副 = 0

# Step 1: Find the approximate square root by trial
while (借算步 + 1) ** 2 <= 積:
    借算步 += 1

# Step 2: Multiply the borrowed step by 1 to establish the initial divisor
法 = 借算步 * 1

# Step 3: Divide the area by the divisor
商 = 實 // 法

# Step 4: Double the divisor to establish the fixed divisor
定法 = 2 * 法

# Step 5: Adjust and continue dividing
while True:
    實 = 實 - 商 * 法
    if 實 == 0:
        break
    所得副 = 實 // 定法
    if 所得副 == 0:
        break
    法 = 定法 + 所得副
    商 = 實 // 法
    定法 = 2 * 法

# Final result
a = 借算步
"""
"""
