"""
又有積五十六萬四千七百五十二步、四分步之一。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This is a classic square root extraction problem from ancient Chinese mathematics. The procedure involves iterative steps to extract the square root of a given number. Let's translate the procedure into Python code step by step.

The problem states that the area is 564752 and 1/4 of a step, and we are tasked to find the side length of the square.


"""


from fractions import Fraction

# 積五十六萬四千七百五十二步、四分步之一
積 = Fraction(564752, 1) + Fraction(1, 4)

# 開方術曰：置積為實
實 = 積

# 開方術步驟
# Step 1: Borrow one counting rod (算) and determine the initial estimate of the square root
借算 = 1
while (借算 + 1) ** 2 <= 實:
    借算 += 1

# Step 2: Multiply the borrowed counting rod by itself to find the divisor (法)
法 = 借算 * 2

# Step 3: Subtract the square of the borrowed counting rod from the area
餘 = 實 - 借算 ** 2

# Step 4: Iteratively refine the square root
while 餘 > 0:
    # Double the divisor
    法 = 法 * 2

    # Determine the next digit of the square root
    副 = 0
    while (法 + 副 + 1) * (副 + 1) <= 餘:
        副 += 1

    # Update the square root and remainder
    借算 = 借算 * 10 + 副
    餘 = 餘 - (法 + 副) * 副

# Final result
a = Fraction(借算, 10)
print(f"方為 {a} 步")


"""


### Explanation of the Code:
1. **Initialization**: The area (`積`) is given as `564752` and `1/4`. This is converted into a `Fraction` to handle the fractional part accurately.
2. **Initial Estimate**: The largest integer whose square is less than or equal to the area is found (`借算`).
3. **Iterative Refinement**: The square root is refined digit by digit using the ancient method of doubling the divisor (`法`) and subtracting the square of the current estimate from the remainder (`餘`).
4. **Fractional Handling**: If the area has a fractional part, the procedure continues to refine the square root until the fractional part is resolved.

The final result is the side length of the square (`a`), expressed in steps (`步`).
"""


"""
Code error: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit"""
