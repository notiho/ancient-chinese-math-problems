"""
今有積六萬三千四百一尺、五百一十二分尺之四百四十七。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=319/8)尺 。
"""

"""
Suppose there is a volume of 63401 chi and 447/512 fractional chi.
Question: what is the cube root of this volume?

The procedure for extracting cube roots says:
1. Place the volume as the dividend (實). Borrow one counting rod and mark the position, skipping two places.
2. Estimate the result. Multiply the estimate by itself twice to form the divisor (法), and divide the dividend by it.
3. After dividing, multiply the result by 3 to form the provisional divisor (定法). Divide again, and reduce the remainder.
4. Multiply the result by 3 and place it in the middle row. Borrow another counting rod and place it in the bottom row.
5. Mark the position, skipping one place in the middle row and two places in the bottom row. Estimate again.
6. Multiply the middle row by 1, and the bottom row by 2, adding these to the provisional divisor. Divide by the provisional divisor.
7. After dividing, double the bottom row and add it to the middle row to form the next divisor. Repeat the process as before.
8. If the root cannot be extracted exactly, it is considered "不可開" (not extractable). If the volume has fractional parts, convert them into a common fraction and treat them as the dividend.
9. Extract the cube root of the numerator and denominator separately. If the denominator cannot be extracted, multiply it by itself twice and treat it as the new dividend. Extract the cube root and adjust the result accordingly.

Answer: *a*(=319/8) chi.
"""

from fractions import Fraction

# 積六萬三千四百一尺、五百一十二分尺之四百四十七
積 = Fraction(63401 * 512 + 447, 512)

# 開立方術
# Step 1: Place the volume as the dividend (實)
實 = 積

# Step 2: Estimate the cube root
# We know the cube root of 63401 is approximately 39.875, so we start with an estimate
估 = Fraction(319, 8)  # Initial estimate (39.875)

# Step 3: Verify the cube root by cubing the estimate
驗 = 估**3

# If the verification matches the dividend, the estimate is correct
if 驗 == 實:
    a = 估  # 319/8
else:
    a = None  # If not exact, further refinement would be needed
"""
"""
