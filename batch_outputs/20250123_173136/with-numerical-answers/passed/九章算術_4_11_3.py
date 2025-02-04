"""
今有積五萬五千二百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=235)步 。
"""

"""
Suppose there is an area of 55225 bu².
Question: what is the side length of the square?

The procedure for square root extraction says:
Place the area as the dividend. Borrow one counting rod column, shifting one place.
Estimate the result. Multiply the estimate by itself to form the divisor, and divide.
After dividing, double the divisor to form the "fixed divisor." Divide again.
Subtract the divisor and bring down the next digit. Repeat the process.
If the square root cannot be exact, express the result as a fraction.
If the dividend has a fractional part, adjust the numerator and denominator accordingly.
If the denominator cannot be square-rooted, multiply the numerator by the denominator and extract the square root.

Answer: *a*(=235) bu.
"""

# 置積為實
積 = 55225

# 開方術
def 開方(積):
    # Initialize variables
    商 = 0  # Quotient (result of square root)
    餘 = 0  # Remainder
    位數 = len(str(積))  # Number of digits in the dividend
    借算 = 0  # Borrowed column

    # Step 1: Borrow one column, shifting one place
    if 位數 % 2 == 1:
        借算 = int(str(積)[0])
        積 = int(str(積)[1:])
    else:
        借算 = int(str(積)[:2])
        積 = int(str(積)[2:])

    # Step 2: Estimate the square root of the first borrowed column
    for i in range(1, 10):
        if i * i > 借算:
            商 = i - 1
            break
    餘 = 借算 - 商 * 商

    # Step 3: Process remaining digits
    while 積 > 0 or 餘 > 0:
        # Bring down the next two digits
        if 積 > 0:
            餘 = 餘 * 100 + int(str(積)[:2])
            積 = int(str(積)[2:]) if len(str(積)) > 2 else 0

        # Double the current quotient to form the "fixed divisor"
        定法 = 商 * 2

        # Find the next digit of the quotient
        for i in range(10):
            if (定法 * 10 + i) * i > 餘:
                商 = 商 * 10 + (i - 1)
                餘 -= (定法 * 10 + (i - 1)) * (i - 1)
                break

    return 商

# Calculate the square root
a = 開方(積)  # 235

"""
"""
