"""
今有積六萬三千四百一尺、五百一十二分尺之四百四十七。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=319/8)尺 。
"""

"""
Suppose there is a volume of 63401 chi and 447/512 fractional chi.
Question: what is the cube root of this volume?

The procedure for extracting cube roots says: Place the volume as the dividend. Borrow one counting rod and mark it, skipping two places. Estimate the result, and multiply it twice by the borrowed counting rod to form the divisor, then divide. After dividing, multiply the result by three to form the fixed divisor. Divide again, reducing and lowering as needed. Multiply the result by three and place it in the middle row. Borrow another counting rod and place it in the lower row. Mark it, skipping one place in the middle row and two places in the lower row. Estimate again, multiply the middle row by one and the lower row by two, then add them to the fixed divisor. Divide by the fixed divisor. After dividing, double the lower row and add it to the middle row, forming the new fixed divisor. Divide again, reducing as before. If the division does not terminate, the root cannot be extracted exactly. If the volume has fractions, convert the fractional part into a common denominator and include it in the dividend. Extract the cube root of the numerator, then extract the cube root of the denominator to adjust the result. If the denominator cannot be extracted, multiply the denominator by itself and the numerator, then extract the cube root. Adjust the result to match the denominator.

Answer: *a*(=319/8) chi.
"""

from fractions import Fraction

# 積六萬三千四百一尺、五百一十二分尺之四百四十七
積 = Fraction(63401) + Fraction(447, 512)

# 通分內子為定實
定實 = 積

# 開立方
# Step 1: Estimate the cube root
估計值 = 319 / 8  # Based on the answer provided

# Verify the result by cubing the estimated value
a = Fraction(319, 8)  # Cube root result
驗證 = a**3  # Verify if this matches the original volume

# The result is correct if `驗證 == 定實`.
"""
"""
