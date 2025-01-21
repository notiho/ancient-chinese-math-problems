"""
今有積五萬五千二百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=235)步 。
"""

"""
Suppose there is an area of 55225 bu².
Question: what is the side length of the square?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod column, shifting it one place to the left. Estimate the result. Multiply the estimate by itself to form the divisor, and divide. After dividing, double the divisor to form the new fixed divisor. Divide again. Subtract the divisor and bring down the next digit. Repeat the process as before. If the square root cannot be exact, it is considered not extractable, and the result should be expressed as a side length. If the dividend has fractions, convert them into a common fraction for the dividend. Then extract the square root of the numerator and denominator separately. If the denominator cannot be extracted, multiply the numerator by the denominator and extract again, ensuring the result is expressed as a fraction.

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

    # Step 1: Shift left (conceptually, this is handled by the number of digits)
    位數 = len(str(實))
    位數 = (位數 + 1) // 2  # Determine the number of digits in the square root

    # Step 2: Iteratively extract square root digit by digit
    for i in range(位數):
        # Bring down the next digit
        借算 = 借算 * 100 + (實 // (10 ** ((位數 - i - 1) * 2)) % 100)

        # Estimate the next digit
        for x in range(10):
            if (定法 * 10 + x) * x > 借算:
                x -= 1
                break

        # Update the root
        開方結果 = 開方結果 * 10 + x

        # Update 定法 and 副
        副 = (定法 * 10 + x) * x
        借算 -= 副
        定法 = 定法 * 10 + 2 * x

    return 開方結果

# 計算開方
a = 開方(積)  # 235 steps
"""
"""
