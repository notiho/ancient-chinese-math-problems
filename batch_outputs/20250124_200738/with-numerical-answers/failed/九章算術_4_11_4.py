"""
今有積五萬五千二百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=235)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 55225 bu². 
Question: what is the side length of the square field?

The procedure for square root extraction says: Place the area as the dividend. Borrow one counting rod column, shifting one place. 
Estimate the result. Multiply the estimate by itself to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Subtract the divisor from the dividend. Lower the next digit. Repeat the process by placing the borrowed column as before, and multiply the estimate by itself to form the auxiliary. Add the auxiliary to the fixed divisor, and divide. Subtract the auxiliary from the fixed divisor. Repeat the process as before. If the square root cannot be exact, it is considered not extractable, and the side length should be expressed as a fraction. If the dividend has a fractional part, convert it into a common fraction and proceed. If the denominator cannot be extracted, multiply the denominator by the fixed divisor and proceed.

Answer: *a*(=235) bu.
"""

# 置積為實
積 = 55225

# 開方術
# Step-by-step manual square root extraction process

# Initialize variables
商 = 0  # Quotient (side length being calculated)
餘數 = 積  # Remainder (starts as the area)

# Start the square root extraction process
while True:
    # 超一等 (Shift one place to the left for the current digit)
    借位 = len(str(餘數)) - 1  # Determine the highest place value
    if 借位 % 2 == 0:
        借位 -= 1  # Ensure we are working with pairs of digits

    # 議所得 (Estimate the next digit of the square root)
    候選商 = 0
    while (商 * 20 + 候選商) * 候選商 <= 餘數:
        候選商 += 1
    候選商 -= 1  # Step back to the correct digit

    # Update 商 (Quotient)
    商 = 商 * 10 + 候選商

    # Update 餘數 (Remainder)
    減數 = (商 * 20 - 候選商) * 候選商
    餘數 -= 減數

    # Check if the remainder is zero (exact square root)
    if 餘數 == 0:
        break

# Final result
a = 商  # 235#----- content ends here -----

"""
Code error: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit"""
