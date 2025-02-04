"""
今有積六萬三千四百一尺、五百一十二分尺之四百四十七。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=319/8)尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 63401 chi and 447/512 fractional chi.
Question: what is the cube root of this volume?

The procedure for extracting the cube root says:
1. Place the volume as the dividend. Borrow one counting rod and mark it, skipping two places.
2. Estimate the result, and multiply it twice by the borrowed counting rod to determine the divisor. Divide by this divisor.
3. After dividing, multiply the result by 3 to establish the fixed divisor. Divide again, reducing the remainder as necessary.
4. Multiply the result by 3 and place it in the middle row. Borrow one counting rod and place it in the bottom row. Mark it, skipping one place in the middle row and two places in the bottom row.
5. Estimate again, multiply the middle row by 1 and the bottom row by 2, adding these to the fixed divisor. Divide by the fixed divisor.
6. After dividing, double the bottom row and add it to the middle row to update the fixed divisor. Divide again, reducing the remainder as before.
7. If the volume cannot be fully divided, it is considered unsolvable. If the volume has fractional parts, convert them to a common denominator to form the dividend. Extract the cube root of the numerator and denominator separately. If the denominator cannot be extracted, multiply it twice by the numerator and extract the cube root of the result. Adjust the result to match the denominator.

Answer: *a*(=319/8) chi.
"""

from fractions import Fraction

# 定積
積 = Fraction(63401) + Fraction(447, 512)

# 開立方術
# Step 1: Convert the volume into a single fraction
積分母 = 積.denominator
積分子 = 積.numerator

# Step 2: Extract the cube root of the numerator and denominator separately
分子立方根 = round(積分子 ** (1 / 3), 8)
分母立方根 = round(積分母 ** (1 / 3), 8)

# Step 3: Check if the denominator can be perfectly extracted
if not 分母立方根.is_integer():
    # If not, multiply the denominator twice by the numerator and extract the cube root
    積分母 = 積分母 ** 2
    積分子 = 積分子 * 積分母
    分子立方根 = round(積分子 ** (1 / 3), 8)
    分母立方根 = round(積分母 ** (1 / 3), 8)

# Step 4: Adjust the result to match the denominator
if 分母立方根.is_integer():
    分母立方根 = int(分母立方根)
    分子立方根 = int(分子立方根)
    a = Fraction(分子立方根, 分母立方根)  # 319/8
else:
    a = None  # Cannot be solved

a  # Result: 319/8#----- content ends here -----

"""
"""
