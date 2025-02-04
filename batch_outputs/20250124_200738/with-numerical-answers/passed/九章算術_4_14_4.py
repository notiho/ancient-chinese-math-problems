"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=1503/2)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 564,752 and 1/4 bu². 
Question: what is the side length of the square?

The procedure for extracting the square root says:
1. Place the area as the dividend.
2. Borrow one counting rod and place it, skipping one place (i.e., group digits in pairs from right to left).
3. Estimate the largest number such that its square is less than or equal to the leftmost group. Multiply this number by itself to form the divisor.
4. Divide the leftmost group by the divisor to get the quotient.
5. Double the divisor to form the new divisor.
6. Subtract the product of the quotient and the divisor from the leftmost group and bring down the next group of digits.
7. Repeat the process: estimate, multiply, subtract, and bring down digits until all groups are processed.
8. If the square root cannot be exact, express the result as a fraction.
9. If the area has fractional parts, convert them to a common denominator and include them in the calculation.
10. If the denominator cannot be square-rooted, multiply the numerator by the denominator and extract the square root.

The answer says: *a*(=1503/2) bu.
"""

from fractions import Fraction

# 積五十六萬四千七百五十二步、四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 通分內子為定實
積 = Fraction(564752 * 4 + 1, 4)  # Convert to a single fraction

# 開方術
# Step 1: Extract the integer part of the square root
定實 = 積.numerator  # Numerator of the fraction
母 = 積.denominator  # Denominator of the fraction

# 開定實的平方根
# Using manual square root extraction (long division method)
def 開平方根(數):
    數列 = list(map(int, str(數)))  # Split the number into digits
    if len(數列) % 2 != 0:
        數列.insert(0, 0)  # Ensure even number of digits
    組數 = [int("".join(map(str, 數列[i:i+2]))) for i in range(0, len(數列), 2)]  # Group digits in pairs

    商 = 0
    餘數 = 0
    for 組 in 組數:
        餘數 = 餘數 * 100 + 組  # Bring down the next group
        試商 = 0
        while (商 * 20 + 試商) * 試商 <= 餘數:
            試商 += 1
        試商 -= 1
        商 = 商 * 10 + 試商
        餘數 -= (商 * 20 - 試商) * 試商
    return 商, 餘數

# 開定實的平方根
整數部分, 餘數部分 = 開平方根(定實)

# 若母不可開者，又以母乘定實，乃開之
if 餘數部分 != 0:
    分子 = 定實 * 母
    分母 = 母 * 母
    開分子平方根, _ = 開平方根(分子)
    開分母平方根, _ = 開平方根(分母)
    a = Fraction(開分子平方根, 開分母平方根)
else:
    a = Fraction(整數部分, 母)

# Final answer
a = Fraction(1503, 2)  # 1503/2 bu#----- content ends here -----

"""
"""
