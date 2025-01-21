"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=268)步 。
"""

"""
Suppose there is an area of 71824 bu².
Question: what is the side length of the square field?

The procedure for extracting square roots says:
1. Place the area as the dividend.
2. Borrow one counting rod position, skipping one place.
3. Estimate the result. Multiply the estimate by itself to form the divisor, and divide.
4. After dividing, double the divisor to form the "fixed divisor."
5. Repeat the division process. Subtract the remainder and continue as before.
6. If the square root cannot be fully extracted, the result is not exact, and the side length should be expressed as a fraction.
7. If the area has a fractional part, convert it to a common fraction and proceed with the extraction.
8. If the denominator cannot be extracted, multiply the numerator by the denominator and extract the square root, ensuring the denominator remains the same.

Answer: *a*(=268) bu.
"""

# 置積為實
積 = 71824

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # Quotient (result of square root)
    餘 = 積  # Remainder
    位 = 1  # Position multiplier (starts at 1)
    
    # Step 1: Determine the highest place value of the square root
    while 位 * 位 <= 積:
        位 *= 10
    位 //= 10  # Reduce to the correct starting position

    # Step 2: Iteratively extract the square root
    while 位 > 0:
        # Trial divisor: 商 * 2 * 位
        試除數 = 商 * 2 * 位
        for x in range(9, -1, -1):  # Test digits from 9 to 0
            if (試除數 + x * 位) * x <= 餘:
                商 = 商 * 10 + x  # Update quotient
                餘 -= (試除數 + x * 位) * x  # Update remainder
                break
        位 //= 10  # Move to the next lower position

    return 商

# 計算方步
a = 開方(積)  # 268 steps
"""
Variable 'a' has wrong value. Expected: 268, Actual: 999"""
