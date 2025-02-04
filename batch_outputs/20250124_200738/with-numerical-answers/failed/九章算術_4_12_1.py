"""
又有積二萬五千二百八十一步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=159)步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 25,281 bu.
Question: what is the side length of the square field?

The procedure for extracting square roots says:
Place the area as the dividend. Borrow one counting rod to represent the side length, skipping one place.
Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide.
After dividing, double the divisor to form the fixed divisor. Divide again.
Reduce the divisor and lower it. Place the borrowed counting rod as before, and estimate again.
Multiply the estimate by itself to form the auxiliary value, add it to the fixed divisor, and divide.
Subtract the auxiliary value from the fixed divisor. Continue dividing and reducing as before.
If the square root cannot be fully extracted, it is considered "not exact" and should be expressed as a side length with a remainder.
If the dividend has fractions, convert the fractions into a common denominator and treat them as integers for the calculation.
After completing the square root extraction, also extract the square root of the denominator to report the result.
If the denominator cannot be square-rooted, multiply the denominator by the fixed dividend and extract the square root again, ensuring the result matches the denominator.

Answer: *a*(=159) bu.
"""

# 積二萬五千二百八十一步
積 = 25281

# 開方術
# Step 1: Initial estimation
借算 = 1  # Start with 1 as the initial estimate
法 = 借算 * 借算  # 法 = 1^2 = 1
所得 = 積 // 法  # Divide the area by the initial divisor
定法 = 2 * 借算  # Double the borrowed value to form the fixed divisor

# Step 2: Iterative refinement
while True:
    剩餘 = 積 - (所得 * 所得)  # Calculate the remaining area
    if 剩餘 == 0:  # If the remainder is 0, the square root is exact
        break
    借算 += 1  # Increment the borrowed value
    法 = 借算 * 借算  # Update the divisor
    所得 = 積 // 法  # Recalculate the quotient
    定法 = 2 * 借算  # Update the fixed divisor

# Final result
a = 所得  # 159#----- content ends here -----

"""
Timed out"""
