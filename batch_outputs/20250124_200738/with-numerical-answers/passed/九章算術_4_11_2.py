"""
今有積五萬五千二百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=235)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 55,225 bu. 
Question: what is the side length of the square field?

The procedure for extracting square roots says: Place the area as the dividend. Borrow one counting rod and place it, skipping one position. 
Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Subtract the divisor and bring down the next digit. Repeat the process by placing the borrowed counting rod as before, estimating, multiplying, and adding to the fixed divisor. Divide again. Subtract and continue as before. 
If the square root cannot be fully extracted, it is considered "inextractable" and should be expressed in terms of the side length. 
If the dividend has a fractional part, convert the fraction into a common denominator and treat it as a whole number. Extract the square root, and then extract the square root of the denominator. If the denominator cannot be extracted, multiply the denominator by the result and extract again, ensuring the result is expressed as a fraction.

Answer: *a*(=235) bu.
"""

# 置積為實
積 = 55225

# 開方術
def 開方(實):
    # Initialize variables
    借算 = 0
    定法 = 0
    副 = 0
    開方結果 = 0

    # Step 1: Borrow one counting rod (determine the highest place value)
    while (借算 + 1) ** 2 <= 實:
        借算 += 1

    # Step 2: Multiply the borrowed rod by itself to form the divisor
    法 = 借算 ** 2

    # Step 3: Divide the dividend by the divisor
    開方結果 = 借算
    剩餘 = 實 - 法

    # Step 4: Double the divisor to form the fixed divisor
    while 剩餘 > 0:
        定法 = 2 * 開方結果

        # Step 5: Bring down the next digit and repeat
        while (副 + 1) * (定法 * 10 + (副 + 1)) <= 剩餘:
            副 += 1

        開方結果 = 開方結果 * 10 + 副
        剩餘 -= (定法 * 10 + 副) * 副
        副 = 0

    return 開方結果

# 計算結果
a = 開方(積)  # 235
#----- content ends here -----

"""
"""
