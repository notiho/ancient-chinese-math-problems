"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=159)步 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 25281 bu. 
Question: what is the side length of the square field?

The procedure for extracting square roots says: Place the volume as the dividend. Borrow one counting rod to represent the side length, skipping one place (i.e., group digits in pairs from right to left). 
Estimate the first digit of the root. Multiply this digit by itself to form the divisor, and divide. After division, double the divisor to form the "fixed divisor." 
Continue dividing, subtracting, and iterating as follows: 
1. Subtract the square of the estimated digit from the current dividend.
2. Bring down the next pair of digits.
3. Use the fixed divisor, add the next estimated digit, and divide again.
4. Repeat until all digits are processed.

If the square root cannot be exact, express the result as a fraction. If the dividend has a fractional part, convert it into a common fraction and proceed as above.

The answer says: *a*(=159) bu.
"""

# 置積為實
積 = 25281

# 開方術
def 開方(積):
    # Initialize variables
    實 = str(積)  # Convert the number to a string for digit grouping
    實 = "0" * (len(實) % 2) + 實  # Ensure even number of digits
    借算 = []  # List to store the digits of the root
    定法 = 0  # Fixed divisor
    餘數 = 0  # Remainder

    # Process each pair of digits
    for i in range(0, len(實), 2):
        # Bring down the next pair of digits
        餘數 = 餘數 * 100 + int(實[i:i + 2])

        # Estimate the next digit of the root
        for x in range(9, -1, -1):
            if (定法 * 10 + x) * x <= 餘數:
                借算.append(x)
                break

        # Update the remainder
        餘數 -= (定法 * 10 + 借算[-1]) * 借算[-1]

        # Update the fixed divisor
        定法 = 定法 * 10 + 2 * 借算[-1]

    # Combine the digits of the root
    return int("".join(map(str, 借算)))

# 計算結果
a = 開方(積)  # 159#----- content ends here -----

"""
"""
