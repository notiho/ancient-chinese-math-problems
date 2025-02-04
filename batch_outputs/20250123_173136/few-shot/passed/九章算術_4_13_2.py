"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
To solve this problem, we need to implement the ancient Chinese square root extraction method ("開方術"). This method involves iterative approximation to find the square root of a given number. Below is the Python implementation of the procedure:


"""


"""
Suppose there is an area of 71824 bu². 
Question: what is the side length of the square field?

The square root extraction procedure says:
Place the given area as the dividend. Borrow one counting rod column, skipping one place.
Estimate the largest number that can fit. Multiply this number by itself, and subtract it from the dividend. 
Double the number found so far to form the divisor. Divide the remaining dividend by this divisor.
Repeat the process by appending the next digit of the dividend, and continue until the square root is fully extracted.
If the square root cannot be fully extracted, the result is expressed as a fraction.
If the area has a fractional part, convert it to a common denominator and extract the square root of the numerator and denominator separately.

Answer: *a* bu.
"""

from fractions import Fraction

# 積七萬一千八百二十四步
積 = 71824

# 開方術
def 開方(積):
    # Initialize variables
    實 = 積  # Dividend
    定法 = 0  # Final result (square root)
    副 = 0  # Temporary divisor

    # Step-by-step extraction
    while 實 > 0:
        # Borrow one column (skip one place)
        借 = 1
        while (借 + 1) ** 2 <= 實:
            借 += 1

        # Update 定法 and 副
        定法 = 定法 * 10 + 借
        副 = 副 * 2 + 借

        # Subtract the square of the borrowed number
        實 -= 借 ** 2

        # If there is no remainder, break
        if 實 == 0:
            break

        # Double the divisor for the next iteration
        副 *= 2

    # If there is a remainder, express as a fraction
    if 實 > 0:
        分子 = 實
        分母 = 副
        分數 = Fraction(分子, 分母)
        return 定法 + 分數
    else:
        return 定法

# Calculate the square root
a = 開方(積)
print(f"Answer: {a} bu")


"""


### Explanation of the Code:
1. **Initialization**: The dividend (`實`) is set to the given area, and the square root (`定法`) starts at 0.
2. **Borrowing and Estimation**: The largest number (`借`) whose square is less than or equal to the current dividend is found.
3. **Update Results**: The square root (`定法`) and the divisor (`副`) are updated iteratively.
4. **Subtraction**: The square of the borrowed number is subtracted from the dividend.
5. **Fraction Handling**: If there is a remainder, it is expressed as a fraction.
6. **Output**: The final square root is returned, either as an integer or a fraction.

### Example:
For `積 = 71824`, the square root is `a = 268 bu`.
"""


"""
"""
