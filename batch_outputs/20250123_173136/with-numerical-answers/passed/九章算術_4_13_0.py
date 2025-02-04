"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=268)步 。
"""

"""
Suppose there is an area of 71824 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod column, shifting one place. 
Estimate the result. Multiply the estimate by itself to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. 
Repeat the division. Subtract the divisor and bring down the next digit. Repeat the process as before. 
If the square root cannot be completed exactly, it is considered unsolvable, and the side length is expressed as an approximation. 
If the area has fractions, convert the numerator into a proper fraction and proceed. After completing the square root, also take the square root of the denominator. 
If the denominator cannot be square-rooted, multiply the numerator by the denominator and proceed as before, ensuring the denominator remains as 1.

Answer: *a*(=268) bu.
"""

# 置積為實
積 = 71824

# 開方術
def 開方(實):
    # Initialize variables
    借算 = 0
    定法 = 0
    副 = 0
    開方結果 = 0

    # Step 1: Borrow one column (shift one place)
    while 實 >= (借算 + 1) ** 2:
        借算 += 1

    # Step 2: Multiply the borrowed value by itself to form the divisor
    法 = 借算 * 借算

    # Step 3: Divide the area by the divisor
    開方結果 = 借算

    # Step 4: Double the divisor to form the fixed divisor
    定法 = 2 * 借算

    # Step 5: Check for remainder and repeat if necessary
    餘數 = 實 - 法
    while 餘數 > 0:
        副 = 0
        while 餘數 >= (定法 + 副 + 1) * (副 + 1):
            副 += 1
        開方結果 = 開方結果 * 10 + 副
        餘數 -= (定法 + 副) * 副
        定法 = 定法 * 10 + 2 * 副

    return 開方結果

# 計算開方
a = 開方(積) # 268
"""
"""
