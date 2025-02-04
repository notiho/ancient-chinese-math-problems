"""
今有積一百八十六萬八百六十七尺問為立方幾何
開立方術曰置積為實借一算步之超二等議所得以再乘所借一算為法而除之除已三之為定法復除折而下以三乘所得數置中行復借一算置下行步之中超一下超二等復置議以一乘中再乘下皆副以加定法以定法除除已倍下并中從定法復除折下如前開之不盡者亦為不可開若積有分者通分內子為定實定實乃開之訖開其母以報除若母不可開者又以母再乘定實乃開之訖令如母而一
荅曰 a尺 
"""

"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is its cube root?

The procedure for extracting cube roots says:
1. Place the volume as the dividend.
2. Borrow one counting rod, and step through the digits, skipping two places at a time, to determine the initial estimate.
3. Multiply the estimate by itself, then multiply again by the borrowed counting rod, to form the divisor.
4. Divide the dividend by the divisor to obtain the first digit of the cube root.
5. Multiply the result by 3 to form the "fixed divisor."
6. Subtract the product from the dividend, and bring down the next group of digits.
7. Multiply the current result by 3, and place it in the middle row.
8. Borrow another counting rod, and repeat the process for the next digit, stepping through the digits as before.
9. Multiply the middle row by the new digit, and add it to the fixed divisor.
10. Divide the new dividend by the updated divisor to obtain the next digit of the cube root.
11. Repeat the process until all digits are exhausted.
12. If the division does not terminate, the cube root cannot be exactly extracted.
13. If the volume has fractions, convert them to a common denominator and proceed as above.
14. After extracting the cube root of the numerator, extract the cube root of the denominator.
15. If the denominator cannot be exactly extracted, multiply the numerator by the square of the denominator and proceed as above.

Answer: *a* chi.
"""

# Define the volume
積 = 1860867

# Initialize variables
商 = 0  # The result (cube root)
餘 = 積  # The remainder
位 = 0  # Current digit position

# Step through the digits, skipping two places at a time
while 餘 > 0:
    # Borrow one counting rod (determine the next digit of the cube root)
    借 = 1
    while (借 ** 3) <= 餘:
        借 += 1
    借 -= 1

    # Update the cube root
    商 = 商 * 10 + 借

    # Calculate the divisor
    法 = 借 ** 2 * 3

    # Subtract the product from the remainder
    餘 -= 借 ** 3

    # Bring down the next group of digits (if applicable)
    餘 *= 1000  # Simulate bringing down the next group of digits

    # Increment the digit position
    位 += 1

# The result is the cube root
a = 商
"""
"""
