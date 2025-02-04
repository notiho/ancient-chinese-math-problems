"""
又有積七萬一千八百二十四步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=268)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 71824 bu².
Question: what is the side length of the square field?

The procedure for extracting square roots says: Place the area as the dividend. Borrow one counting rod to mark the position, skipping one place. Estimate the result. Multiply the estimate by the borrowed counting rod to form the divisor, and divide. After dividing, double the divisor to form the fixed divisor. Divide again. Subtract the divisor and bring down the next digit. Repeat the process by placing the borrowed counting rod as before, estimating, multiplying, and adding to the fixed divisor. Divide again. Subtract and bring down as before. If the square root cannot be exact, it is considered unsolvable, and the side length is given as the approximate value. If the dividend has fractions, convert the fractions to the same denominator as the whole number and proceed. After completing the square root extraction, if the denominator cannot be square-rooted, multiply the numerator by the denominator and extract again, ensuring the denominator remains as 1.

Answer: *a*(=268) bu.
"""

# 置積為實
積 = 71824

# 開方術
# Step 1: Initialize variables
實 = 積
商 = 0
位 = 0

# Step 2: Determine the number of digits in the dividend
while 實 >= 100:
    實 //= 100
    位 += 1

# Step 3: Restore the original dividend
實 = 積

# Step 4: Perform the square root extraction
for i in range(位, -1, -1):
    # Borrow one rod and estimate
    借 = 10**i
    定法 = 2 * 商 * 借
    副 = 0
    while (定法 + 副) * 副 <= 實:
        副 += 1
    副 -= 1

    # Update 商 and 實
    商 = 商 * 10 + 副
    實 -= (定法 + 副) * 副

# Final result
a = 商  # 268#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 268, Actual: 26800"""
