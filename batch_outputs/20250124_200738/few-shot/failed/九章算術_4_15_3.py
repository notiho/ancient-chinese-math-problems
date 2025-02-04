"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a步 。
"""

"""
This problem involves finding the square root of a very large number using an ancient Chinese method of extracting square roots, which is a step-by-step manual process. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

"""
Suppose there is an area of 3,970,215,625 bu². 
Question: what is the side length of the square field?

The procedure for extracting square roots says:
Place the area as the dividend. Borrow one counting rod and place it, skipping one position.
Estimate the result. Multiply the borrowed counting rod by itself to form the divisor, and divide.
After dividing, double the divisor to form the fixed divisor. Divide again.
Subtract the divisor and bring down the next digit. Repeat the process.
If the square root cannot be fully extracted, it is considered unsolvable, and the side length is expressed as a fraction.
If the area has a fractional part, convert it to a common fraction and proceed with the extraction.
Once completed, extract the square root of the numerator and denominator separately.
If the denominator cannot be extracted, multiply the denominator by the fixed numerator and extract again.

Answer: *a* bu.
"""

from fractions import Fraction

# 積三十九億七千二百一十五萬六百二十五步
積 = 3970215625

# 開方術
def 開方(積):
    # 置積為實
    實 = 積

    # 初始化
    借算 = 0
    定法 = 0
    副 = 0
    開方結果 = 0

    # 開方過程
    while 實 > 0:
        # 借一算步之，超一等
        借算 = int(實 ** 0.5)
        實 -= 借算 ** 2

        # 議所得，以一乘所借一算為法，而以除
        法 = 借算 * 2
        if 法 == 0:
            break

        # 除已，倍法為定法
        定法 = 法 * 2

        # 折法而下
        副 = 實 // 定法
        開方結果 = 開方結果 * 10 + 副

        # 復置借算步之如初，以復議一乘之
        實 -= 副 * 定法

    # 若開之不盡者為不可開，當以面命之
    if 實 > 0:
        return Fraction(積).sqrt()

    return 開方結果

# 計算結果
a = 開方(積)
print(f"荅曰：{a}步。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initialization**: The total area (`積`) is set as the dividend (`實`). Variables for intermediate calculations (`借算`, `定法`, `副`, `開方結果`) are initialized.
2. **Iterative Square Root Extraction**:
   - Estimate the largest possible digit (`借算`) such that its square is less than or equal to the current dividend.
   - Subtract the square of the estimate from the dividend.
   - Double the estimate to form the divisor (`定法`).
   - Divide the remaining dividend by the divisor to get the next digit of the square root (`副`).
   - Subtract the product of the divisor and the digit from the dividend and repeat.
3. **Handling Remainders**: If the square root cannot be fully extracted (i.e., there is a remainder), the result is expressed as a fraction.
4. **Output**: The final square root is printed.

This code follows the ancient Chinese procedure for extracting square roots step by step. If the square root cannot be fully extracted, it uses fractions to represent the result.
"""


"""
Variable 'a' has wrong value. Expected: 63025, Actual: 0"""
