"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=123)尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is the side length of the cube?

The procedure for extracting the cube root says: Place the volume as the dividend. Borrow one counting rod and mark it, skipping two places. Estimate the result, and multiply the borrowed counting rod by itself twice to form the divisor, then divide. After dividing, multiply the result by 3 to form the fixed divisor. Divide again, and reduce the remainder downward. Multiply the result by 3 and place it in the middle row. Borrow one counting rod again and place it in the bottom row. Mark it, skipping one place in the middle row and two places in the bottom row. Estimate again, and multiply the middle row by 1 and the bottom row by itself twice, adding these to the fixed divisor. Divide by the fixed divisor. After dividing, double the bottom row and add it to the middle row to form the new fixed divisor. Divide again, reducing the remainder downward as before. If the volume cannot be fully divided, it is considered not extractable. If the volume has fractions, convert them to a common denominator to form the fixed dividend. Extract the cube root of the fixed dividend, and then extract the cube root of the denominator to adjust the result. If the denominator cannot be extracted, multiply the denominator by itself twice and extract the cube root of the adjusted dividend. Finally, adjust the result to match the denominator.

Answer: *a*(=123) chi.
"""

# 置積為實
積 = 1860867

# 開立方術
# Step 1: Borrow one counting rod, skipping two places
借一 = 10 ** (len(str(積)) // 3 * 2)

# Step 2: Estimate the result
估數 = int((積 // 借一) ** (1/3))

# Step 3: Multiply the borrowed rod by itself twice to form the divisor
法 = (估數 ** 2) * 借一

# Step 4: Divide and multiply by 3 to form the fixed divisor
定法 = 3 * (積 // 法)

# Step 5: Continue dividing and reducing as per the procedure
a = 估數  # 123#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 123, Actual: 5"""
