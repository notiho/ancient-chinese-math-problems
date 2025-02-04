"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
The problem described involves finding the square root of a given area (積) to determine the side length (方). This is a classic "開方術" (square root extraction method) from ancient Chinese mathematics. Below is the Python implementation of the procedure:


"""


"""
Suppose there is an area of 25281 bu.
Question: what is the side length of the square?

The square root extraction procedure says:
Place the area as the dividend. Borrow one counting rod column, shifting one place.
Estimate the result. Multiply the estimate by itself to form the divisor, and divide.
After dividing, double the divisor to form the fixed divisor. Divide again.
Subtract the divisor and bring down the next digit. Repeat the process.
If the square root cannot be exact, it is considered "不可開" (not exact), and the result is expressed in terms of the side length with a remainder.
If the area has a fractional part, convert it to a common fraction and proceed as above.
If the denominator cannot be simplified, multiply the numerator by the denominator and proceed as above.

Answer: *a* bu.
"""

from fractions import Fraction

# 積二萬五千二百八十一步
積 = 25281

# 開方術 implementation
def 開方術(積):
    # Initialize variables
    商 = 0  # Quotient (side length)
    餘 = 積  # Remainder
    位 = 0  # Position (to handle digit-by-digit extraction)
    
    while 餘 > 0:
        # Step 1: Borrow one column (shift one place)
        借 = 10 ** 位
        
        # Step 2: Estimate the result
        for i in range(9, -1, -1):  # Try digits from 9 to 0
            if (商 * 20 + i) * i <= 餘:
                break
        
        # Step 3: Update 商 and 餘
        商 = 商 * 10 + i
        餘 -= (商 * 20 - i) * i
        
        # Step 4: Move to the next digit
        位 += 1
    
    return 商

# Calculate the side length
a = 開方術(積)
print(f"Side length: {a} bu")


"""


This implementation follows the ancient Chinese square root extraction method step by step. The result `a` represents the side length of the square field in bu. If the square root cannot be exact, the remainder will indicate the fractional part.
"""


"""
Variable 'a' has wrong value. Expected: 159, Actual: 993"""
