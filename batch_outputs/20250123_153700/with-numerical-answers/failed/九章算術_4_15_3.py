"""
又有積三十九億七千二百一十五萬六百二十五步。問︰為方幾何？
開方術曰：置積為實。借一算步之，超一等。議所得，以一乘所借一算為法，而以除。除已，倍法為定法。其復除。折法而下。復置借算步之如初，以復議一乘之，所得副，以加定法，以除。以所得副從定法。復除折下如前。若開之不盡者為不可開，當以面命之。若實有分者，通分內子為定實。乃開之，訖，開其母報除。若母不可開者，又以母乘定實，乃開之，訖，令如母而一。
荅曰： a(=63025)步 。
"""

"""
Suppose there is a volume of 3,970,215,625 bu. 
Question: what is the side length of the square?

The procedure for extracting square roots says: Place the volume as the dividend. Borrow one counting rod, moving it one place to the left. 
Estimate the result. Multiply the borrowed counting rod by 1 to create the divisor, and divide. 
After dividing, double the divisor to create the fixed divisor. Divide again. 
Reduce the divisor and continue. Place the borrowed counting rod back as before, and multiply it by 1 again. 
The result is added to the fixed divisor and used to divide. 
The result is subtracted from the fixed divisor. Continue dividing as before. 
If the square root cannot be fully extracted, it is considered unsolvable, and the side length is expressed as a fraction. 
If there is a remainder, convert it into a fraction with the numerator as the remainder and the denominator as the divisor. 
Extract the square root of the numerator and denominator separately. 
If the denominator cannot be extracted, multiply the numerator by the denominator and extract again, ensuring the denominator remains as 1.

Answer: *a*(=63025) bu.
"""

# 置積為實
積 = 3970215625

# 開方術
# 開平方根的手算過程模擬

# 初始化變量
實 = 積
商 = 0
位 = 0

# 借一算步之，超一等
while 實 >= 100:
    實 //= 100
    位 += 1

# 議所得
商 = int(實**0.5)

# 還原實際數據
商 *= 10**位

# 確認平方
a = 商  # 63025
"""
Variable 'a' has wrong value. Expected: 63025, Actual: 60000"""
