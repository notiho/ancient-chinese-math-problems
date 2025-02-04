"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
開立方術曰：置積為實。借一算步之，超二等。議所得，以再乘所借一算為法，而除之。除已，三之為定法。復除，折而下。以三乘所得數置中行。復借一算置下行。步之，中超一，下超二等。復置議，以一乘中，再乘下，皆副以加定法。以定法除。除已，倍下、并中從定法。復除，折下如前。開之不盡者，亦為不可開。若積有分者，通分內子為定實。定實乃開之，訖，開其母以報除。若母不可開者，又以母再乘定實，乃開之。訖，令如母而一。
荅曰： a(=123)尺 。
"""

"""
Suppose there is a volume of 1,860,867 cubic chi.
Question: what is the cube root of this volume, expressed in chi?

The procedure for extracting the cube root says: Place the volume as the dividend. Borrow one counting rod and step it, skipping two places. 
Evaluate the resulting number, and multiply it twice by the borrowed counting rod to form the divisor. Divide by this divisor. After dividing, multiply by 3 to form the fixed divisor. Divide again, and reduce the remainder. 
Multiply the resulting number by 3 and place it in the middle row. Borrow one counting rod again and place it in the bottom row. Step it, skipping one place in the middle and two places in the bottom. 
Evaluate again, multiply the middle by 1 and the bottom by 2, and add these to the fixed divisor. Divide by the fixed divisor. After dividing, double the bottom and add it to the middle to form the next fixed divisor. Divide again, reducing the remainder as before. 
If the volume cannot be completely divided, it is considered not extractable. If the volume has fractions, convert the fractions into a common denominator to form the fixed dividend. Extract the cube root of the fixed dividend, and then extract the cube root of the denominator to report the result. If the denominator cannot be extracted, multiply the denominator twice by the fixed dividend and extract the cube root. Finally, adjust the result to match the denominator.

Answer: *a*(=123) chi.
"""

# 置積為實
積 = 1860867

# 開立方術
# Step 1: Initialize variables
實 = 積
商 = 0

# Step 2: Iteratively extract the cube root
while True:
    # Borrow one rod and skip two places
    借 = int(實 ** (1/3))  # Approximate cube root
    if 借 ** 3 > 實:
        借 -= 1
    
    # Multiply twice by the borrowed rod to form the divisor
    法 = 3 * (借 ** 2)
    
    # Divide to find the next digit of the cube root
    商 += 借
    實 -= 借 ** 3
    
    # Check if the remainder is zero
    if 實 == 0:
        break
    
    # If the remainder is not zero, continue the process
    if 實 < 0:
        raise ValueError("Cannot extract exact cube root.")
    
a = 商  # 123
"""
Variable 'a' has wrong value. Expected: 123, Actual: 183"""
