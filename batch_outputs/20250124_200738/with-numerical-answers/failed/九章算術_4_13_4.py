"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=268)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 71824 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod column, shifting one place. 
Estimate the result. Multiply the estimate by itself to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Subtract the divisor and bring down the next digit. Repeat the process by placing the borrowed column as before, and estimate again. Multiply the estimate by itself to form the auxiliary, add it to the fixed divisor, and divide. Subtract the auxiliary from the fixed divisor. Repeat the process as before. If the square root cannot be fully extracted, it is considered unsolvable, and the side length is expressed as a fraction. If the area has a fractional part, convert it to a common fraction and proceed. After completing the square root extraction, extract the square root of the denominator. If the denominator cannot be extracted, multiply the denominator by the fixed value and extract again, ensuring the result is expressed as a fraction.

Answer: *a*(=268) bu.
"""

# 置積為實
積 = 71824

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0
    餘 = 積
    定法 = 0

    while 餘 > 0:
        # 超一等 (shift one place)
        借位 = len(str(餘)) - 1 if len(str(餘)) % 2 == 0 else len(str(餘)) - 2
        借算 = 10 ** 借位

        # 議所得 (estimate the next digit)
        預測 = 0
        while (定法 + 預測 * 借算) * 預測 <= 餘:
            預測 += 1
        預測 -= 1

        # Update 商 (quotient)
        商 = 商 * 10 + 預測

        # Update 餘 (remainder)
        減去 = (定法 + 預測 * 借算) * 預測
        餘 -= 減去

        # Update 定法 (fixed divisor)
        定法 = 定法 + 2 * 預測 * 借算

        # Bring down the next digit
        餘 *= 100

    return 商

# Calculate the square root
a = 開方(積) # 268#----- content ends here -----

"""
Code error: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit"""
